#from graphviz import Source
import csv
import numpy as np
import re
import os
np.set_printoptions(threshold=np.inf)

class generateMap(object):

    def __init__(self):
        pass

    def createMatrix(self):
        self.desAttackList = []
        self.srcAttackList = []
        self.rewardList = []#contain all rewards
        self.rewardDict = {}#contain node number with reward
        self.qq = {}
        # all the nodes with names and scores
        self.csvfile = open('VERTICES.CSV', 'r')
        #self.csvfile = open('VERTICES.CSV', 'r')
        # each connected pair of nodes
        self.arcscsv = open('ARCS.CSV', 'r')
        #self.arcscsv = open('ARCS.CSV', 'r')
        self.arcsCsvData = self.arcscsv.readlines()
        self.allCsvData = self.csvfile.readlines()
        self.endLine = self.allCsvData[-1]
        #get the last node in the graph
        self.line=int(self.endLine.split(',')[0])
        #matrix of - ones (44,44)
        self.MAP = -(np.ones((self.line, self.line), dtype=np.float))
        self.i = 0

        for self.csvdata in self.allCsvData:#loop foreach node in the graph and give a reward based on the type of node
            if(len(re.findall('execCode', self.csvdata)) > 0):#if node contain execcode commnad
                if(self.i == 0):#give a score of 100 if the node is the first one else give it 0.3
                    self.rewardList.append(100.0)
                    self.rewardDict[self.i] = 100.0
                else:
                    self.rewardList.append(0.3)
                    self.rewardDict[self.i] = 0.3

            elif(len(re.findall('vulExists', self.csvdata)) > 0):#if node represent some vul
                
                self.cveNumber = self.csvdata.split('(')[1].split(',')[1].split("'")[1]#get the vul number
                self.cve_base_score, self.cve_exploitablity_score = self.get_cvss_score(self.cveNumber)#retrieve scores
                
                self.cvss_score = self.cve_base_score * (self.cve_exploitablity_score/10)#calc the final score
                self.rewardList.append(self.cvss_score)
                self.rewardDict[self.i] = self.cvss_score
                self.qq[self.i] = self.cvss_score # any ul with its score
           
            elif(len(re.findall('attackerLocated', self.csvdata)) > 0):#the node is the start node (not the node 1 )
                self.startLabel = self.csvdata.split('(')[1].split(')')[0]
                if(self.startLabel == 'internet'):
                    self.rewardList.append(0.01)
                    self.rewardDict[self.i] = 0.01

            else:#reward for the rest nodes
                self.rewardList.append(0.1)
                self.rewardDict[self.i] = 0.1

            self.i = self.i + 1
        for self.data in self.allCsvData:
            if(len(re.findall('RULE 2', self.data)) > 0):# rule is (remote exploit of a server program)
                #update rewards for all (RULE 2) that have a conncetion to vulExist node
                #remote code execution for having full access for the target
                for self.a in self.qq:
                    for self.b in self.arcsCsvData:
                        if int(self.a) == int(self.b.split(',')[1]) - 1 :
                            if self.allCsvData.index(self.data) == int(self.b.split(',')[0]) - 1:
                                self.rewardDict[self.allCsvData.index(self.data)] = self.qq[self.a] #give the source node the same reward as the vul
                                
        #self.txtfile = open('AttackGraph.txt', 'r')
        self.txtfile = open('AttackGraph.txt', 'r')
        self.allTxtData = self.txtfile.readlines()

        for self.txtdata in self.allTxtData:  #each line in the attack_graph.txt
            if(len(re.findall('"', self.txtdata)) == 0):#choose all lines that in form num1,num2,-1
                self.desAttack = int(self.txtdata.split(',')[0]) #num1 is the destination
                self.srcAttack = int(self.txtdata.split(',')[1]) #num2 is the source
                self.desAttackList.append(self.desAttack)
                self.srcAttackList.append(self.srcAttack)

                self.state = [(self.srcAttack - 1), (self.desAttack - 1)] #rows of map are sources, columns of map is destination
                self.location = self.MAP[tuple(self.state)]

                #put the reward value in the intersection of each source and destination
                if(self.srcAttack > self.desAttack):#for prevent looping
                    if(self.rewardDict[self.srcAttack - 1] == 0.01):
                        self.MAP[tuple(self.state)] = self.rewardDict[self.srcAttack - 1]
                    elif(self.rewardDict[self.desAttack - 1] == 100.0):                       
                        self.MAP[tuple(self.state)] = self.rewardDict[self.desAttack - 1]
                    else:                    
                        self.MAP[tuple(self.state)] = (self.rewardDict[self.srcAttack - 1] + self.rewardDict[self.desAttack - 1])#sum the rewards for the both
                else:
                    self.MAP[tuple(self.state)] = 0.0
        return self.MAP

    def get_cvss_score(self, cveNumber):
        #with open('CVE_Info_Dataset.csv', 'r') as self.csvfile:
        with open('CVE_Info_Dataset.csv', 'r') as self.csvfile:
            self.allCveData = csv.reader(self.csvfile)
            for self.cvedata in self.allCveData:
                if self.cveNumber == self.cvedata[0]:
                    self.cve_base_score = float(self.cvedata[2])
                    self.cve_exploitablity_score = float(self.cvedata[3])
                    return self.cve_base_score, self.cve_exploitablity_score
                    
    @property
    def sendMap(self):
        self.x = self.createMatrix()
        return self.x

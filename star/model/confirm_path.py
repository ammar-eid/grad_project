import os
import sys
from generateMap import generateMap
import numpy as np
np.set_printoptions(suppress=True)

MAP = generateMap().sendMap

edgeLinks = dict() #all edges from source to destination

score_value=lambda a,b:MAP[tuple([int(a)-1,int(b)-1])] #get score from a to b

def get_neighbors(v):
    return edgeLinks[v]
# This is heuristic function which is having equal values for all nodes
def h( n):
    return { x:1 for x in edgeLinks.keys()}[n]

def a_star_algorithm( s, e):
    # In this open_lst is a lisy of nodes which have been visited, but who's
    # neighbours haven't all been always inspected, It starts off with the start node
    # And closed_lst is a list of nodes which have been visited
    # and who's neighbors have been always inspected
    open_lst = set([s])
    closed_lst = set([])
    # poo has present distances from start to all other nodes
    # the default value is +infinity
    poo = {}
    poo[s] = 0
    # par contains an adjac mapping of all nodes
    par = {}
    par[s] = s
    while len(open_lst) > 0:
        n = None
        # it will find a node with the lowest value of f() -
        for v in open_lst:
            if n == None or poo[v] + h(v) < poo[n] + h(n):
                n = v;
        if n == None:
            print('Path does not exist!')
            return None
        # if the current node is the stop
        # then we start again from start
        if n == e:
            reconst_path = []
            while par[n] != n:
                reconst_path.append(n)
                n = par[n]
            reconst_path.append(s)
            reconst_path.reverse()
            return reconst_path

        # for all the neighbors of the current node do
        for (m, weight) in get_neighbors(n):
            # if the current node is not present in both open_lst and closed_lst
            # add it to open_lst and note n as it's par
            if m not in open_lst and m not in closed_lst:
                open_lst.add(m)
                par[m] = n
                poo[m] = poo[n] + weight

            # otherwise, check if it's quicker to first visit n, then m
            # and if it is, update par data and poo data
            # and if the node was in the closed_lst, move it to open_lst
            else:
                if poo[m] > poo[n] + weight:
                    poo[m] = poo[n] + weight
                    par[m] = n

                    if m in closed_lst:
                        closed_lst.remove(m)
                        open_lst.add(m)

        # remove n from the open_lst, and add it to closed_lst
        # because all of his neighbors were inspected
        open_lst.remove(n)
        closed_lst.add(n)
    print('Path does not exist!')
    return None

def addEdge(a,b):
    if a not in edgeLinks:
        edgeLinks[a] = list() #add source
    if b not in edgeLinks:
        edgeLinks[b] = list() #add destination
    edgeLinks[a].append(tuple([b,score_value(a,b)])) #key is source and value is destination+score for travelling

def load():
    with open('./processdata/ARCS.txt', 'r') as ff:
        lines = ff.readlines() #all arcs between nodes
        for i in lines:
            b,a,_ = i.split(',')
            addEdge(a,b) #add to dict of source and dest

if __name__ == '__main__':
    start=str(np.array(list(zip(*np.where(MAP==0.01))))[0][0]+1)
    end =str(1)
    load()
    csvfile = open('../mulval_result/VERTICES.CSV', 'r')
    allCsvData = csvfile.readlines()
    for x in a_star_algorithm(start, end):
        print(x,end=" ")
        print(allCsvData[int(x)-1].split('"')[1])
    

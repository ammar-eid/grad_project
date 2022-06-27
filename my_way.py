import numpy as np
import json
import csv
import os
import sys

map=np.loadtxt("newmap.txt")
path_num=np.argmax(map[0])


def decode_path(all_paths, path_index):
    topList = []
    nodeBeforeList = []
    nodeBeforeDict = {}
    mulvalPathFileList = []
    mulvalFileList = []
    for pathdata in all_paths[path_index]:
        topNode = int(pathdata[0]) + 1
        topList.append(topNode)
    topList.append(1)

    #mulvalFile = open('../../mulval_result/VERTICES.CSV', 'r')
    mulvalFile = open('VERTICES.CSV', 'r')
    mulvalFile_csv = csv.reader(mulvalFile)
    #mulvalPathFile = open('../../mulval_result/ARCS.CSV', 'r')
    mulvalPathFile = open('ARCS.CSV', 'r')
    mulvalPathFile_csv = csv.reader(mulvalPathFile)

    #print(topList)

    for pathdata in mulvalPathFile_csv:
        mulvalPathFileList.append((int(pathdata[0]), int(pathdata[1])))

    for infodata in mulvalFile_csv:
        mulvalFileList.append((int(infodata[0]), str(infodata[1])))

    for perNode in topList:
        nodeBeforeList = []
        for pathData in mulvalPathFileList:
            if perNode == pathData[0]:
                nodeBeforeList.append(pathData[1])
        nodeBeforeDict.update({perNode: nodeBeforeList})

    vulAttackDict = {}

    for pernodeBefore in nodeBeforeDict.items():
        for pernodeBeforedata in pernodeBefore[1]:
            for infoData in mulvalFileList:
                if int(pernodeBeforedata) == int(infoData[0]):
                    if infoData[1].split(',')[0].find('vulExists') != -1:
                        vul = (infoData[1].split(',')[0].split('(')[1], infoData[1].split(',')[1])
                        vulAttackDict.update({pernodeBefore[0]: (vul)})
                    elif infoData[1].split(',')[0].find('Trojan') != -1:
                        if infoData[0] in topList:
                            vulAttackDict.update({infoData[0]: 'Trojan'})

    #with open("../../Penetration_tools/attack_info.json","w") as f:
    with open("attack_info.json", "w") as f:
            json.dump(vulAttackDict,f)

    print('Attack information according to Nmap scanning result:')
    print(vulAttackDict)

    mulvalFile.close()
    mulvalPathFile.close()

def start():
    model = "nmap"
    try:
        state_path = path_num - 1
        all_paths = np.load('all_paths.npy', allow_pickle=True)
        all_paths = all_paths.tolist()
        if model == 'nmap':
            decode_path(all_paths, state_path)
        print("AutoPentest-DRL: Optimal attack path was computed successfully")
        print("                 (labels match 'mulval_result/AttackGraph.pdf')")
        for i in all_paths[state_path]:
            # Add 1 to match label values in MulVAL attack graph
            print(str(i[0]+1) + ' > ', end='')
            # Add 1 to match label values in MulVAL attack graph
        print(str(0+1))
    except KeyboardInterrupt:
        print ("\nKeyboard interrupt detected => end execution")
    sys.exit(1)



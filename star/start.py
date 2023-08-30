import os
import tkinter.font as font
from tkinter import *
import real_attack as rl
window_main = Tk()
button=lambda x,y,z:Button(x,text=y,command=z,bg='#0f4b6e',fg="white",font=font.Font(size=12),pady=5)

def logical_attack():
    os.system("python3 AutoPentest-DRL.py logical_attack")
#---------------------------start information gathering---------------------------
def info_gath():
        window_info_gath=Tk()
        window_info_gath.config(bg="#0f4b6e")
        window_info_gath.geometry("400x320")
        window_info_gath.title("real attack data")
        btn_info_gath = button(window_info_gath,"you dont know ip ?",host2ip).pack()
        btn_pw_attack = button(window_info_gath,"nmap",nmap).pack()
        btn_net_test = button(window_info_gath,"scanning wordpress",scan_wp).pack()
        btn_exp_tools = button(window_info_gath,"CSMS scanner",cms_scanner).pack()
        btn_sniff_spoof = button(window_info_gath,"emails, subdomain", multi).pack()
        btn_web_hack = button(window_info_gath,"Web content scanner", dirb).pack()
        btn_Exit = button(window_info_gath,"Back", window_info_gath.destroy).pack()
def host2ip():
    window=Tk()
    window.config(bg="#0f4b6e")
    window.title("host2ip")
    hot_name_lbl = Label(window, text='host Name', bg='#0f4b6e', fg='white').pack()
    host_name_tf=Entry(window,width=40)
    ok_btn=Button(window,text='  OK  ',bg='#0f4b6e',fg="white",font=font.Font(size=12),pady=5,command=lambda:rl.host2ip(host_name_tf.get()))
    host_name_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn=button(window,'cancel',window.destroy).pack(side="right")
def nmap():
    window=Tk()
    window.config(bg="#0f4b6e")
    window.geometry("390x155")
    window.title("nmap")
    title_lbl = Label(window, text='Knowing the ip address of the target hostname is crucial\nsince it\'s used for many tools in pen testing',\
                      bg='#0f4b6e', fg='white').pack()
    ip_lbl = Label(window, text='IP :', bg='#0f4b6e', fg='white',font=font.Font(size=12)).pack()
    ip_tf=Entry(window,width=40)
    scan_type_lbl = Label(window, text='scan type :', bg='#0f4b6e', fg='white',font=font.Font(size=12))
    scan_type_tf=Entry(window,width=40)
    ok_btn=Button(window,text='  OK  ', bg='#0f4b6e', fg='white',font=font.Font(size=12),command=lambda:rl.nmap(ip_tf.get(),scan_type_tf.get()))
    ip_tf.pack()
    scan_type_lbl.pack()
    scan_type_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn=button(window,'cancel',window.destroy).pack(side="right")
def scan_wp():
    window=Tk()
    window.config(bg="#0f4b6e")
    window.geometry("400x120")
    window.title("scan wordpress")
    title_lbl = Label(window,text='Scanning WordPress to identify the security-related problems on\nthe WordPress site', \
                      bg='#0f4b6e', fg='white').pack()
    target_lbl = Label(window, text='write the target name', bg='#0f4b6e', fg='white', font=font.Font(size=12)).pack()
    target_tf = Entry(window, width=40)
    ok_btn = Button(window, text='  OK  ', bg='#0f4b6e', fg='white', font=font.Font(size=12),
                    command=lambda: rl.swp(target_tf.get()))
    target_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn = button(window, 'cancel', window.destroy).pack(side="right")
def cms_scanner():
    window=Tk()
    window.geometry("400x120")
    window.config(bg="#0f4b6e")
    window.title("cms scan")
    title_lbl = Label(window, text='CMS scanner automates the method of detecting security flaws\nof the foremost popular CMSs', \
                      bg='#0f4b6e', fg='white').pack()
    target_lbl = Label(window, text='write the target name', bg='#0f4b6e', fg='white', font=font.Font(size=12)).pack()
    target_tf = Entry(window, width=40)
    ok_btn = Button(window, text='  OK  ', bg='#0f4b6e', fg='white', font=font.Font(size=12),
                    command=lambda: rl.cms_scan(target_tf.get()))
    target_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn = button(window, 'cancel', window.destroy).pack(side="right")
def multi():
    window = Tk()
    window.geometry("400x120")
    window.config(bg="#0f4b6e")
    window.title("multi scan")
    title_lbl = Label(window,
                      text='using the harvester for gathering email and subdomain information', \
                      bg='#0f4b6e', fg='white').pack()
    target_lbl = Label(window, text='Enter the hostname address: ', bg='#0f4b6e', fg='white', font=font.Font(size=12)).pack()
    target_tf = Entry(window, width=40)
    ok_btn = Button(window, text='  OK  ', bg='#0f4b6e', fg='white', font=font.Font(size=12),
                    command=lambda: rl.multi(target_tf.get()))
    target_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn = button(window, 'cancel', window.destroy).pack(side="right")
def dirb():
    window = Tk()
    window.geometry("400x150")
    window.config(bg="#0f4b6e")
    window.title("dirb")
    title_lbl = Label(window,
                      text='Web Content Scanner looks for existing (and/or hidden) Web Objects.\n'+
                           'important paths to that might contain useful information:\n /robots.txt, /phpmyadmin, /wp-login', \
                      bg='#0f4b6e', fg='white').pack()
    target_lbl = Label(window, text='Enter the hostname address: ', bg='#0f4b6e', fg='white',
                       font=font.Font(size=12)).pack()
    target_tf = Entry(window,width=40)
    ok_btn = Button(window, text='  OK  ', bg='#0f4b6e', fg='white', font=font.Font(size=12),
                    command=lambda: rl.dirb(target_tf.get()))
    target_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn = button(window, 'cancel', window.destroy).pack(side="right")
#---------------------------end information gathering---------------------------
#---------------------------start password attacks---------------------------
def pw_attack():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("300x300")
    window.title("Password Attacks")
    Label(window, bg='#0f4b6e', \
          font=font.Font(size=14), fg="white", \
          text="--------------------Password Attacks--------------------").pack()
    button(window, "FTP Brute-Force Attack", ftp_atk).pack()
    button(window, "MD5 hash cracker", md5_crack).pack()
    button(window, "ZIP file Cracker", zip_crack).pack()
    button(window, "Gmail Password Cracker", gmail_crack).pack()
    button(window, "HTTP brute force", http_crack).pack()
    button(window, "Exit", window.destroy).pack()
def ftp_atk():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("390x155")
    window.title("ftp_atk")
    title_lbl = Label(window,
                      text='ftp attack',\
                      bg='#0f4b6e', fg='white').pack()
    url_lbl = Label(window, text='Enter The Target URL : ', bg='#0f4b6e', fg='white', font=font.Font(size=12)).pack()
    url_tf = Entry(window, width=40)
    uname_lbl = Label(window, text='Enter The Username : ', bg='#0f4b6e', fg='white', font=font.Font(size=12))
    uname_tf = Entry(window, width=40)
    ok_btn = Button(window, text='  OK  ', bg='#0f4b6e', fg='white', font=font.Font(size=12),
                    command=lambda: rl.ftp_atk(url_tf.get(), uname_tf.get()))
    url_tf.pack()
    uname_lbl.pack()
    uname_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn = button(window, 'cancel', window.destroy).pack(side="right")
def md5_crack():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("550x155")
    window.title("md5_crack")
    title_lbl = Label(window,
                      text='------------------------------------CRACK MD5 HASH------------------------------------', \
                      bg='#0f4b6e', fg='white').pack()
    url_lbl = Label(window, text='Enter md5 hash: (ex: 320157b0a9d971845c5b0a0796058c79)', bg='#0f4b6e', fg='white', font=font.Font(size=12)).pack()
    url_tf = Entry(window, width=70)
    ok_btn = Button(window, text='  OK  ', bg='#0f4b6e', fg='white', font=font.Font(size=12),
                    command=lambda: rl.md5_crack(url_tf.get()))
    url_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn = button(window, 'cancel', window.destroy).pack(side="right")
def zip_crack():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("550x155")
    window.title("zip_crack")
    url_lbl = Label(window, text='Enter the zip file name (Must be in the same directory of the program): ', bg='#0f4b6e', fg='white',
                    font=font.Font(size=12)).pack()
    url_tf = Entry(window, width=50)
    ok_btn = Button(window, text='  OK  ', bg='#0f4b6e', fg='white', font=font.Font(size=12),
                    command=lambda: rl.zip_crack(url_tf.get()))
    url_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn = button(window, 'cancel', window.destroy).pack(side="right")
def gmail_crack():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("400x155")
    window.title("gmail_crack")
    url_lbl = Label(window, text='Enter The Target Gmail Address => ', bg='#0f4b6e', fg='white', font=font.Font(size=12)).pack()
    url_tf = Entry(window, width=40)
    uname_lbl = Label(window, text='Enter "0" to use the inbuilt passwords \nlist or enter the file path', bg='#0f4b6e', fg='white', font=font.Font(size=12))
    uname_tf = Entry(window, width=40)
    ok_btn = Button(window, text='  OK  ', bg='#0f4b6e', fg='white', font=font.Font(size=12),
                    command=lambda: rl.gmail_crack(url_tf.get(), uname_tf.get()))
    url_tf.pack()
    uname_lbl.pack()
    uname_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn = button(window, 'cancel', window.destroy).pack(side="right")
def http_crack():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("390x155")
    window.title("http_crack")
    title_lbl = Label(window,
                      text='NOTE: this method might not work on all login pages!', \
                      bg='#0f4b6e', fg='white').pack()
    url_lbl = Label(window, text='Enter the login page url: ', bg='#0f4b6e', fg='white', font=font.Font(size=12)).pack()
    url_tf = Entry(window, width=40)
    uname_lbl = Label(window, text='Enter the username:  ', bg='#0f4b6e', fg='white', font=font.Font(size=12))
    uname_tf = Entry(window, width=40)
    ok_btn = Button(window, text='  OK  ', bg='#0f4b6e', fg='white', font=font.Font(size=12),
                    command=lambda: rl.http_crack(url_tf.get(), uname_tf.get()))
    url_tf.pack()
    uname_lbl.pack()
    uname_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn = button(window, 'cancel', window.destroy).pack(side="right")
#---------------------------end password attacks---------------------------
#---------------------------start web hack---------------------------
def web_hack():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("600x350")
    window.title("network and wireless attacks")
    Label(window, bg='#0f4b6e', \
          font=font.Font(size=14), fg="white", \
          text="--------------------Web Attacks--------------------").pack()
    button(window, "Error-Based SQL Injection", sql_injection).pack()
    button(window, "Cross Site Scripting", scan_xss).pack()
    button(window, "Testing insecure web server configurations", t_ISC).pack()
    button(window, "DoS Attack", brute_web).pack()
    button(window, "Fuxploider (File upload vulnerability scanner and exploitation)", fux_scan).pack()
    button(window, "Exit", window.destroy).pack()
def sql_injection():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("390x155")
    window.title("sql_injection")
    url_lbl = Label(window, text='Enter the target url: ',
                    bg='#0f4b6e', fg='white',
                    font=font.Font(size=12)).pack()
    url_tf = Entry(window, width=40)
    ok_btn = Button(window, text='  OK  ', bg='#0f4b6e', fg='white', font=font.Font(size=12),
                    command=lambda: rl.sql_injection(url_tf.get()))
    url_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn = button(window, 'cancel', window.destroy).pack(side="right")
def scan_xss():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("390x155")
    window.title("scan_xss")
    url_lbl = Label(window, text='Enter the target url: ',
                    bg='#0f4b6e', fg='white',
                    font=font.Font(size=12)).pack()
    url_tf = Entry(window, width=40)
    ok_btn = Button(window, text='  OK  ', bg='#0f4b6e', fg='white', font=font.Font(size=12),
                    command=lambda: rl.scan_xss(url_tf.get()))
    url_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn = button(window, 'cancel', window.destroy).pack(side="right")
def t_ISC():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("390x155")
    window.title("test_ISC")
    url_lbl = Label(window, text='Enter the target website: ',
                    bg='#0f4b6e', fg='white',
                    font=font.Font(size=12)).pack()
    url_tf = Entry(window, width=40)
    ok_btn = Button(window, text='  OK  ', bg='#0f4b6e', fg='white', font=font.Font(size=12),
                    command=lambda: rl.test_ISC(url_tf.get()))
    url_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn = button(window, 'cancel', window.destroy).pack(side="right")
def brute_web():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("390x200")
    window.title("ftp_atk")
    title_lbl = Label(window,
                      text='ftp attack', \
                      bg='#0f4b6e', fg='white').pack()
    packets_lbl = Label(window, text='How many packets do you want to send : ', bg='#0f4b6e', fg='white', font=font.Font(size=12)).pack()
    packets_tf = Entry(window, width=40)
    dst_ip_lbl = Label(window, text='Enter The target IP : ', bg='#0f4b6e', fg='white', font=font.Font(size=12))
    dst_ip_tf = Entry(window, width=40)

    dst_port_lbl = Label(window, text='Enter The target PORT : ', bg='#0f4b6e', fg='white', font=font.Font(size=12))
    dst_port_tf = Entry(window, width=40)

    ok_btn = Button(window, text='  OK  ', bg='#0f4b6e', fg='white', font=font.Font(size=12),
                    command=lambda: rl.brute_web(packets_tf.get(), dst_ip_tf.get(), dst_port_tf.get()))
    packets_tf.pack()
    dst_ip_lbl.pack()
    dst_ip_tf.pack()
    dst_port_lbl.pack()
    dst_port_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn = button(window, 'cancel', window.destroy).pack(side="right")
def fux_scan():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("390x155")
    window.title("test_ISC")
    url_lbl = Label(window, text='Enter the target website: ',
                    bg='#0f4b6e', fg='white',
                    font=font.Font(size=12)).pack()
    url_tf = Entry(window, width=40)
    ok_btn = Button(window, text='  OK  ', bg='#0f4b6e', fg='white', font=font.Font(size=12),
                    command=lambda: rl.fux_scan(url_tf.get()))
    url_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn = button(window, 'cancel', window.destroy).pack(side="right")

#-----------------------------------start network and wireless attacks------------------
def net_wire():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("300x300")
    window.title("network and wireless attacks")
    Label(window, bg='#0f4b6e', \
          font=font.Font(size=14), fg="white", \
          text="---------------Network and Wireless Attacks - --------------").pack()
    button(window, "DHCP Starvation", dhcp_strv).pack()
    button(window, "Fake Access Point", fake_access).pack()
    button(window, " WiFi Scanner", wifi_scan).pack()
    button(window, "MAC address flooding", mac_flood).pack()
    button(window, "BruteX", brutex).pack()
    button(window, "Exit", window.destroy).pack()
def dhcp_strv():
    rl.dhcp_strv()
def fake_access():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.title("fake access")
    Label(window, bg='#0f4b6e', \
          font=font.Font(size=14), fg="white", \
          text="NOTE: MONITOR MODE MUST BE ENABLED TO PERFORM THIS ATTACK\nYOU MUST HAVE A NIC THAT SUPPORTS MONITOR INJECTION").pack()
    point_lbl = Label(window, text='Enter the fake Access Point name: ', bg='#0f4b6e', fg='white').pack()
    point_tf = Entry(window, width=40)
    ok_btn = Button(window, text='  OK  ', bg='#0f4b6e', fg="white", font=font.Font(size=12), pady=5,
                    command=lambda: rl.fake_access(point_tf.get()))
    point_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn = button(window, 'cancel', window.destroy).pack(side="right")
def wifi_scan():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.title("wifi scan")
    Label(window, bg='#0f4b6e', \
          font=font.Font(size=14), fg="white", \
          text="---------This Script discovers all the local hosts in the network---------").pack()
    Label(window, bg='#0f4b6e', \
          font=font.Font(size=14), fg="white", \
          text="Please Enter the IP Address range you want to discover (ex 192.168.1.0/24): ").pack()
    ip_tf = Entry(window, width=40)
    ok_btn = Button(window, text='  OK  ', bg='#0f4b6e', fg="white", font=font.Font(size=12), pady=5,
                    command=lambda: rl.wifi_scan(ip_tf.get()))
    ip_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn = button(window, 'cancel', window.destroy).pack(side="right")
def mac_flood():
    window=Tk()
    window.config(bg="#0f4b6e")
    Label(window, bg='#0f4b6e', \
          font=font.Font(size=14), fg="white", \
          text="Flooding the switch interface with a large number of packets").pack()
    rl.mac_flood()
def brutex():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("390x155")
    window.title("brutex")
    url_lbl = Label(window, text='Enter the url: ', bg='#0f4b6e', fg='white', font=font.Font(size=12)).pack()
    url_tf = Entry(window, width=40)
    port_lbl = Label(window, text='enter the port number: ', bg='#0f4b6e', fg='white', font=font.Font(size=12))
    port_tf = Entry(window, width=40)
    ok_btn = Button(window, text='  OK  ', bg='#0f4b6e', fg='white', font=font.Font(size=12),
                    command=lambda: rl.brutex(url_tf.get(), port_tf.get()))
    url_tf.pack()
    port_lbl.pack()
    port_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn = button(window, 'cancel', window.destroy).pack(side="right")
#-----------------------------------end network and wireless attacks------------------
#-----------------------------------start post exploitation---------------------------
def post_Exp():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("400x320")
    window.title("exploitation tools")
    Label(window, text='---------------Powerful Exploitation Tools---------------',font=font.Font(size=12) ,bg='#0f4b6e', fg='white').pack()
    button(window,"commix",commix).pack()
    button(window, "corsy", corsy).pack()
    button(window, "FDsploit", fdsploit).pack()
    button(window, "sqlmap", sqlmap).pack()
    button(window, "HostPanic", hostpanic).pack()
    button(window, "exit", window.destroy).pack()
def commix():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("400x120")
    window.title("commix")
    title_lbl = Label(window,
                      text='Commix is an open source penetration testing tool\n'+\
                      "automates the detection and exploitation of command injection vulnerabilities.\n", \
                      bg='#0f4b6e', fg='white').pack()
    rl.commix()
def corsy():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("400x120")
    window.title("corsy")
    title_lbl = Label(window,
                      text='Corsy scans for all known misconfigurations in CORS implementations.', \
                      bg='#0f4b6e', fg='white').pack()
    Label(window, text='Enter the url you want to test: ', bg='#0f4b6e', fg='white', font=font.Font(size=12)).pack()
    target_tf = Entry(window, width=40)
    ok_btn = Button(window, text='  OK  ', bg='#0f4b6e', fg='white', font=font.Font(size=12),
                    command=lambda: rl.corsy(target_tf.get()))
    target_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn = button(window, 'cancel', window.destroy).pack(side="right")
def fdsploit():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("400x120")
    window.title("FD sploit")
    title_lbl = Label(window,
                      text='fdsploit is a File Inclusion & Directory Traversal fuzzing,\nenumeration & exploitation tool.',\
                      bg='#0f4b6e', fg='white').pack()

    rl.fdsploit()
def sqlmap():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("400x120")
    window.title("sql map")
    title_lbl = Label(window,
                      text='sqlmap is used for detecting and exploiting SQL injection flaws\nand taking over of database servers.\n'+\
                      "It is one of the most powerful tools for SQLI attacks",
                      bg='#0f4b6e', fg='white').pack()
    rl.sqlmap()
def hostpanic():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("400x120")
    window.title("hostpanic")
    title_lbl = Label(window,
                      text='Find host header injections and perform Host Header attacks\nwith other kind of bugs like web cache poison', \
                      bg='#0f4b6e', fg='white').pack()
    Label(window, text='Enter the target url :', bg='#0f4b6e', fg='white', font=font.Font(size=12)).pack()
    target_tf = Entry(window, width=40)
    ok_btn = Button(window, text='  OK  ', bg='#0f4b6e', fg='white', font=font.Font(size=12),
                    command=lambda: rl.hostpanic(target_tf.get()))
    target_tf.pack()
    ok_btn.pack(side="left")
    cancel_btn = button(window, 'cancel', window.destroy).pack(side="right")
#------------------------------------end post exploitation-------------------------------
def real_attack():
    window_real = Tk()
    window_real.config(bg="#0f4b6e")
    window_real.geometry("300x300")
    window_real.title("real attack data")
    button(window_real,"Information gathering",info_gath).pack()
    button(window_real,"Password Attacks",pw_attack).pack()
    button(window_real,"web hacking",web_hack).pack()
    button(window_real, "Network & Wireless Testing",net_wire).pack()
    button(window_real,"Exploitation Tools",post_Exp).pack()
    button(window_real,"Exit",window_real.destroy).pack()

window_main.geometry("500x300")
window_main.config(bg='#0f4b6e')
lbl = Label(window_main,bg='#0f4b6e',\
            font=font.Font(size=12),fg="white",\
            text="An Automation Penetration Testing tool from El Shorouk Academy Team.\nUsed for legal purposes only!\n\n").pack()

btn_logical = button(window_main,'Logical Attack!',logical_attack)
btn_real = button(window_main,'Real Attack !',real_attack)
btn_exit = button(window_main,'!0 exit 0!',window_main.quit)
f=font.Font(size=16)
btn_exit["font"]=btn_real["font"]=btn_logical["font"]=f
btn_exit.pack(side='bottom',pady=10,padx=10)
btn_real.pack(side='left',pady=10,padx=10)
btn_logical.pack(side='right',pady=10,padx=10)
window_main.mainloop()
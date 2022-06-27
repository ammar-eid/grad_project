import tkinter.font as font
from tkinter import *
import my_way as model
import real_attack as rl
window_main = Tk()
button=lambda x,y,z:Button(x,text=y,command=z,bg='#0f4b6e',fg="white",font=font.Font(size=12),pady=5)

def logical_attack():
    window_main.destroy()
    model.start()
    window_logical = Tk()
    window_logical.title("logical attack data")
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

def pw_attack():
          window_pw_attack=Tk()
def web_hack():
        window_exp_tools=Tk()
#-----------------------------------start network and wireless attacks------------------
def net_wire():
    window = Tk()
    window.config(bg="#0f4b6e")
    window.geometry("300x400")
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
    window.title("exploitation tools")
    Label(window, text='---------------Powerful Exploitation Tools---------------',font=font.Font(size=12) ,bg='#0f4b6e', fg='white').pack()
    button(window,"commix",commix).pack(side="left")
    button(window, "corsy", corsy).pack(side="left")
    button(window, "FDsploit", fdsploit).pack(side="left")
    button(window, "sqlmap", sqlmap).pack(side="left")
    button(window, "HostPanic", hostpanic).pack(side="left")
    button(window, "exit", window.destroy).pack(side="left")
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
    window_real.geometry("300x400")
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

from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#0f4b6e')
clicked = StringVar()


def scan_wp():

    window=Tk()
    window.geometry("400x100")
    hot_name_lbl = Label(window, text='select a word scan target', bg='#0f4b6e', fg='white').pack()
    host_name_tf=Entry(window,width=40).pack()
    ok_btn=Button(window,text='OK',relief=SOLID).pack()
    cancel_btn=Button(window,text='cancel',relief=SOLID).pack()

btn = Button(ws,text='Frame Sentence',relief=SOLID,command=nmap)
btn.pack(pady=10)
ws.mainloop()

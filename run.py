from tkinter import *
from tkinter import ttk
from dark_title_bar import *
import sv_ttk
import os

w = Tk()
w.title('Run')
w.geometry('400x150')
w.iconbitmap('C:/UserFiles/AR/Code/Apps/Applets/winRun/icon.ico')
w.resizable(False,False)
w.configure(bg='#1c1c1c')
dark_title_bar(w)

def run():
    os.system(e.get())
    if():
        os.system(e.get())
    else:
        l.configure(text='Specify PATH', foreground='red')
    

e = Entry(w, bg='#242424', foreground='white')
e.pack(pady=10)
l = Label(w,text='', bg='#1c1c1c', foreground='white')
l.pack()
btn = Button(text='Run', command= run, bg='#242424', foreground='white')
btn.pack(pady=10)

w.mainloop()
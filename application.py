from tkinter import *
from tkinter import ttk
import sv_ttk
import os

w = Tk()
w.title('Run')
w.geometry('400x150')
sv_ttk.set_theme("light")
w.iconbitmap('icon.ico')
w.resizable(False,False)

def run():
    os.system(e.get())

e = ttk.Entry(w)
e.pack(pady=10)
btn = ttk.Button(text='Run', command= run)
btn.pack(pady=10)

w.mainloop()
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from customtkinter import *
import os

w = ctk.CTk()
w.title("")
w.geometry('400x150')
w.iconbitmap('icon.ico')
w.resizable(False, False)
ctk.set_appearance_mode("System")

def run():
    os.system(e.get())
    if():
        os.system(e.get())
    else:
        l.configure(text='Specify PATH', text_color='red')
    

e = CTkEntry(w, placeholder_text="Enter program:")
e.pack(pady=20)
l = CTkLabel(w,text=None)
l.pack()
btn = CTkButton(w, text='Run', command= run)
btn.pack(pady=6)

w.mainloop()
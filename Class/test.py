from tkinter import *
from tkinter import ttk
import tkinter as tk

class o():
    def __init__(self):
        self.root = Tk()
    
        
        self.Button=Button(self.root,command=lambda:p(),text='hello')
        self.Button.place(x=3,y=3)
        self.Button2=Button(self.root,command=self.hello,text='o')
        self.Button2.place(x=10,y=30)
        global v
        v="h"
        self.root.mainloop()
    def hello(self):
        print(v)

def p():
    print(v)   
o()


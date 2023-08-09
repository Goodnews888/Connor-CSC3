from tkinter import *
from tkinter import ttk
import tkinter as tk

class o():
    def __init__(self):
        self.root = Tk()
        score = 0
        self.o=Label(text=score)
        self.o.place(x=3,y=3)
        score1 = 3
        self.o.config(text=score1)
        self.root.mainloop()
   
o()

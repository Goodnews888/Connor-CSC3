from tkinter import *
from tkinter import ttk
from PIL import Image
import tkinter as tk
import customtkinter

class o():
    def __init__(self):
        self.root = customtkinter.CTk()

        cutlet = customtkinter.CTkImage(Image.open("AS91906\image\logo1.png"), size=(275, 200))
        cutlet_imgbtn = customtkinter.CTkButton(self.root, image=cutlet, text="",         # Puts the image in a button
                                            fg_color='transparent', hover_color="#333333")          # Configuration to button background
        cutlet_imgbtn.grid(row=0, column=0, sticky="news", pady=(15,10), padx=10) 
        
        self.root.mainloop()
   
o()

a = open("database.txt","r")
print(a.read())
a.close()

a = open("database.txt","w")
a.write("12")
a.close()
a = open("database.txt","r+")
print(a.read())
a.close()
#Importing tkinter to allow for GUI
from tkinter import *

from tkinter import ttk

from PIL import Image, ImageTk
#Importing messagebox to allow for error messages if there is wrong input by the user
from tkinter import messagebox

#Importing random to allow for random generation of receipt number.
import random
import os





class MyGUI():
    def help(self):
        print("")
    def start(self):
        print("")
    def __init__(self):
        # Giving attributes to window
        self.window = Tk()
        self.window.title("Spelling Game")
        self.window.configure(width = 1000, height = 600)
        self.window.configure(bg='white')

        # move window center
        self.winWidth = self.window.winfo_reqwidth()
        self.winwHeight = self.window.winfo_reqheight()
        self.posRight = int(self.window.winfo_screenwidth() / 2 - self.winWidth / 2)
        self.posDown = int(self.window.winfo_screenheight() / 2 - self.winwHeight / 1.75)
        self.window.geometry("+{}+{}".format(self.posRight, self.posDown))

        #GUI of titles, buttons, labels
        self.title = Label(self.window, text="A Vocabulary \nGame", bg = 'white' ,font=('Aerial',30,'bold')).place(x=368, y= 250)
        self.quit = Button(self.window, padx = 14,text="Quit",command=quit, font=('Aerial',14,'bold')).place(x=900, y =15)
        self.start = Button(self.window, padx = 20, text = "Start \n(Space)", justify = LEFT, command=self.start,font=("Aerial", 15,"bold")).place(x=338, y=450)
        self.help = Button(self.window, padx =35, pady =13, text = "Help",command=self.help,font=("Aerial", 15,"bold")).place(x=538, y=450)

        #Setting up frames for parent self.window
        self.frame1 = Frame(self.window, bg='white', highlightbackground="black", highlightthickness=1, width = 250, height = 120)
        self.frame2 = Frame(self.window, bg='white', highlightbackground="black", highlightthickness=1,width = 250, height = 170)
        self.frame3 = Frame(self.window, bg='white', highlightbackground="black", highlightthickness=1,width = 250, height = 120)
        self.frame4 = Frame(self.window, bg='white', highlightbackground="black", highlightthickness=1,width = 250, height = 170)
        self.frame1.place(x=20, y=75)
        self.frame2.place(x=20, y=410)
        self.frame3.place(x=730, y=75)
        self.frame4.place(x=730, y=410)
        

        frame2_label = Label(self.frame2, text="Difficulty:", font=("Aerial", 18,"bold"))
        frame2_label.place(x=10, y=10)

        self.r1_v = IntVar()
        self.r1_v.set(1)
        

        self.easyb = Radiobutton(self.frame2, width=7, anchor=W, text="Easy", command=self.difficulty,variable=self.r1_v, value=1, font=("Aerial", 12,"bold"))
        self.easyb.place(x=50, y=55)
        self.mediumb = Radiobutton(self.frame2, width=7, anchor=W,text="Medium",command=self.difficulty,variable=self.r1_v, value=2,font=("Aerial", 12,"bold"))
        self.mediumb.place(x=50, y=85)
        self.hardb = Radiobutton(self.frame2, width=7, anchor=W,text="Hard",command=self.difficulty,variable=self.r1_v, value=3,font=("Aerial", 12,"bold"))
        self.hardb.place(x=50, y=115)
        image=Image.open("AS91906\image\logo1.png")

        self.difficulty()


        # Resize the logo in the given (width, height)
        img=image.resize((90, 100))

        # Conver the logo in TkImage
        my_img=ImageTk.PhotoImage(img)

        # Display the logo with label
        label=Label(self.window, image=my_img, bg='white')
        label.place(x=455, y=60)
        
        
       
        
        self.window.resizable(False, False)
        self.window.mainloop()
    def difficulty(self):
        if self.r1_v.get()==1:
            print('hf')
            self.easyb.config(bg='green')
            self.mediumb.config(bg='white')
            self.hardb.config(bg='white')
        if self.r1_v.get()==2:
            self.easyb.config(bg='white')
            self.mediumb.config(bg='orange')
            self.hardb.config(bg='white')
        if self.r1_v.get()==3:
            self.easyb.config(bg='white')
            self.mediumb.config(bg='white')
            self.hardb.config(bg='red')


        

        
            

    


MyGUI()









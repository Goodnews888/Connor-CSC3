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
        while self.rootcount <= 1:
            self.help = Toplevel()
            self.help.resizable(False, False)
            self.help.configure(width=500, height = 600)
            self.helpWidth = self.help.winfo_reqwidth()
            self.helpHeight = self.help.winfo_reqheight()
            self.posRight = int(self.help.winfo_screenwidth() / 2 - self.helpWidth / 2)
            self.posDown = int(self.help.winfo_screenheight() / 2 - self.helpHeight / 1.75)
            self.help.geometry("+{}+{}".format(self.posRight, self.posDown))
            self.rootcount += 1
            self.help.protocol("WM_DELETE_WINDOW", self.result_close)

            #Initializing Labels
            framehelp = Text(self.help, wrap="word", highlightbackground="black", highlightthickness=1, width =59,height =33.4)
            framehelp.insert("1.0","In this game, you will be given a letter. You will then have to enter in a word that starts with the given letter. All words that you enter have to be proper words from the official dictionary. After you've entered in a correct word, you will be granted one point, which is added to your score. A new letter will be given, where you will have to again enter in a word that starts with the new given letter. This process is repeated again and again until your time runs out for the round. The goal of the game is to enter in as many words as you can in the timeframe.\n\nIf you do not like your given letter, you have the option to get a new letter via the skip button.\n\nHowever! There is a catch. You cannot enter in the same repeated word. You can't enter in the word 'ant' twice. This rule only applies for the round that you play. So you may enter in the same word, but only in different rounds you play. Another catch are the difficulties. The default difficulty is easy mode. Difficulties determine the minimum letter count of words you enter. For example in easy difficulty. the minimum letter count in words entered is 1... You'd be required to enter in words that have a minimum count of 1 letter. In medium, the minimum letter count is 3. In hard, the minimum letter count is 6.\n\nIf you enter in improper words, repeated words, or words that don't meet the minimum letter count requirement, the program will let you know by highlighting the rule you are breaking in red. It will highlight in red until you are no longer breaking that rule.")
            framehelp.config(state="disabled")
            framehelp.place(x=10, y=50)
            Label(self.help, text = "Instructions", font=('Aerial',20,'bold')).place(x=170, y=10)
            Button(self.help, text = " X ", command = self.result_close, font=('Aerial',10,'bold')).place(x=460, y=10)
            
    
    
        
    def result_close(self):
        self.rootcount = 1
        self.help.destroy()
    def start(self):
        pass
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
        

        frame2_label = Label(self.frame2, text="Difficulty:", bg ='white',font=("Aerial", 18,"bold"))
        frame2_label.place(x=10, y=10)

        frame4_label = Label(self.frame4, bg ='white',text="Difficulty:", font=("Aerial", 18,"bold"))
        frame4_label.place(x=10, y=10)

        self.diffic = Label(self.frame4, bg ='green', text ="Easy",  font=("Aerial", 18,"bold"))
        self.diffic.place(x=125, y=10)
    
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
        
        self.rootcount = 1
        


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
            self.easyb.config(bg='green')
            self.mediumb.config(bg='white')
            self.hardb.config(bg='white')
            self.diffic.configure(bg ='green', text ="Easy",  font=("Aerial", 18,"bold"))

        if self.r1_v.get()==2:
            self.easyb.config(bg='white')
            self.mediumb.config(bg='orange')
            self.hardb.config(bg='white')
            self.diffic.configure(bg ='orange', text ="Medium",  font=("Aerial", 18,"bold"))
            
        if self.r1_v.get()==3:
            self.easyb.config(bg='white')
            self.mediumb.config(bg='white')
            self.hardb.config(bg='red')
            self.diffic.configure(bg ='red', text ="Hard",  font=("Aerial", 18,"bold"))
    

        


MyGUI()









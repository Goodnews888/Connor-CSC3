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
        self.frame1 = Frame(self.window, width = 250, height = 200)
        self.frame2 = Frame(self.window, width = 250, height = 200)
        self.frame3 = Frame(self.window, width = 250, height = 200)
        self.frame4 = Frame(self.window, width = 250, height = 200)
        self.frame1.place(x=20, y=100)
        self.frame2.place(x=20, y=450)
        self.frame3.place(x=730, y=100)
        self.frame4.place(x=730, y=450)




        r1_v = IntVar()
        r1_v.set(1)

        '''easyb = ttk.Radiobutton(self.frame2, text="Easy", variable=r1_v, value=1)
        easyb.place(x=50, y=450)
        mediumb = ttk.Radiobutton(self.fram2, text="Medium", variable=r1_v, value=2)
        mediumb.place(x=50, y=470)
        hardb = ttk.Radiobutton(self.frame2, text="Hard", variable=r1_v, value=3)
        hardb.place(x=50, y=490)'''
        image=Image.open("AS91906\image\logo1.png")

        # Resize the logo in the given (width, height)
        img=image.resize((90, 100))

        # Conver the logo in TkImage
        my_img=ImageTk.PhotoImage(img)

        # Display the logo with label
        label=Label(self.window, image=my_img)
        label.place(x=455, y=60)
        
        
       
        
        #self.window.resizable(False, False)
        self.window.mainloop()
    def easy(self):
        print('')
    def medium(self):
        print('')

    


MyGUI()









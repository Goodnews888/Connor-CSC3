#Importing tkinter to allow for GUI
from tkinter import *
from tkinter import ttk

#Importing messagebox to allow for error messages if there is wrong input by the user
from tkinter import messagebox

#Importing random to allow for random generation of receipt number.
import random





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
        self.title = Label(self.window, text="A Vocabulary \nGame", bg = 'white' ,font=('Aerial',30,'bold')).place(x=380, y= 250)
        self.quit = Button(self.window, padx = 14,text="Quit",command=quit, font=('Aerial',14,'bold')).place(x=900, y =15)
        self.start = Button(self.window, padx = 20, text = "Start \n(Space)", justify = LEFT, command=self.start,font=("Aerial", 15,"bold")).place(x=350, y=450)
        self.help = Button(self.window, padx =35, pady =13, text = "Help",command=self.help,font=("Aerial", 15,"bold")).place(x=550, y=450)

    


        
        #self.window.resizable(False, False)
        self.window.mainloop()
    


MyGUI()









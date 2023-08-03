#Importing tkinter to allow for GUI
from tkinter import *
import tkinter as tk

import time
import threading
from PIL import Image, ImageTk
#Importing messagebox to allow for error messages if there is wrong input by the user






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
            framehelp.insert("1.0","In this game, you will be given a letter. You will then have to enter in a word that starts with the given letter. All words that you enter have to be proper words from the official dictionary. After you've entered in a correct word, you will be granted one point, which is added to your score. A new letter will be given, where you will have to again enter in a word that starts with the new given letter. This process is repeated again and again until your time runs out for the round. The goal of the game is to enter in as many words as you can in the timeframe.\n\nIf you do not like your given letter, you have the option to get a new letter via the skip button.\n\nHowever! There is a catch. You cannot enter in the same repeated word. You can't enter in the word 'ant' twice. This rule only applies for the round that you play. So you may enter in the same word, but only in different rounds you play. Another catch are the difficulties. The default difficulty is easy mode. Difficulties determine the minimum letter count of words you enter. For example in easy difficulty. the minimum letter count for words entered is 1... You'd be required to enter in words that have a minimum count of 1 letter. In medium, the minimum letter count is 3. In hard, the minimum letter count is 6.\n\nIf you enter in improper words, repeated words, or words that don't meet the minimum letter count requirement, the program will let you know by highlighting the rule you are breaking in red. It will highlight in red until you are no longer breaking that rule.")
            framehelp.config(state="disabled")
            framehelp.place(x=10, y=50)
            Label(self.help, text = "Instructions", font=('Aerial',20,'bold')).place(x=170, y=10)
            Button(self.help, text = " X ", command = self.result_close, font=('Aerial',10,'bold')).place(x=460, y=10)
            
    
    
        
    def result_close(self):
        self.rootcount = 1
        self.help.destroy()
    def gameclose(self):
        self.window.deiconify()
        self.game.destroy()
    def count_down(self):
        counting=True
        second = 60
        self.game.after(61000,self.gameclose)
        while second >-1 and counting:
            if second >=0:
                if second > 9:
                    self.second_var.set(f'{second}')
                    second-=1
                    self.game.update()
                    time.sleep(1)
                else:
                    self.second_var.set(f' 0{second}')
                    self.game.update()
                    time.sleep(1)
            if 'normal' == self.window.state():
                break
            
    def start(self):
        #Giving attributes to game window
        self.game = Toplevel()
        self.game.resizable(False, False)
        self.game.title("Spelling Game")
        self.game.configure(width = 1000, height = 600)
        self.game.configure(bg='white')

        #move game window to center
        self.gameWidth = self.game.winfo_reqwidth()
        self.gameHeight = self.game.winfo_reqheight()
        self.posRight = int(self.game.winfo_screenwidth() / 2 - self.gameWidth / 2)
        self.posDown = int(self.game.winfo_screenheight() / 2 - self.gameHeight / 1.75)
        self.game.geometry("+{}+{}".format(self.posRight, self.posDown))

        #When game window is opened, main window is hidden.
        self.window.withdraw()

        #When game window is closed, main window is shown
        self.game.protocol("WM_DELETE_WINDOW", self.gameclose)

        self.game_frame1=Frame(self.game, bg='white', highlightbackground="black", highlightthickness=1, width = 980, height = 210)
        self.game_frame1.place(x=10,y=10)
        self.game_frame2=Frame(self.game, bg='white', highlightbackground="black", highlightthickness=1, width = 270, height = 150)
        self.game_frame2.place(x=720,y=230)
        


        #Constructing labels inside game_frame1
        gameTitle = Label(self.game_frame1, bg='white',text="A Vocabulary\nGame",font=("Aerial", 30,"bold"))
        gameTitle.place(x=360, y=60)

        self.gamequit = Button(self.game_frame1, text="Quit",padx = 14,command=self.gameclose, font=('Aerial',14,'bold'))
        self.gamequit.place(x=887,y=10)



        # Display the logo with label
        time_image=Label(self.game_frame1, image=self.my_time, bg='white')
        time_image.place(x=120, y=30)
        score_image=Label(self.game_frame1,  image=self.my_score, bg='white')
        score_image.place(x=730, y= 30)
        square_image=Label(self.game, image=self.my_square, bg='white')
        square_image.place(x=450, y=320)

        time_remain=Label(self.game_frame1, text ="Time Remaining:", bg='white',font=('Aerial',18,'bold'))
        time_remain.place(x=50, y=140)

        score_label=Label(self.game_frame1, text ="Score:", bg='white',font=('Aerial',18,'bold'))
        score_label.place(x=700,y=140)
        


        


        #Constructing labels inside the difficulty information frame (game_frame2)
        Label(self.game_frame2, text="Difficulty:", bg ='white',font=("Aerial", 18,"bold")).place(x=10, y=12)

        diffLabel=Label(self.game_frame2,text=self.game_diff,bg='white',font=("Aerial", 18))
        diffLabel.place(x=125, y=15)

        rule1 = Label(self.game_frame2, bg ='white',text="• Minimum letter count:", font=("Aerial", 14))
        rule1.place(x=25,y=50)
        rule2 = Label(self.game_frame2, bg ='white',text="• No repeated words", font=("Aerial", 14))
        rule2.place(x=25, y=80)
        rule3 = Label(self.game_frame2, bg ='white',text="• Valid words only", font=("Aerial", 14))
        rule3.place(x=25, y=110)


        diffminletter = self.diffminletter["text"]
        game_diffminletter = Label(self.game_frame2, bg='white', text=diffminletter, font=("Aerial", 14))
        game_diffminletter.place(x=220, y=50)

        type_label = Label(self.game,bg='white',justify =LEFT,text='Type a word starting\nwith the letter...',font=("Aerial", 19,"bold"))
        type_label.place(x=380,y=250)



        letter_Entry = tk.Entry(self.game, width=44, highlightbackground="black", highlightthickness=2,justify = CENTER,font=("Aerial", 29))
        letter_Entry.place(x=14,y=450)

        Skip = Button(self.game, padx = 50, text = "Skip (Esc)",command=self.skip,font=("Aerial", 15,"bold"))
        Skip.place(x=150, y=530)

        Submit = Button(self.game, padx=30, text = "Submit (Enter)", command=self.submit,font=("Aerial", 15,"bold"))
        Submit.place(x=625,y=530)

        self.second_var = tk.StringVar(value= '00')
        self.second_lbl = tk.Label(self.game,bg='white',font=('Aerial',18,'bold'),textvariable=self.second_var)
        self.second_lbl.place(x=255, y=152)

        countdown_thread = threading.Thread(target=self.count_down)
        countdown_thread.start()


        
    

    def skip(self):
        print('')
    def submit(self):
        print('')

        

        
    


    def __init__(self):
        # Giving attributes to window
        self.window = Tk()
        self.window.title("Spelling Game")
        self.window.configure(width = 1000, height = 600)
        self.window.configure(bg='white')

        self.counting = False


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
        
        #Initializing Labels in the frames created above.
        Label(self.frame1, text = "Previous Score", bg='white',font=("Aerial", 18,"bold")).place(x=30, y=5)
        Label(self.frame2, text="Difficulty:", bg ='white',font=("Aerial", 18,"bold")).place(x=10, y=10)
        Label(self.frame3, text = "High Score", bg='white',font=("Aerial", 18,"bold")).place(x=60, y=5)
        Label(self.frame4, bg ='white',text="Difficulty:", font=("Aerial", 18,"bold")).place(x=10, y=10)
        rule1 = Label(self.frame4, bg ='white',text="• Minimum letter count:", font=("Aerial", 13))
        rule1.place(x=25,y=50)
        rule2 = Label(self.frame4, bg ='white',text="• No repeated words", font=("Aerial", 13))
        rule2.place(x=25, y=80)
        rule3 = Label(self.frame4, bg ='white',text="• Valid words only", font=("Aerial", 13))
        rule3.place(x=25, y=110)
        self.diffic = Label(self.frame4, bg ='green', text ="Easy",  font=("Aerial", 18,"bold"))
        self.diffic.place(x=125, y=10)
        self.diffminletter = Label(self.frame4, bg='green',text ="1", font=("Aerial", 13, "bold"))
        self.diffminletter.place(x=195,y=50)
    
        self.r1_v = IntVar()
        self.r1_v.set(1)
        
        #Initializing Radiobuttons in frame2, for the difficulty option changer.
        self.easyb = Radiobutton(self.frame2, width=7, anchor=W, text="Easy", command=self.difficulty,variable=self.r1_v, value=1, font=("Aerial", 12,"bold"))
        self.easyb.place(x=50, y=55)
        self.mediumb = Radiobutton(self.frame2, width=7, anchor=W,text="Medium",command=self.difficulty,variable=self.r1_v, value=2,font=("Aerial", 12,"bold"))
        self.mediumb.place(x=50, y=85)
        self.hardb = Radiobutton(self.frame2, width=7, anchor=W,text="Hard",command=self.difficulty,variable=self.r1_v, value=3,font=("Aerial", 12,"bold"))
        self.hardb.place(x=50, y=115)
        logo=Image.open("AS91906\image\logo1.png")

        self.difficulty()
        
        self.rootcount = 1
        


        # Resize the logo in the given (width, height)
        logo_size=logo.resize((90, 100))

        # Convert the logo in TkImage
        my_logo=ImageTk.PhotoImage(logo_size)

        
        # Display the logo with label
        label=Label(self.window, image=my_logo, bg='white')
        label.place(x=455, y=60)

        #Defining images for game window
        time=Image.open(r"AS91906\image\time.PNG")
        score=Image.open(r"AS91906\image\score.PNG")
        square=Image.open(r"AS91906\image\square.PNG")

        # Resize the logo in the given (width, height)
        time_size=time.resize((100, 100))
        score_size=score.resize((90, 100))
        square_size=square.resize((110, 110))

        # Convert the logo in TkImage
        self.my_time=ImageTk.PhotoImage(time_size)
        self.my_score=ImageTk.PhotoImage(score_size)
        self.my_square=ImageTk.PhotoImage(square_size)
        
        self.window.resizable(False, False)
        self.window.mainloop()

    def difficulty(self):
        if self.r1_v.get()==1:
            self.easyb.config(bg='green')
            self.mediumb.config(bg='white')
            self.hardb.config(bg='white')
            self.diffic.configure(bg ='green', text ="Easy",  font=("Aerial", 18,"bold"))
            self.diffminletter.configure(bg='green', text="1")

            #Game window
            self.game_diff = "Easy"

        if self.r1_v.get()==2:
            self.easyb.config(bg='white')
            self.mediumb.config(bg='orange')
            self.hardb.config(bg='white')
            self.diffic.configure(bg ='orange', text ="Medium",  font=("Aerial", 18,"bold"))
            self.diffminletter.configure(bg='orange', text="3")

            #Game window
            self.game_diff = "Medium"

        if self.r1_v.get()==3:
            self.easyb.config(bg='white')
            self.mediumb.config(bg='white')
            self.hardb.config(bg='red')
            self.diffic.configure(bg ='red', text ="Hard",  font=("Aerial", 18,"bold"))
            self.diffminletter.configure(bg='red', text="6")

            #Game window
            self.game_diff = "Hard"

    
MyGUI()
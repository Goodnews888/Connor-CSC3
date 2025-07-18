#Importing tkinter to allow for GUI
from tkinter import *
import tkinter as tk
from tkinter import ttk

#Importing Image, ImageTK from PIL to allow for resizing of images.
from PIL import Image, ImageTk

#Importing other modules
import random
import time
import threading
import os
import sys




#MyGUI is a class that contains all the functions necessary to run the game.
class MyGUI():

    
    
    def help(self):
        #This while loop limits the number of help windows to only one count.
        while self.rootcount <= 1:
            self.help = Toplevel()
            self.help.resizable(False, False)
            self.help.configure(width=500, height = 600)

            #Centering the help window
            self.helpWidth = self.help.winfo_reqwidth()
            self.helpHeight = self.help.winfo_reqheight()
            self.posRight = int(self.help.winfo_screenwidth() / 2 - self.helpWidth / 2)
            self.posDown = int(self.help.winfo_screenheight() / 2 - self.helpHeight / 1.75)
            self.help.geometry("+{}+{}".format(self.posRight, self.posDown))

            #Adding 1 the rootcount to prevent more help windows from being opened.
            self.rootcount += 1

            #Checks to see if help window is closed, if it is, rootcount is set back to 1, allowing the user to open
            #another help window.
            self.help.protocol("WM_DELETE_WINDOW", self.result_close)

            #Initializing Labels
            framehelp = Text(self.help, wrap="word", highlightbackground="black", highlightthickness=1, width =59,height =33.4)
            framehelp.insert("1.0","In this game, you will be given a letter. " 
                             "You will then have to enter in a word that starts with the given letter. " 
                             "All words that you enter have to be proper words from the official dictionary. " 
                             "After you've entered in a correct word, you will be granted one point, "
                             "which is added to your score. A new letter will be given, "
                             "where you will have to again enter in a word that starts with the new given letter. "
                             "This process is repeated again and again until your time runs out for the round. "
                             "The goal of the game is to enter in as many words as you can in the timeframe.\n\n"
                             "If you do not like your given letter, you have the option to get a new letter "
                             "via the skip button.\n\nHowever! There is a catch. You cannot enter in the same "
                             "repeated word. You can't enter in the word 'ant' twice. This rule only applies "
                             "for the round that you play. So you may enter in the same word, but only in different "
                             "rounds you play. Another catch are the difficulties. The default difficulty is easy mode. "
                             "Difficulties determine the minimum letter count of words you enter. "
                             "For example in easy difficulty. the minimum letter count for words entered is 1... "
                             "You'd be required to enter in words that have a minimum count of 1 letter. In medium, "
                             "the minimum letter count is 3. In hard, the minimum letter count is 6.\n\nIf you enter in "
                             "improper words, repeated words, or words that don't meet the minimum letter count "
                             "requirement, the program will let you know by highlighting the rule you are breaking in red. "
                             "It will highlight in red until you are no longer breaking that rule.")
            framehelp.config(state="disabled")
            framehelp.place(x=10, y=50)
            Label(self.help, text = "Instructions", font=('Aerial',20,'bold')).place(x=170, y=10)

            #Initializing quit button.
            Button(self.help, text = " X ", command = self.result_close, font=('Aerial',10,'bold')).place(x=460, y=10)
            

    def result_close(self):
        self.rootcount = 1
        self.help.destroy()
    def gameclose(self):
        #When the game window closes, this function runs. The purpose of this function
        #is to display the previous score of the user on the menu window and if any
        #the highscore of the user on the menu window.

        #If game difficulty was set to easy, it will update the previous score and highscore
        #accordingly for the easy difficulty.
        if self.r1_v.get()==1:
            self.easy_prevscore = self.scoreno
            self.prev_score.config(text=self.easy_prevscore)
            if self.easy_prevscore > self.easy_highscore:
                self.easy_highscore = self.easy_prevscore
                self.high_score.config(text=self.easy_highscore)
            else:
                self.high_score.config(text=self.easy_highscore)
        #If game difficulty was set to medium, it will update the previous score and highscore
        #accordingly for the medium difficulty.
        if self.r1_v.get()==2:
            self.medium_prevscore = self.scoreno
            self.prev_score.config(text=self.medium_prevscore)
            if self.medium_prevscore > self.medium_highscore:
                self.medium_highscore = self.medium_prevscore
                self.high_score.config(text=self.medium_highscore)
            else:
                self.high_score.config(text=self.medium_highscore)
        #If game difficulty was set to hard, it will update the previous score and highscore
        #accordingly for the hard difficulty.
        if self.r1_v.get()==3:
            self.hard_prevscore = self.scoreno
            self.prev_score.config(text=self.hard_prevscore)
            if self.hard_prevscore > self.hard_highscore:
                self.hard_highscore = self.hard_prevscore
                self.high_score.config(text=self.hard_highscore)
            else:
                self.high_score.config(text=self.hard_highscore)
        
        #Makes menu window visible again
        self.window.deiconify()

        #Destroys game window.
        self.game.destroy()
        


    def count_down(self):
        #This function runs when the game window is opened.
        #After the game runs for 62 seconds, the game window
        #is closed.


        counting=True
        #The second variable is used to display how much time is remaining in the game
        #via the second_lbl label located in def start_game(self).
        #The label starts of at 60 seconds, and then counts down every second until
        #the label reaches time 00.
        second = 60
        self.game.after(62000,self.gameclose)
        while second >-1 and counting:
            if second >=0:
                if second > 9:
                    self.second_var.set(f'{second}')
                    second-=1
                    self.game.update()
                    time.sleep(1)
                else:
                    self.second_var.set(f' 0{second}')
                    second-=1
                    self.game.update()
                    time.sleep(1)
            if 'normal' == self.window.state():
                break
    def load_image(self, filename):
        return Image.open(os.path.join(self.img_dir, filename))
    def load_text_file(self, filename):
        path = os.path.join(self.base_dir, filename)
        with open(path, 'r') as file:
            return file.read()
            
    def start_game(self):
        #Giving attributes to game window
        self.game = Toplevel()
        self.game.resizable(False, False)
        self.game.title("Spelling Game")
        self.game.configure(width = 1000, height = 600)
        self.game.configure(bg=self.bg_gamecolor)

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

        self.game_frame1=Frame(self.game, bg=self.framegamecolor, highlightbackground=self.bordergamecolor, highlightthickness=5, width = 980, height = 210)
        self.game_frame1.place(x=10,y=10)
        self.game_frame2=Frame(self.game, bg='white', highlightbackground=self.bordergamecolor, highlightthickness=5, width = 270, height = 150)
        self.game_frame2.place(x=720,y=230)
        


        #Constructing labels inside game_frame1
        gameTitle = Label(self.game_frame1, bg=self.framegamecolor,text="A Vocabulary\nGame",font=("Aerial", 30,"bold"))
        gameTitle.place(x=360, y=60)

        #Making quit button for game window
        self.gamequit = Button(self.game_frame1, text="Quit",padx = 14,command=self.gameclose, font=('Aerial',14,'bold'))
        self.gamequit.place(x=880,y=10)



        #Displaying image of clock using a label
        time_image=Label(self.game_frame1, image=self.my_time, bg=self.framegamecolor)
        time_image.place(x=120, y=30)
        #Displaying image of score using a label
        score_image=Label(self.game_frame1,  image=self.my_score, bg=self.framegamecolor)
        score_image.place(x=730, y= 30)
        #Displaying image of square for the background of the randomly generated letter.
        square_image=Label(self.game, image=self.my_square, bg=self.bg_gamecolor)
        square_image.place(x=443, y=320)

        #Time remaining label
        time_remain=Label(self.game_frame1, text ="Time Remaining:", bg=self.framegamecolor,font=('Aerial',18,'bold'))
        time_remain.place(x=50, y=140)

        #Score label
        score_label=Label(self.game_frame1, text ="Score:", bg=self.framegamecolor,font=('Aerial',18,'bold'))
        score_label.place(x=700,y=140)

        #Setting initial score to 0
        self.scoreno = 0

        #Displaying the current score of the user
        self.score = Label(self.game_frame1, text=self.scoreno, bg=self.framegamecolor,font=('Aerial',18,'bold'))
        self.score.place(x=785, y=141)
        
        


        #Constructing labels inside the difficulty information frame (game_frame2)
        Label(self.game_frame2, text="Difficulty:", bg ='white',font=("Aerial", 18,"bold")).place(x=10, y=12)
        diffLabel=Label(self.game_frame2,text=self.game_diff,bg='white',font=("Aerial", 18))
        diffLabel.place(x=125, y=15)
        self.rule1 = Label(self.game_frame2, bg ='white',text="• Minimum letter count:", font=("Aerial", 14))
        self.rule1.place(x=25,y=50)
        self.rule2 = Label(self.game_frame2, bg ='white',text="• No repeated words", font=("Aerial", 14))
        self.rule2.place(x=25, y=80)
        self.rule3 = Label(self.game_frame2, bg ='white',text="• Valid words only", font=("Aerial", 14))
        self.rule3.place(x=25, y=110)
        diffminletter = self.diffminletter["text"]
        game_diffminletter = Label(self.game_frame2, bg='white', text=diffminletter, font=("Aerial", 14))
        game_diffminletter.place(x=220, y=50)

        #Background for the label that says "Type a word starting with the letter..."
        type_label = Label(self.game,bg='white', padx=15, pady=5,highlightbackground=self.type_labelcolor,highlightthickness = 5,justify =LEFT,text='Type a word starting\nwith the letter...',font=("Aerial", 19,"bold"))
        type_label.place(x=360,y=240)


        #Entry box for the user to enter in words
        self.word_Entry = tk.Entry(self.game, width=44, highlightbackground=self.bordergamecolor, highlightthickness=5,justify = CENTER,font=("Aerial", 29))
        self.word_Entry.place(x=9,y=450)
        self.word_Entry.focus_force()

        #Initalizing skip button to allow the user to skip letters, which will generate a new random letter.
        Skip = Button(self.game, padx = 50, text = "Skip (Esc)",command=self.skip,font=("Aerial", 15,"bold"))
        Skip.place(x=150, y=530)

        #Initalizing a submit button to allow the user to submit their word which they have entered in the word_Entry entry box.
        #When the user clicks submit, the submit function will run which will check to see if the
        #word entered in the user meets the requirements. If it does meet the requirements
        #a point is added to their score and a new letter from the alphabet is generated, if not, their word is rejected.
        Submit = Button(self.game, padx=30, text = "Submit (Enter)", command=self.submit, font=("Aerial", 15,"bold"))
        Submit.place(x=625,y=530)

        #Initializing second label, which displays how much time the user has left in their game
        self.second_var = tk.StringVar()
        self.second_lbl = tk.Label(self.game,bg=self.framegamecolor,font=('Aerial',18,'bold'),textvariable=self.second_var)
        self.second_lbl.place(x=268, y=156)
        
        #Making word list, which accumulates any words entered that also meet the word requirements which is according
        #to the validity checker in the def submit function.
        self.word_list = []
        
        #Assigning press-key-events to buttons
        self.game.bind("<Return>", lambda e:self.submit())
        self.game.bind("<Escape>", lambda e:self.skip())

        #Here I am using multi-threading which allows for a function to run in the background
        #In this case I am using multi-threading to allow for the timer to run in the background
        #This is essential as not having the timer run in the background would cause one second freezes to the
        #entire GUI, every second.
        countdown_thread = threading.Thread(target=self.count_down)
        countdown_thread.daemon = True
        countdown_thread.start()

        #Runs the random_letter_func() function, which its purpose is to randomly generate a letter from the alphabet
        #and then display that letter on the screen for the user.
        #This is to prompt the user to enter in a word that starts with that randomly generated letter.
        self.random_letter_func()

    def random_letter_func(self):
        #The purpose of this function is to randomly generate a letter from the alphabet
        #and then display that letter on the screen for the user.
        #This is to prompt the user to enter in a word that starts with that randomly generated letter.
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.random_letter = random.sample(alphabet, 1)
        if "W" in self.random_letter:
            self.letter = Label(self.game, text=self.random_letter,fg='white', bg='black',font=('Aerial',30,'bold'))
            self.letter.place(x=478,y=350)
        elif "I" in self.random_letter:
            self.letter = Label(self.game, text=self.random_letter,fg='white', bg='black',font=('Aerial',30,'bold'))
            self.letter.place(x=492,y=350)
        else:
            self.letter = Label(self.game, text=self.random_letter,fg='white', bg='black',font=('Aerial',30,'bold'))
            self.letter.place(x=483,y=350)
        


        
    

    def skip(self):
        #This function runs when the user clicks the skip button.
        #The function lets the user generate a new random letter from the alphabet.
        self.word_Entry.delete(0, 'end')
        self.letter.destroy()
        self.random_letter_func()
    def submit(self):
        word_entry = str(self.word_Entry.get())
        if len(word_entry) != 0:
            for x in self.random_letter:
                if word_entry[0].upper() == x:
                    word = word_entry.lower()
                    if word in self.dictionary_words:
                        self.rule3.config(bg='white')
                        if len(word) >= self.minletter:
                            if word in self.word_list:
                                self.rule1.config(bg='white')
                                self.rule2.config(bg='red')
                                self.rule3.config(bg='white')
                            else:
                                self.rule1.config(bg='white')
                                self.rule2.config(bg='white')
                                self.rule3.config(bg='white')
                                self.scoreno += 1
                                self.score.config(text=self.scoreno)
                                self.letter.destroy()
                                self.word_Entry.delete(0, 'end')
                                self.random_letter_func()
                                self.word_list.append(word)
                        else:
                            self.rule1.config(bg='red')
                            self.rule2.config(bg='white')
                            self.rule3.config(bg='white')
                    else:
                        self.rule2.config(bg='white')
                        self.rule3.config(bg='red')
                else:
                    self.rule1.config(bg='white')
                    self.rule2.config(bg='white')
                    self.rule3.config(bg='red')
        else:
            self.rule1.config(bg='white')
            self.rule2.config(bg='white')
            self.rule3.config(bg='red')
    def quit(self):
        sys.exit()
        
            


        
            
        
    


    def __init__(self):
        self.img_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image")
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.words_path = os.path.join(self.base_dir, "words_alpha.txt")
        with open(self.words_path, 'r') as file:
            self.dictionary_words = set(word.strip() for word in file.readlines())

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
        self.title = Label(self.window, text="A Vocabulary \nGame", bg = 'white' ,font=('Aerial',30,'bold'))
        self.title.place(x=368, y= 250)
        self.quit = Button(self.window, padx = 14,text="Quit",command=self.quit, font=('Aerial',14,'bold')).place(x=900, y =15)
        self.start = Button(self.window, padx = 20, text = "Start \n(Space)", justify = LEFT,command=self.start_game,font=("Aerial", 15,"bold"))
        self.start.place(x=338, y=450)
        self.help = Button(self.window, padx =35, pady =13, text = "Help",command=self.help,font=("Aerial", 15,"bold")).place(x=538, y=450)

        
        #Key-binding the start button to the 'space' key.
        self.window.bind("<space>", lambda e:self.start_game())

        #Setting up frames for parent self.window
        self.frame1 = Frame(self.window, bg='white', highlightbackground="black", highlightthickness=5, width = 250, height = 120)
        self.frame2 = Frame(self.window, bg='white', highlightbackground="black", highlightthickness=5,width = 250, height = 170)
        self.frame3 = Frame(self.window, bg='white', highlightbackground="black", highlightthickness=5,width = 250, height = 120)
        self.frame4 = Frame(self.window, bg='white', highlightbackground="black", highlightthickness=5,width = 250, height = 170)
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
    
        #Initializing Radiobuttons in frame2, for the difficulty option changer.
        self.r1_v = IntVar()
        self.r1_v.set(1)
        
        self.easyb = Radiobutton(self.frame2, width=7, anchor=W, text="Easy", command=self.difficulty,variable=self.r1_v, value=1, font=("Aerial", 12,"bold"))
        self.easyb.place(x=50, y=55)
        self.mediumb = Radiobutton(self.frame2, width=7, anchor=W,text="Medium",command=self.difficulty,variable=self.r1_v, value=2,font=("Aerial", 12,"bold"))
        self.mediumb.place(x=50, y=85)
        self.hardb = Radiobutton(self.frame2, width=7, anchor=W,text="Hard",command=self.difficulty,variable=self.r1_v, value=3,font=("Aerial", 12,"bold"))
        self.hardb.place(x=50, y=115)
   
        #Setting my rootcount variable to 1, for the purpose of creating a limitation that only allows
        #one help window to be opened at a time. This variable is being used in my def help function
        #and def result_close function.
        self.rootcount = 1
        
        #Dropdown Menu
        n = tk.StringVar()
        self.theme_chosen = ttk.Combobox(self.window, state='readonly',width = 25,textvariable = n,font=("Aerial", 12) )
        self.theme_chosen['values'] = ('Black & White',
                                        'Color')
        
        #Setting the theme of the window to black & white by default.
        self.theme_chosen.current(0)
        
        #Binding the selected combobox to the function def color.
        #This will be used as a way of changing the theme of the window.
        self.theme_chosen.bind("<<ComboboxSelected>>", self.color)
        self.theme_chosen.place(x=730, y=210)


        #Retrieving logo image
        logo = self.load_image("logo1.png")
        
        # Resize the logo in the given (width, height)
        logo_size=logo.resize((90, 100))

        # Convert the logo in TkImage
        my_logo=ImageTk.PhotoImage(logo_size)

        
        # Display the logo with label
        self.logo_label=Label(self.window, image=my_logo, bg='white')
        self.logo_label.place(x=455, y=60)

        #Retrieving images for game window
        time=self.load_image("time.png")
        score=self.load_image("score.png")
        square=self.load_image("square.png")

        # Resize the logo in the given (width, height)
        time_size=time.resize((100, 100))
        score_size=score.resize((90, 100))
        square_size=square.resize((110, 110))

        # Convert the logo in TkImage
        self.my_time=ImageTk.PhotoImage(time_size)
        self.my_score=ImageTk.PhotoImage(score_size)
        self.my_square=ImageTk.PhotoImage(square_size)

        
        #Setting the previous scores and highscores to 0 by default
        self.easy_prevscore=0
        self.easy_highscore=0
        self.medium_prevscore=0
        self.medium_highscore=0
        self.hard_prevscore=0
        self.hard_highscore=0
        #Initializing Previous Score & Highscore labels
        self.prev_score = Label(self.frame1, bg='white',text=0,font=("Aerial", 18,"bold"))
        self.prev_score.place(x=115, y=50)
        self.high_score = Label(self.frame3, bg='white',text=0,font=("Aerial", 18,"bold"))
        self.high_score.place(x=115,y=50)
        
        self.color()
        self.difficulty()
        
        #This line of code prevents the main window from being resized
        self.window.resizable(False, False)

        self.window.mainloop()
    def color(self, *args):
        if self.theme_chosen.current() ==0:
            #Setting the theme of the menu & game to black & white.
            self.frame1.config(highlightbackground="black")
            self.frame2.config(highlightbackground="black")
            self.frame3.config(highlightbackground="black")
            self.frame4.config(highlightbackground="black")
            self.logo_label.config(bg='white')
            self.title.config(bg='white')
            self.window.configure(bg='white')
            self.framegamecolor = "white"
            self.bordergamecolor = "black"
            self.type_labelcolor = "white"
            self.bg_gamecolor = "white"

            
        else:
            #Setting the theme of the menu & game to colored.
            self.frame1.config(highlightbackground="#ED7014")
            self.frame2.config(highlightbackground="#ED7014")
            self.frame3.config(highlightbackground="#ED7014")
            self.frame4.config(highlightbackground="#ED7014")
            self.logo_label.config(bg='#7e4614')
            self.title.config(bg='#7e4614')
            self.window.configure(bg='#7e4614')
            self.framegamecolor = "#ED7014"
            self.bordergamecolor ="#ED7014"
            self.type_labelcolor = "#ED7014"
            self.bg_gamecolor = "#7e4614"
    
    def difficulty(self):
        #If difficulty = 'Easy'
        if self.r1_v.get()==1:
            #Changing text and colors accordingly in the menu window 
            self.easyb.config(bg='green')
            self.mediumb.config(bg='white')
            self.hardb.config(bg='white')
            self.diffic.configure(bg ='green', text ="Easy",  font=("Aerial", 18,"bold"))
            self.diffminletter.configure(bg='green', text="1")

            #Setting the minimum letter count of words to 1.
            self.minletter = 1
            

            #Changing text in the game window accordingly
            self.game_diff = "Easy"
            self.prev_score.config(text=self.easy_prevscore)
            self.high_score.config(text=self.easy_highscore)
            
        #If difficulty = 'Medium'
        if self.r1_v.get()==2:
            #Changing text and colors accordingly in the menu window 
            self.easyb.config(bg='white')
            self.mediumb.config(bg='orange')
            self.hardb.config(bg='white')
            self.diffic.configure(bg ='orange', text ="Medium",  font=("Aerial", 18,"bold"))
            self.diffminletter.configure(bg='orange', text="3")

            #Setting the minimum letter count of words to 3.
            self.minletter = 3

            #Changing text in the game window accordingly
            self.game_diff = "Medium"
            self.prev_score.config(text=self.medium_prevscore)
            self.high_score.config(text=self.medium_highscore)

                

        #If difficulty = 'Hard'
        if self.r1_v.get()==3:
            #Changing text and colors accordingly in the menu window 
            self.easyb.config(bg='white')
            self.mediumb.config(bg='white')
            self.hardb.config(bg='red')
            self.diffic.configure(bg ='red', text ="Hard",  font=("Aerial", 18,"bold"))
            self.diffminletter.configure(bg='red', text="6")

            #Setting the minimum letter count of words to 6.
            self.minletter = 6

            #Changing text in the game window accordingly
            self.game_diff = "Hard"
            self.high_score.config(text=self.hard_highscore)
            self.prev_score.config(text=self.hard_prevscore)

    

#Calling class to initalize the game.
MyGUI()
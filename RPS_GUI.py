from random import randint
from tkinter import *


class RpsGame:
    '''-------------------------------------------------------------------------------------------------
    1. GAME CLASS
    -------------------------------------------------------------------------------------------------'''
    def __init__(self):
        self.human = 'empty'
        self.bot = 'empty'
        self.winner = 'No one has won yet'
        print('starting with: ' + self.human + ' & ' + self.bot )

    def findwinner(self):
        if (self.human == 'rock' and self.bot == 'rock'):
            self.winner = 'Its a tie'
        elif (self.human == 'rock' and self.bot == 'paper'):
            self.winner = 'You lose'
        elif (self.human == 'rock' and self.bot == 'scissors'):
            self.winner = 'You WIN!' 

        elif self.human == 'paper' and self.bot == 'paper':
            self.winner = 'Its a tie'
        elif self.human == 'paper' and self.bot == 'scissors':
            self.winner = 'You lose'
        elif self.human == 'paper' and self.bot == 'rock':
            self.winner = 'You WIN!' 

        elif self.human == 'scissors' and self.bot == 'scissors':
            self.winner = 'Its a tie'
        elif self.human == 'scissors' and self.bot == 'rock':
            self.winner = 'You lose'
        elif self.human == 'scissors' and self.bot == 'paper':
            self.winner = 'You WIN!'
        else:
            self.winner = 'Incorrect Entry'
        

    def botchoice(self):
        if (randint(1, 3)) == 1:
            self.bot = 'rock'
        elif (randint(1, 3)) == 2:
            self.bot = 'paper'
        else:
            self.bot = 'scissors'
        


 
 
 
'''-------------------------------------------------------------------------------------------------
2. GAME GUI
-------------------------------------------------------------------------------------------------'''


class GUI:
    def __init__(self, master):
        
        self.master = master
        master.title("RPS!")
        master.geometry("400x400+100+100")

        self.label = Label(master, text="Select Rock, Paper, Or Scissors", fg = "black", bg = "white", font = "Helvetica 8 bold")
        self.label.pack(pady=20, padx = 20)

        self.greet_button = Button(master, text="Rock", command=lambda *args: self.play("rock"))
        self.greet_button.pack(pady=10, padx = 10)

        self.greet_button = Button(master, text="Paper", command=lambda *args: self.play("paper"))
        self.greet_button.pack(pady=10, padx = 10)

        self.greet_button = Button(master, text="Scissors", command=lambda *args: self.play("scissors"))
        self.greet_button.pack(pady=10, padx = 10)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(pady=20, padx = 10)

        self.listbox = Listbox(master)
        self.listbox.pack(pady=20, padx = 10)

    def play(self, playerchoice):
        self.playerchoice = playerchoice
        GameInstance = RpsGame()
        GameInstance.human = playerchoice
        GameInstance.botchoice()
        GameInstance.findwinner()
      
        self.listbox.delete(0, END)
        self.listbox.insert(END,'You play: ' + GameInstance.human)
        self.listbox.insert(END,'Bot plays: ' + GameInstance.bot)
        self.listbox.insert(END,GameInstance.winner)
       
root = Tk()
my_gui = GUI(root)
root.mainloop()

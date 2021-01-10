from tkinter import *
import random
window = Tk() #initialize tkinter
window.geometry('400x400')  #set size/geometry of window
window.resizable(0,0)
window.title('First Rock-Paper-Scissor Game')   #title of the window
window.config(bg = 'turquoise')
Label(window, text = 'Rock, Paper, Scissors', font = 'helvetica 20 bold', bg = 'dark turquoise').pack() #display text, pack organize widget in block
user_input = StringVar()
Label(window, text = 'Choose any one : rock, paper, scissors', font = 'arial 14 bold', bg= 'seashell2').place(x=20, y=70)
Entry(window, font = 'arial 14', textvariable = user_input , bg = 'antiquewhite2').place(x=90 , y = 130)

comp_pick = random.randint(1,3)

#choice made by computer

if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'

Result = StringVar()

#function for the game/defining the game
def play():
    user_pick = user_input.get()
    if user_pick == comp_pick:
        Result.set('tie,you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose,computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you loose,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')

#to set variables result and user_input to empty string
def Reset():
    Result.set("")
    user_input.set("")

#exit function
def Exit():
    window.destroy()

Entry(window, font='helvetica 10 bold', textvariable = Result, bg = 'turquoise', width=50).place(x=25, y=250)

#defining PLAY Button
Button(window, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=190)

#defining RESET Button
Button(window, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=70,y=310)

#defining EXIT Button
Button(window, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=310)


window.mainloop()

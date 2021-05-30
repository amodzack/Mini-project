#THE COLOUR GAME
#Are you ready to play?
import tkinter
import random
colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown','Grey','Maroon']
score = 0 
timeleft = 75
def start_game(event):
   if timeleft == 75:
      countdown()
   nxtcolour()
def nxtcolour():
   global timeleft
   global score
   if timeleft > 0:
      e.focus_set()
      if e.get().lower() == colours[1].lower():
         score += 1
      e.delete(0,tkinter.END) 
      random.shuffle(colours)
      label.config(fg = str(colours[1]), text = str(colours[0]))
      scoreLabel.config(text = "SCORE: "+str(score))
def countdown():
   global timeleft
   if timeleft > 0:
      timeleft -= 1
      timeLabel.config(text = "TIME LEFT: "+str(timeleft))
      timeLabel.after(1000, countdown)

root = tkinter.Tk()
root.title("THE COLORGAME")
root.geometry("420x297")

instructions = tkinter.Label(root, text = "Type in the colour of the words, and not the word text!",font = ('Calibri', 14))
instructions.pack()

scoreLabel = tkinter.Label(root, text = "Press enter to start",font = ('Calibri', 11))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text = "TIME LEFT: "+str(timeleft),font = ('Calibri', 11))               
timeLabel.pack()
  
label = tkinter.Label(root, font = ('Calibri', 60))
label.pack()
  
e = tkinter.Entry(root)
  
root.bind('<Return>', start_game)
e.pack()

e.focus_set()

root.mainloop()
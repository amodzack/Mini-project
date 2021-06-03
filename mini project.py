#THE COLOUR GAME
#Are you ready to play?
import tkinter
import random

colours = [
    'Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White',
    'Purple', 'Brown', 'Grey', 'Maroon'
]
score = 0
timeleft = 75
word = ''


def start_game():
    if timeleft == 75:
        countdown()
        word = random.choice(colours).lower()
        label.config(text=random.choice(colours), fg=word)
        e.bind('<Return>', nxtcolour)


def nxtcolour(event):
    global timeleft
    global score
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="SCORE: " + str(score))


def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="TIME LEFT: " + str(timeleft))
        timeLabel.after(1000, countdown)
    elif timeleft == 0:
        timeLabel.config(text="Time's up!!!")


def reset():
    global timeleft
    global score
    global word
    timeleft = 75
    score = 0
    word = ''
    scoreLabel.config(text="SCORE: " + str(score))
    label.config(text='')
    timeLabel.config(text="TIME LEFT: ")
    e.delete(0, tkinter.END)


window = tkinter.Tk()
window.title("THE COLORGAME")
window.geometry("525x400")

instructions = tkinter.Label(
    window,
    text="Type in the colour of the words, and not the word text!",
    font=('Algerian', 12))
instructions.pack()

scoreLabel = tkinter.Label(window, text="Press Start", font=('Algerian', 11))
scoreLabel.pack()

timeLabel = tkinter.Label(window,
                          text="TIME LEFT: " + str(timeleft),
                          font=('Algerian', 11))
timeLabel.pack()

start_button = tkinter.Button(window,
                              text="Start",
                              width=20,
                              fg="black",
                              bg="white",
                              activebackground="blue",
                              command=start_game)
start_button.pack()

reset_button = tkinter.Button(window,
                              text="Reset",
                              width=20,
                              fg="black",
                              bg="white",
                              activebackground="red",
                              command=reset)
reset_button.pack()

label = tkinter.Label(window, font=('Algerian', 60))
label.pack()

e = tkinter.Entry(window, bd=10)
e.pack()

e.focus_set()

window.mainloop()

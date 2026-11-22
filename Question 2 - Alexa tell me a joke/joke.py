# imports the tkinter module along with the random library
from tkinter import *
import random

# ====== Sets up the output window ======
root = Tk()

# Changes the window title, size icon and background
root.title("Tell me a Joke !")
root.geometry("650x350")
root.resizable(0,0) # Makes the user unable to change the window size
root.iconbitmap("Question 2 - Alexa tell me a joke/kirby.ico")
root.configure(bg="#771040")

# ====== Functions======
# Global variable for the punchline of the joke from the text file
punchline1 = ""

# Opens and reads the provided text file with the jokes and punuchlines
randomjokes = open("Assessment 1 - Skills Portfolio/A1 - Resources/randomJokes.txt", "r")
jokes = randomjokes.readlines()
randomjokes.close()

# Defines a function for the alexa button to show a joke
def TellJoke():
    global punchline1

    # chooses a random joke frmo the text file
    joke1 = random.choice(jokes)

    # Separates the setup and the punchline in one line using the question mark into parts
    part = joke1.strip().split("?", 1)

    # Defines the setup as "joke2" and adds a question mark at the end
    joke2 = part[0] + "?"
    # Defines the second part of the line as "punchline1" using the global variable
    punchline1 = part[1]

    # Changes the text in the joke and punchline labels
    joke.config(text= joke2)
    # Clears the punchline label for the new joke
    punchline.config(text="")

# Defines the function to show the punchline
def show_punchline():
    # Changes the text in the punchline label to 
    punchline.config(text= punchline1)


def QuitJokes():
    root.destroy()

# ====== Design for the GUI======
# Configures the rows to use the window height equally
for row in range(8):
    root.grid_rowconfigure(row, weight=1)
# Configures the columns to use the window width equally
for column in range(6):
    root.grid_columnconfigure(column, weight=1)

# Creates the title label
title = Label(root, text="Want a joke?", font=("Times New Roman", 20, "bold"), bg="#771040", fg="#E9E4DD")
# Positions the title label inside the grid
title.grid(row=0, column=2, rowspan=2, columnspan=2, sticky=NSEW)

# Creates an empty label for the joke to be displayed
joke = Label(root, text="", font=("Times New Roman", 16), bg="#771040", fg="#E9E4DD")
# Positions the joke label inside the grid
joke.grid(row=3, column=1, columnspan=4, sticky=NSEW)

# Creates an empty label for the joke to be displayed
punchline = Label(root, text="", font=("Times New Roman", 14), bg="#771040", fg="#E9E4DD")
# Positions the punchline label inside the grid
punchline.grid(row=4, column=1, columnspan=4, sticky=NSEW)

# Creates a button which selects a random joke and displays it in the joke label
alexa = Button(root,text="Alexa, tell me a joke", font=("Courier New", 16, "bold"), fg="#771040", bg="#E9E4DD", width=40, command= TellJoke)
# Positions the alexa button inside the grid
alexa.grid(row=5, column=1, columnspan=4, sticky=NSEW, pady=5)

# Creates a button to reveal the punchline in the punchline label
show = Button(root,text="Show punchline", font=("Courier New", 14), bg="#771040", fg="#E9E4DD", width=20, command=show_punchline)
# Positions the show button inside the grid
show.grid(row=6, column=1, columnspan=2, sticky=NSEW, pady=5, padx=6)

# Creates a button to select another joke from the list
next = Button(root,text="Next Joke", font=("Courier New", 14), bg="#771040", fg="#E9E4DD", width=20, command= TellJoke)
# Positions next button inside the grid
next.grid(row=6, column=3, columnspan=2, sticky=NSEW, pady=5, padx=6)

# Createes the exit button to close the window
exit = Button(root, text="EXIT", font=("Courier New", 14, "bold"), bg="#530228", fg="#E9E4DD", command=lambda: QuitJokes())
# Positions the exit button inside the grid
exit.grid(row=7, column=2, columnspan=2, sticky=NSEW, pady=5)

# Runs the application
root.mainloop()
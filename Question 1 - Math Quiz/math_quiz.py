# imports the tkinter module for the GUI, Pillow for images, and the random library
from tkinter import *
from PIL import ImageTk, Image
import random

# ====== Sets up the output window ======
root = Tk()

# Changes the window title, size icon and background
root.geometry('500x500')
root.configure(bg="#FBF9E2")
root.title("Maths Quiz!")
root.iconbitmap("Question 1 - Math Quiz/smiski.ico")
root.resizable(0,0) # Makes the user unable to change the window size

# global variables
score = 0
correct_question = 0
question_num = 0
attempt = 1
correct = 0
min_num = 0
max_num = 9

# ====== Functions ======
# generate a random number
def randomInt():
      return random.randint(min_num, max_num)

# generate a random operation, descision between addition and subtraction:
def decideOperation():
      return random.choice(["+", "-"])

# closes the window
def ExitQuiz():
      root.destroy()

# function to display the difficulty menu and sqitch between frames
def DisplayMenu(menu):
    menu.tkraise()

# function to display the question to be done by the user
def displayProblem():
    global correct, attempt

    if question_num == 10:
            displayResults()
            return

    attempt = 1

    num1 = randomInt()
    num2 = randomInt()
    operation = decideOperation()

    if operation == "+":
            correct = num1 + num2
    else:
           correct = num1 - num2

    # Changes the text in the question label
    question.config(
          text=f"Question {question_num + 1} of 10"
    )

    # Changes the text in the problem label
    problem.config(
          text=f"{num1} {operation} {num2}"
    )

    # resets the answer entry and feedback label for the question
    answer.delete(0, END)
    feedback.config(text="")

    # sets focus on the answer entry so there is immediate keyboard input
    answer.focus()

# function to start the quiz
def QuizStart(level):
    global min_num, max_num
    global score, question_num, correct_question

    # if statements for the specific difficulties and the set minimun and maximum numbers
    if level == "Easy":
        min_num = 0
        max_num = 9
    if level == "Medium":
            min_num = 10
            max_num = 99
    if level == "Hard":
            min_num = 1000
            max_num = 9999

    # sets the score, question number, and number of correct questions to 0 at the start of each quiz
    score = 0
    question_num = 0
    correct_question = 0

    # sets the score value at 0 at the start of each quiz
    score1.config(text="Score: 0 / 100")

    # displays the quiz frame for the user
    DisplayMenu(quiz)
    # calls the display problem function
    displayProblem()

# function to see if the correct answer and the user's answer is the same
def isCorrect(user_answer):
      return user_answer == correct

# Function which checks the user's answer and responds accordingly if there is an incorrect answer, correct answer, or value error
def checkanswer():
      global score, question_num, attempt, correct_question

      try :
         user_answer = int (answer.get())

      # Ensures the answer entry only accepts integer entries
      except ValueError:
            feedback.config(
                  text="Please enter a valid integer.",
                  fg="#414B32"
            )
            return
      # checks users answer and awards point based on the number of attepts or none if the answer is incorrect twice
      if isCorrect(user_answer):
                if attempt == 1:
                        score += 10
                        feedback.config(
                        text="+ 10 points!",
                        fg="#414B32")
                        
                else:
                 score += 5
                 feedback.config(
                     text="+ 5 points!",
                     fg="#414B32"
                )
                question_num += 1
                correct_question += 1

                root.after(1000, displayProblem)
                score1.config(text=f"Score: {score} / 100")
      else: 
            if attempt == 1:
                  attempt = 2

                  feedback.config(
                                    text="Incorrect! Please try again!",
                                    fg="#414B32"
                              )
                  answer.delete(0, END)
                  answer.focus()
            else:
                  feedback.config(
                                    text=f"Correct answer: {correct}",
                                    fg="#414B32"
                              )
                  question_num += 1

                  root.after(1500, displayProblem)

# Displaying the results frame and giving the final score and grade
def displayResults():
      DisplayMenu(results)

      correct_qs.config(
            text = f"You got {correct_question} questions correct out of 10 !"
      )

      results_score.config(
            text=f"Final Score: {score} / 100"
      )

      # if else statement for giving a grade to the user
      if score > 90:
            grade = "A+"

      elif score >= 80:
            grade = "A"

      elif score >= 70:
            grade = "B"

      elif score >= 60:
            grade = "C"

      elif score >= 50:
            grade = "D"

      else:
            grade = "F"

      results_grade.config(
            text= f"Final Grade: {grade}"
      )
      
# ====== Heading ======
# Design label 1
design = Label(root, text ="˚₊۶ৎ˙⋆", 
               font=('Georgia',20), 
               bg="#FBF9E2", fg="#414B32")
# Places and positions the label beside the title
design.place(x=60, y=20)

# Common title header for the program
title = Label(root, text="Maths Quiz", 
              font=('Georgia',20), 
              bg="#FBF9E2",fg="#414B32")
# Places and positions the title in the top middle of the root window
title.place(x=180, y=20)

# Design label 2
design2 = Label(root, text ="˚₊۶ৎ˙⋆", 
                font=('Georgia',20), 
                bg="#FBF9E2", fg="#414B32")
# Places and positions the label beside the title
design2.place(x=350, y=20)

# ====== Menu =======
# Creates a menu frame for the difficulty seleciton
menu = Frame(root, bg="#3D4B32")

# Imports an image using pillow to be resized ans used as the background of the menu frame
bg1 = Image.open("Question 1 - Math Quiz/green-dot.jpg") 
bg2 = bg1.resize((500,500)) 
img2 = ImageTk.PhotoImage(bg2)
imgLabel2 = Label(menu, image=img2)
imgLabel2.place(x=-2, y=-2)

# The header label for the menu frame
label = Label(menu, text="Please pick a difficulty!", 
              font=('Georgia', 16, 'bold'), 
              bg="#414B32", fg="#FBF9E2", 
              relief='solid', height=2 ,width=30)
label.pack(pady=(50,30), padx=20)

# Button for the easy quiz to take the user to the correct frame using the QuizStart command
easy = Button(menu, text="Easy", 
              font=('Georgia', 16, 'bold'), 
              bg="#FBF9E2", fg="#414B32", 
              width=30, 
              activebackground="#414B32", 
              activeforeground="#FBF9E2", 
              command=lambda: QuizStart("Easy"))
easy.pack(pady=10)

# Button for the medium quiz to take the user to the correct frame using the QuizStart command
medium = Button(menu, text="Medium", 
                font=('Georgia', 16, 'bold'), 
                bg="#FBF9E2", fg="#414B32", 
                width=30, 
                activebackground="#414B32", 
                activeforeground="#FBF9E2",
                command=lambda: QuizStart("Medium"))
medium.pack(pady=10)

# Button for the hard quiz to take the user to the correct frame using the QuizStart command
hard = Button(menu, text="Hard", 
              font=('Georgia', 16, 'bold'), 
              bg="#FBF9E2", fg="#414B32", 
              width=30, 
              activebackground="#414B32", 
              activeforeground="#FBF9E2",
              command=lambda: QuizStart("Hard"))
hard.pack(pady=10)

# Places the menu frame so it can be called
menu.place(x=0, y=70, height=500, width=500)

# Quiz frame
quiz = Frame(root, bg="#3D4B32")
# Imports an image using pillow to be resized ans used as the background of the quiz frame
quiz_bg = Image.open("Question 1 - Math Quiz/pattern.jpg") 
quiz_bg1 = quiz_bg.resize((500,500)) 
quiz_bg2 = ImageTk.PhotoImage(quiz_bg1)
bgLabel2 = Label(quiz, image=quiz_bg2)
bgLabel2.place(x=-2, y=-2)

# Question label showing which question the user is on
question = Label(quiz, text = "Question 1 of 10", 
                 font=('Georgia', 16, 'bold'), 
                 bg="#E6E2B7", fg="#414B32")
question.place(x=23, y=15)

# The score label showing the user how many points they have earned
score1 = Label(quiz, text="Score: 0 / 100", 
               font=('Georgia', 16, 'bold'), 
                 bg="#E6E2B7", fg="#414B32")
score1.place(x=321, y=15)

# the problem label used by the showproblem function to display a maths problem
problem = Label(quiz, text = "", 
                font=('Georgia', 16, 'bold'), 
                bg="#E6E2B7", fg="#414B32" )
problem.pack(pady=(80,10))

# An entry section for the user to input their answers to the given problem
answer = Entry(quiz, 
               font=('Georgia', 16, 'bold'), 
               bg="#E6E2B7", fg="#414B32", 
               width=30)
answer.pack(pady=20)

# The feedback label used to display the amount of points earned, 
# the correct answer is the user is incorrect on both attempts, 
# and a warning if the user has not inputted integers
feedback = Label(quiz, 
                 font=('Georgia', 12, 'bold'), 
                 bg="#E6E2B7", fg="#414B32")

feedback.pack(pady=10)

# A button for the user to sumbmit the answer they have entered
submit = Button(quiz, text = "Submit", 
                font=('Georgia', 16, 'bold'), 
                bg="#E6E2B7", fg="#414B32",
                activebackground="#414B32",
                activeforeground="#E6E2B7",
                width= 30, command=checkanswer)
submit.pack(pady=20)

# A button for the user to return to the menu while in the quiz
home = Button (quiz, text="< Go back to menu",
               font=('Georgia', 10, 'bold'), 
                bg="#E6E2B7", fg="#414B32",
                activebackground="#414B32",
                activeforeground="#E6E2B7",
                width= 15, command=lambda: DisplayMenu(menu))
home.place(x=5, y=395)

# A button for the user to exit the program while in the quiz
close = Button (quiz, text="Exit quiz >",
               font=('Georgia', 10, 'bold'), 
                bg="#E6E2B7", fg="#414B32",
                activebackground="#414B32",
                activeforeground="#E6E2B7",
                width= 15, command=lambda: ExitQuiz())
close.place(x=350, y=395)

# Places the quiz frame so it is ready to be called 
quiz.place(x=0, y=70, height=500, width=500)


# ====== Results Frame ======
results = Frame(root, bg="#FBF9E2")
# Imports an image using pillow to be resized ans used as the background of the results frame
results_bg = Image.open("Question 1 - Math Quiz/green-plaid.jpg") 
results_bg1 = results_bg.resize((500,500)) 
results_bg2 = ImageTk.PhotoImage(results_bg1)
bgLabel3 = Label(results, image=results_bg2)
bgLabel3.place(x=-2, y=-2)

# Header for the results page
results_title = Label(results, text="✮⋆˙ Your Results ˙⋆✮ ", 
                  font=('Georgia', 16, 'bold'), 
                  bg="#ECF5E0", fg="#414B32")
results_title.pack(pady=10)

# Label to show the number of correctly answered questions
correct_qs = Label(results, 
                  font=('Georgia', 16, 'bold'), 
                  bg="#ECF5E0", fg="#414B32")
correct_qs.pack(pady=10)

# Label to show the final scored the user got
results_score = Label(results, 
              font=('Georgia', 16, 'bold'), 
              bg="#ECF5E0", fg="#414B32" )
results_score.pack(pady=10)

# Label to show the final grade the user achieved
results_grade = Label(results, 
              font=('Georgia', 16, 'bold'), 
              bg="#ECF5E0", fg="#414B32" )
results_grade.pack(pady=10)

# A restart button to bring the user back to the menu to select another quiz
restart = Button(results, text="Return to Menu",
              font=('Georgia', 16, 'bold'), 
              fg="#ECF5E0", bg="#414B32",
              activebackground="#ECF5E0",
              activeforeground="#414B32",
              command=lambda: DisplayMenu(menu))
restart.pack(pady= 5)

# An exit button to close the crogram
done = Button(results, text="Exit Quiz",
              font=('Georgia', 16, 'bold'), 
              fg="#ECF5E0", bg="#414B32",
              activebackground="#ECF5E0",
              activeforeground="#414B32",
              command=lambda: ExitQuiz())
done.pack(pady= 5)

# Places the results frame so it is ready to be called
results.place(x=0, y=70, height=500, width=500)

# Calls the menu frame as the first frame the user sees
DisplayMenu(menu)

# Runs the application
root.mainloop()

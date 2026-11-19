from tkinter import *
from PIL import ImageTk, Image
import random
root = Tk()

root.geometry('500x500')
root.configure(bg="#FBF9E2")
root.title("Maths Quiz!")
root.iconbitmap("Question 1 - Math Quiz/smiski.ico")
root.resizable(0,0)

# global variables
score = 0
correct_question = 0
question_num = 0
attempt = 1
correct = 0
min_num = 0
max_num = 9

# generate a random number
def randomInt():
      return random.randint(min_num, max_num)

# generate a random operation, descision between addition and subtraction:
def decideOperation():
      return random.choice(["+", "-"])

# closes the window
def ExitQuiz():
      root.destroy()

# function to display the difficulty menu
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

    question.config(
          text=f"Question {question_num + 1} of 10"
    )

    problem.config(
          text=f"{num1} {operation} {num2}"
    )

    answer.delete(0, END)
    feedback.config(text="")

    answer.focus()

# function to start the quiz
def QuizStart(level):
    global min_num, max_num
    global score, question_num, correct_question

    if level == "Easy":
        min_num = 0
        max_num = 9
    if level == "Medium":
            min_num = 10
            max_num = 99
    if level == "Hard":
            min_num = 1000
            max_num = 9999

    score = 0
    question_num = 0
    correct_question = 0

    score1.config(text="Score: 0 / 100")

    DisplayMenu(quiz)
    displayProblem()

def isCorrect(user_answer):
      return user_answer == correct

def checkanswer():
      global score, question_num, attempt, correct_question

      try :
         user_answer = int (answer.get())

      except ValueError:
            feedback.config(
                  text="Please enter a valid integer.",
                  fg="#414B32"
            )
            return
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
      

# Menu
menu = Frame(root, bg="#3D4B32")
bg1 = Image.open("Question 1 - Math Quiz/green-dot.jpg") 
bg2 = bg1.resize((500,500)) 
img2 = ImageTk.PhotoImage(bg2)
imgLabel2 = Label(menu, image=img2)
imgLabel2.place(x=-2, y=-2)

design = Label(root, text ="˚₊۶ৎ˙⋆", 
               font=('Georgia',20), 
               bg="#FBF9E2", fg="#414B32")
design.place(x=60, y=20)

design2 = Label(root, text ="˚₊۶ৎ˙⋆", 
                font=('Georgia',20), 
                bg="#FBF9E2", fg="#414B32")
design2.place(x=350, y=20)

title = Label(root, text="Maths Quiz", 
              font=('Georgia',20), 
              bg="#FBF9E2",fg="#414B32")
title.place(x=180, y=20)

label = Label(menu, text="Please pick a difficulty!", 
              font=('Georgia', 16, 'bold'), 
              bg="#414B32", fg="#FBF9E2", 
              relief='solid', height=2 ,width=30)
label.pack(pady=(50,30), padx=20)

easy = Button(menu, text="Easy", 
              font=('Georgia', 16, 'bold'), 
              bg="#FBF9E2", fg="#414B32", 
              width=30, 
              activebackground="#414B32", 
              activeforeground="#FBF9E2", 
              command=lambda: QuizStart("Easy"))
easy.pack(pady=10)

medium = Button(menu, text="Medium", 
                font=('Georgia', 16, 'bold'), 
                bg="#FBF9E2", fg="#414B32", 
                width=30, 
                activebackground="#414B32", 
                activeforeground="#FBF9E2",
                command=lambda: QuizStart("Medium"))
medium.pack(pady=10)

hard = Button(menu, text="Hard", 
              font=('Georgia', 16, 'bold'), 
              bg="#FBF9E2", fg="#414B32", 
              width=30, 
              activebackground="#414B32", 
              activeforeground="#FBF9E2",
              command=lambda: QuizStart("Hard"))
hard.pack(pady=10)

menu.place(x=0, y=70, height=500, width=500)

# Quiz frame
quiz = Frame(root, bg="#3D4B32")
quiz_bg = Image.open("Question 1 - Math Quiz/pattern.jpg") 
quiz_bg1 = quiz_bg.resize((500,500)) 
quiz_bg2 = ImageTk.PhotoImage(quiz_bg1)
bgLabel2 = Label(quiz, image=quiz_bg2)
bgLabel2.place(x=-2, y=-2)

question = Label(quiz, text = "Question 1 of 10", 
                 font=('Georgia', 16, 'bold'), 
                 bg="#E6E2B7", fg="#414B32")
question.place(x=23, y=15)

score1 = Label(quiz, text="Score: 0 / 100", 
               font=('Georgia', 16, 'bold'), 
                 bg="#E6E2B7", fg="#414B32")
score1.place(x=321, y=15)

problem = Label(quiz, text = "", 
                font=('Georgia', 16, 'bold'), 
                bg="#E6E2B7", fg="#414B32" )
problem.pack(pady=(80,10))

answer = Entry(quiz, 
               font=('Georgia', 16, 'bold'), 
               bg="#E6E2B7", fg="#414B32", 
               width=30)
answer.pack(pady=20)

feedback = Label(quiz, 
                 font=('Georgia', 12, 'bold'), 
                 bg="#E6E2B7", fg="#414B32")

feedback.pack(pady=10)

submit = Button(quiz, text = "Submit", 
                font=('Georgia', 16, 'bold'), 
                bg="#E6E2B7", fg="#414B32",
                activebackground="#414B32",
                activeforeground="#E6E2B7",
                width= 30, command=checkanswer)
submit.pack(pady=20)

quiz.place(x=0, y=70, height=500, width=500)


# Results Frame
results = Frame(root, bg="#FBF9E2")
results_bg = Image.open("Question 1 - Math Quiz/green-plaid.jpg") 
results_bg1 = results_bg.resize((500,500)) 
results_bg2 = ImageTk.PhotoImage(results_bg1)
bgLabel3 = Label(results, image=results_bg2)
bgLabel3.place(x=-2, y=-2)

results_title = Label(results, text="✮⋆˙ Your Results ˙⋆✮ ", 
                  font=('Georgia', 16, 'bold'), 
                  bg="#ECF5E0", fg="#414B32")
results_title.pack(pady=10)

correct_qs = Label(results, 
                  font=('Georgia', 16, 'bold'), 
                  bg="#ECF5E0", fg="#414B32")
correct_qs.pack(pady=10)

results_score = Label(results, 
              font=('Georgia', 16, 'bold'), 
              bg="#ECF5E0", fg="#414B32" )
results_score.pack(pady=10)

results_grade = Label(results, 
              font=('Georgia', 16, 'bold'), 
              bg="#ECF5E0", fg="#414B32" )
results_grade.pack(pady=10)

restart = Button(results, text="Return to Menu",
              font=('Georgia', 16, 'bold'), 
              fg="#ECF5E0", bg="#414B32",
              activebackground="#ECF5E0",
              activeforeground="#414B32",
              command=lambda: DisplayMenu(menu))
restart.pack(pady= 5)

done = Button(results, text="Exit Quiz",
              font=('Georgia', 16, 'bold'), 
              fg="#ECF5E0", bg="#414B32",
              activebackground="#ECF5E0",
              activeforeground="#414B32",
              command=lambda: ExitQuiz())
done.pack(pady= 5)

results.place(x=0, y=70, height=500, width=500)

DisplayMenu(menu)

root.mainloop()

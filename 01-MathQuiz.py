from tkinter import *
from random import randint


root= Tk()
root.geometry("500x500")
root.title("Math Quiz")
root.grid_columnconfigure(0, weight=1)
root['bg']='beige'
# Frames Switching
menuFrame = Frame(root, bg = "beige")
menuFrame.grid(row=0, column=0, sticky="nsew")

quizFrame = Frame(root, bg = "beige")
quizFrame.grid(row=0, column=0, sticky="nsew")

menuFrame.tkraise()



# Difficulty Menu
def displayMenu():
   
    headingLabel = Label(
        menuFrame,
        text="Math Quiz",
        font=("Roboto", 22)
    )
    headingLabel.grid(row=0, column=0, pady=20)

    difficultyLabel = Label(
        menuFrame,
        text="Select Difficulty",
        font= ("Roboto", 16)
    )
    difficultyLabel.grid(row=1, column=0, pady=10)

    easyButton = Button(
        menuFrame,
        text="Easy",
        font= ("Roboto", 14),
        width=15,
        command=lambda: startQuiz("Easy")
        )
    easyButton.grid(row=2, column=0, pady=5)

    moderateButton = Button(
        menuFrame,
        text="Moderate",
        font= ("Roboto", 14),
        width=15,
        command=lambda: startQuiz("Moderate")
        )
    moderateButton.grid(row=3, column=0, pady=5)

    advancedButton = Button(
        menuFrame,
        text="Advanced",
        font= ("Roboto", 14),
        width=15,
        command=lambda: startQuiz("Advanced")
        )
    advancedButton.grid(row=4, column=0, pady=5)

    
def startQuiz(difficulty):
    menuFrame.lower()
    quizFrame.tkraise()
    displayProblem(difficulty)

# Random Number Generator
def randomInt(difficulty):
    if difficulty == "Easy":
        number = randint(1, 9)
    elif difficulty == "Moderate":
        number = randint(10, 99)
    elif difficulty == "Advanced":
        number = randint(1000, 9999)
    
    return number

# Decide Operation
def decideOperation():
    operation = randint(1,2)
    
    if operation == 1:
        return "+"
    elif operation == 2:
        return "-"  
    
def displayProblem (difficulty):
    number1 = randomInt(difficulty)
    number2 = randomInt(difficulty)
    operation = decideOperation()
    
    if operation == "+":
        correctAnswer = number1 + number2
    elif operation == "-":
        correctAnswer = number1 - number2
        
    questionLabel = Label(
        quizFrame,
        text=f"{number1} {operation} {number2} = ?",
        font=("Roboto", 22) 
    )
    questionLabel.grid(row=5, column=0, pady=20)

    

displayMenu()
root.mainloop()   
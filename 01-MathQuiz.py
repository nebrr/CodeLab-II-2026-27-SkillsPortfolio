from tkinter import *
from random import randint
score = 0
attempts = 0
difficulty = ""
questionNumber = 0


root= Tk()
root.geometry("500x500")
root.title("Math Quiz")
root['bg']='beige'
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)


# Frames Switching
menuFrame = Frame(root, bg = "beige")
menuFrame.grid(row=0, column=0, sticky="nsew")
menuFrame.grid_columnconfigure(0, weight=1)


quizFrame = Frame(root, bg = "beige")
quizFrame.grid(row=0, column=0, sticky="nsew")
quizFrame.grid_columnconfigure(0, weight=1)
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
    moderateButton.grid(row=3, column=0, pady=20)

    advancedButton = Button(
        menuFrame,
        text="Advanced",
        font= ("Roboto", 14),
        width=15,
        command=lambda: startQuiz("Advanced")
        )
    advancedButton.grid(row=4, column=0, pady=5)

def startQuiz(selectedDifficulty):
    global difficulty, score, attempts, questionNumber
    
    difficulty = selectedDifficulty
    score = 0
    attempts = 0 
    questionNumber = 0
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
    global attempts, questionNumber
    attempts = 0
    questionNumber += 1
    questionCounterLabel = Label(
        quizFrame,
        text=f"Question{questionNumber}/10",
        font=("Roboto",14)
    )
    questionCounterLabel.grid(row=3, column=0, pady=10)
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
    questionLabel.grid(row=4, column=0, pady=10)
    
    scoreLabel = Label(
        quizFrame,
        text=f"Score: {score}",
        font=("Roboto",14)
      
    )
    scoreLabel.grid(row=5, column=0, pady=20)

    answerEntry = Entry(
        quizFrame,
        font=("Roboto", 16),
        width=10
    )
    answerEntry.grid(row=6, column=0, pady=10)
    
    resultLabel = Label(
        quizFrame,
        text = "",
        font=("Roboto", 14)
    )
    resultLabel.grid(row=8, column=0, pady=10)

    submitButton = Button(
            quizFrame,
            text="Submit",
            font=("Roboto", 14),
            width=15,
            command=lambda: isCorrect(
                int(answerEntry.get()),
                correctAnswer,
                resultLabel,
                scoreLabel
            )
    )
    submitButton.grid(row=7, column=0, pady=5)

def isCorrect(userAnswer, correctAnswer, resultLabel, scoreLabel): 
    global score, attempts

    if userAnswer == correctAnswer:
        if attempts == 0:
            score +=10 
            resultLabel.config(text="correct! + 10 Points") 
        else:
            score += 5
            resultLabel.config(text="correct! + 5 Points")
        
        nextQuestion()    
    else:
        attempts +=1
        if attempts ==1:
            resultLabel.config(text="Incorrect! Try Again")
        else:
            resultLabel.config(text="No more Attempts :( ")

def nextQuestion():
    displayProblem(difficulty)



displayMenu()
root.mainloop()   
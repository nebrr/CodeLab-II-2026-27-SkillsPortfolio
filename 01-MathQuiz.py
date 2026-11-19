from tkinter import *
from random import randint
score = 0
attempts = 0
difficulty = ""
questionNumber = 0
question_finished = False


root= Tk()
root.geometry("500x500")
root.title("Math Quiz")
root['bg']='#926c4d'
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)


# Frames Switching
menuFrame = Frame(root, bg = "#926c4d")
menuFrame.grid(row=0, column=0, sticky="nsew")
menuFrame.grid_columnconfigure(0, weight=1)


quizFrame = Frame(root, bg = "#926c4d")
quizFrame.grid(row=0, column=0, sticky="nsew")
quizFrame.grid_columnconfigure(0, weight=1)
menuFrame.tkraise()


resultsFrame = Frame(root, bg="#926c4d")
resultsFrame.grid(row=0, column=0, sticky="nsew")
resultsFrame.grid_remove()

menuFrame.tkraise()

# Difficulty Menu
def displayMenu():
   
    headingLabel = Label(
        menuFrame,
        text="Math Quiz",
        font=("Minecraft", 22),
        bg=  "#926c4d"
    )
    headingLabel.grid(row=0, column=0, pady=20)

    difficultyLabel = Label(
        menuFrame,
        text="Select Difficulty",
        font= ("Minecraft", 16),
        bg = "#926c4d"
    )
    difficultyLabel.grid(row=1, column=0, pady=10)

    easyButton = Button(
        menuFrame,
        text="Easy",
        font= ("Minecraft", 14),
        width=15,
        command=lambda: startQuiz("Easy")
        )
    easyButton.grid(row=2, column=0, pady=5)

    moderateButton = Button(
        menuFrame,
        text="Moderate",
        font= ("Minecraft", 14),
        width=15,
        command=lambda: startQuiz("Moderate")
        )
    moderateButton.grid(row=3, column=0, pady=20)

    advancedButton = Button(
        menuFrame,
        text="Advanced",
        font= ("Minecraft", 14),
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
    for widget in quizFrame.winfo_children():
        widget.destroy()
    attempts = 0
    questionNumber += 1
    questionCounterLabel = Label(
        quizFrame,
        text=f"Question{questionNumber}/10",
        font=("Minecraft",14)
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
        font=("Minecraft", 22) 
    )
    questionLabel.grid(row=4, column=0, pady=10)
    
    scoreLabel = Label(
        quizFrame,
        text=f"Score: {score}",
        font=("Minecraft",14)
      
    )
    scoreLabel.grid(row=5, column=0, pady=20)

    answerEntry = Entry(
        quizFrame,
        font=("Minecraft", 16),
        width=10
    )
    answerEntry.grid(row=6, column=0, pady=10)
    
    resultLabel = Label(
        quizFrame,
        text = "",
        font=("Minecraft", 14)
    )
    resultLabel.grid(row=8, column=0, pady=10)

    submitButton = Button(
            quizFrame,
            text="Submit",
            font=("Minecraft", 14),
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
            nextQuestion()

def nextQuestion():
    if questionNumber >=10:
        displayResults()
    else:
        displayProblem(difficulty)
    

def displayResults():
    quizFrame.grid_remove()
    resultsFrame.grid()
    resultsFrame.tkraise()
    
    for widget in resultsFrame.winfo_children():
        widget.destroy()
    
    resultsLabel = Label(
        resultsFrame,
        text ="QUIZ FINISHED!",
        font=("Minecraft", 22),
         bg="#926c4d"
    )
    resultsLabel.grid(row=0, column=0, pady=20)
    
    finalScoreLabel = Label(
        resultsFrame,
        text=f"Final Score {score}/100",
        font=("Minecraft", 18),
        bg = "#926c4d"
    )
    finalScoreLabel.grid (row=1, column=0, pady=10)
    
    gradeLabel = Label(
        resultsFrame,
        text=f"Grade: {calculateGrade()}",
        font=("Minecraft", 18),
        bg="#926c4d"
    )
    gradeLabel.grid(row=2, column=0, pady=10)
    
    playAgainButton = Button(
        resultsFrame, 
        text= "Play Again?",
        font=("Minecraft", 14),
        width =15,
        command=playAgain
    )
    playAgainButton.grid(row=3, column=0, pady =10)
    
    exitButton = Button(
        resultsFrame,
        text= "Leave",
        font=("Minecraft", 14),
        width=15,
        command=root.destroy
    )
    exitButton.grid(row=4, column =0, pady=10)
    
    
def calculateGrade():
    if score > 90:
        return "A+"
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"
    
    
def playAgain():
    global score, attempts, questionNumber
    
    score = 0
    attempts = 0
    questionNumber = 0
    
    resultsFrame.grid_remove()
    menuFrame.tkraise()
    
displayMenu()
root.mainloop()   
from tkinter import *
from random import randint
from PIL import ImageTk, Image
score = 0
attempts = 0
difficulty = ""
questionNumber = 0
question_finished = False


root= Tk()
root.geometry("700x500")
root.resizable(0,0)
root.title("Math Quiz")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)


# Frames Switching
menuFrame = Frame(root,)
menuFrame.grid(row=0, column=0, sticky="nsew")
menuFrame.grid_columnconfigure(0, weight=1)

# QUIZ FRAME
quizFrame = Frame(root,)
quizFrame.grid(row=0, column=0, sticky="nsew")
quizFrame.grid_columnconfigure(0, weight=1)

# RESULTS FRAME
resultsFrame = Frame(root,)
resultsFrame.grid(row=0, column=0, sticky="nsew")
resultsFrame.grid_columnconfigure(0, weight=1)
resultsFrame.grid_remove()
menuFrame.tkraise()

resultsFrame.grid_remove()

# Backround Image
bgImage = Image.open("images/DirtBackround.jpg")
bgImage = bgImage.resize((700, 500))
bgPhoto = ImageTk.PhotoImage(bgImage)

bgLabel = Label(menuFrame, image=bgPhoto, borderwidth=0)
bgLabel.image = bgPhoto
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
bgLabel.lower()

quizBgLabel = Label(quizFrame, image= bgPhoto, borderwidth=0)
quizBgLabel.image = bgPhoto
quizBgLabel.place(x=0, y=0, relwidth=1, relheight=1)

resultBgLabel= Label(resultsFrame, image=bgPhoto, borderwidth=0)
resultBgLabel.image = bgPhoto
resultBgLabel.place(x=0, y=0, relwidth=1, relheight=1)


menuFrame.tkraise()

# Difficulty Menu
def displayMenu():
   
    headingLabel = Label(
        menuFrame,
        text="Math Quiz",
        font=("Minecraft", 30),
        bg="white",
        fg="black"
        
    )
    headingLabel.grid(row=0, column=0, pady=(60, 20))

    difficultyLabel = Label(
        menuFrame,
        text="Select Difficulty",
        font= ("Minecraft", 20),
        bg="white",
        fg="black"
    )
    difficultyLabel.grid(row=1, column=0, pady=10)

    easyButton = Button(
        menuFrame,
        text="Easy",
        font= ("Minecraft", 14),
        width=18,
        bg="#777777",
        fg="white",
        relief= RAISED,
        bd=5,
        command=lambda: startQuiz("Easy")
        )
    easyButton.grid(row=2, column=0, pady=8)

    moderateButton = Button(
        menuFrame,
        text="MEDIUM",
        font= ("Minecraft", 14),
        width=18,
        bg="#777777",
        fg="white",
        relief=RAISED,
        bd=5,
        command=lambda: startQuiz("Moderate")
        )
    moderateButton.grid(row=3, column=0, pady=20)

    advancedButton = Button(
        menuFrame,
        text="HARD",
        font= ("Minecraft", 14),
        width=18,
        bg="#777777",
        fg="white",
        bd=5,
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

# Display Problem (Questions) 
def displayProblem(difficulty):
    global attempts, questionNumber
    for widget in quizFrame.winfo_children():
        if widget is not quizBgLabel:
            widget.destroy()
   

    attempts = 0
    questionNumber += 1

    number1 = randomInt(difficulty)
    number2 = randomInt(difficulty)
    operation = decideOperation()

    if operation == "+":
        correctAnswer = number1 + number2
    elif operation == "-":
        correctAnswer = number1 - number2
        
    # MATH QUESTIONAIRE
    questionLabel = Label(
        quizFrame,
        text=f"{number1} {operation} {number2} = ?",
        font=("Minecraft", 24),
        bg="white",
        fg="black"
    )
    questionLabel.grid(row=1, column=0, pady=15)

    # Question Counter
    questionCounterLabel = Label(
        quizFrame,
        text=f"QUESTION {questionNumber}/10",
        font=("Minecraft", 14),
        bg="white",
        fg="#26351c"
    )
    questionCounterLabel.grid(row=0, column=0, pady=(40, 20))
    
    
    # Score function
    scoreLabel = Label(
        quizFrame,
        text=f"SCORE: {score}",
        font=("Minecraft",14),
        bg="white",
        fg="#26351c"
      
    )
    scoreLabel.grid(row=2, column=0, pady=20)

    # Answer Box
    answerEntry = Entry(
        quizFrame,
        font=("Minecraft", 16),
        width=15,
        justify="center"
    )
    answerEntry.grid(row=3, column=0, pady=15)
    
    # Result Message
    resultLabel = Label(
        quizFrame,
        text = "",
        font=("Minecraft", 12),
        bg="white",
        fg="black"
        
    )
    resultLabel.grid(row=5, column=0, pady=10)

    submitButton = Button(
            quizFrame,
            text="SUBMIT",
            font=("Minecraft", 14),
            width=25,
            height = 2,
            bg="#777777",
            fg="white",
            relief=RAISED,
            bd=5,
            command=lambda: submit_answer(
                answerEntry,
                correctAnswer,
                resultLabel,
                scoreLabel
            )
    )
    submitButton.grid(row=4, column=0, pady=30)
    
def submit_answer(answerEntry, correctAnswer, resultLabel, scoreLabel):
    user_input = answerEntry.get()
    try:
        userAnswer = int(user_input)
        isCorrect(userAnswer, correctAnswer, resultLabel, scoreLabel)
    except ValueError:
        resultLabel.config(text="Please enter a valid number!")
    

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
    for widget in resultsFrame.winfo_children():
        if widget is not resultBgLabel:
            widget.destroy()
       
    
    quizFrame.grid_remove()
    resultsFrame.grid()
    resultsFrame.tkraise()
    resultBgLabel.lower()
    
    # Create the results label and buttons
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
        bg= "#777777",
        relief= RAISED,
        bd= 5,
        command=playAgain
    )
    playAgainButton.grid(row=3, column=0, pady =10)
    
    exitButton = Button(
        resultsFrame,
        text= "Leave",
        font=("Minecraft", 14),
        width=15,
        bg="#777777",
        relief= RAISED,
        bd=5,
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
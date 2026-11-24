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

menuCanvas = Canvas(
    menuFrame,
    width=700,
    height=500,
    highlightthickness=0
)
menuCanvas.place(x=0, y=0)

menuCanvas.create_image(
    0,0,
    image=bgPhoto,
    anchor="nw"
)

# Title Text
menuCanvas.create_text(
    350, 80,
    text="Math Quiz",
    font=("Minecraft", 30),
    fill="white"
)
menuCanvas.create_text(
    350, 155,
    text="Select Difficulty",
    font=("Minecraft", 20),
    fill="white"
)

# QUIZ FRAME BACKGROUND
quizCanvas = Canvas(
    quizFrame,
    width=700,
    height=500,
    highlightthickness=0
)
quizCanvas.place(x=0, y=0)

# RESULTS FRAME BACKGROUND
resultsCanvas = Canvas(
    resultsFrame,
    width=700,
    height=500,
    highlightthickness=0
)
resultsCanvas.place(x=0, y=0)

menuCanvas.tk.call("lower", menuCanvas._w)
menuFrame.tkraise()

# Difficulty Menu
def displayMenu():

    # EASY BUTTON
    easyButton = Button(
        menuFrame,
        text="EASY",
        font=("Minecraft", 14),
        width=18,
        bg="#777777",
        fg="white",
        relief=RAISED,
        bd=5,
        command=lambda: startQuiz("Easy")
    )

    menuCanvas.create_window(
        350, 230,
        window=easyButton
    )

    # MEDIUM BUTTON
    moderateButton = Button(
        menuFrame,
        text="MEDIUM",
        font=("Minecraft", 14),
        width=18,
        bg="#777777",
        fg="white",
        relief=RAISED,
        bd=5,
        command=lambda: startQuiz("Moderate")
    )

    menuCanvas.create_window(
        350, 300,
        window=moderateButton
    )

    # HARD BUTTON
    advancedButton = Button(
        menuFrame,
        text="HARD",
        font=("Minecraft", 14),
        width=18,
        bg="#777777",
        fg="white",
        bd=5,
        command=lambda: startQuiz("Advanced")
    )

    menuCanvas.create_window(
        350, 370,
        window=advancedButton
    )



def startQuiz(selectedDifficulty):
    global difficulty, score, attempts, questionNumber
    
    difficulty = selectedDifficulty
    score = 0
    attempts = 0 
    questionNumber = 0
    quizFrame.grid()
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
        if widget is not quizCanvas:
            widget.destroy()

    quizCanvas.delete("all")

    quizCanvas.create_image(
        0, 0,
        image=bgPhoto,
        anchor="nw"
    )

    attempts = 0
    questionNumber += 1

    number1 = randomInt(difficulty)
    number2 = randomInt(difficulty)
    operation = decideOperation()

    if operation == "+":
        correctAnswer = number1 + number2
    elif operation == "-":
        correctAnswer = number1 - number2

    # QUESTION COUNTER
    quizCanvas.create_text(
        350, 70,
        text=f"QUESTION {questionNumber}/10",
        font=("Minecraft", 18),
        fill="white"
    )

    # MATH QUESTION
    quizCanvas.create_text(
        350, 145,
        text=f"{number1} {operation} {number2} = ?",
        font=("Minecraft", 24),
        fill="white"
    )

    # SCORE
    scoreText = quizCanvas.create_text(
        350, 210,
        text=f"SCORE: {score}",
        font=("Minecraft", 18),
        fill="white"
    )

    # ANSWER BOX
    answerEntry = Entry(
        quizFrame,
        font=("Minecraft", 16),
        width=15,
        justify="center"
    )

    quizCanvas.create_window(
        350, 270,
        window=answerEntry
    )

    # RESULT MESSAGE
    resultText = quizCanvas.create_text(
        350, 325,
        text="",
        font=("Minecraft", 14),
        fill="white"
    )

    # SUBMIT BUTTON
    submitButton = Button(
        quizFrame,
        text="SUBMIT",
        font=("Minecraft", 14),
        width=25,
        height=2,
        bg="#777777",
        fg="white",
        relief=RAISED,
        bd=5,
        command=lambda: submit_answer(
            answerEntry,
            correctAnswer,
            resultText,
            scoreText
        )
    )

    quizCanvas.create_window(
        350, 405,
        window=submitButton
    )

    
def submit_answer(answerEntry, correctAnswer, resultText, scoreText):
    user_input = answerEntry.get()

    try:
        userAnswer = int(user_input)

        isCorrect(
            userAnswer,
            correctAnswer,
            resultText,
            scoreText
        )

    except ValueError:
        quizCanvas.itemconfig(
            resultText,
            text="Please enter a valid number!"
        )
    

def isCorrect(userAnswer, correctAnswer, resultText, scoreText):
    global score, attempts
   
    if userAnswer == correctAnswer:
        if attempts == 0:
            score += 10
            quizCanvas.itemconfig(
                resultText,
                text="Correct! +10 Points"
            )
        else:
            score += 5
            quizCanvas.itemconfig(
                resultText,
                text="Correct! +5 Points"
            )
        quizCanvas.itemconfig(
            scoreText,
            text=f"SCORE: {score}"
        )
        nextQuestion()

    else:
        attempts += 1

        if attempts == 1:
            quizCanvas.itemconfig(
                resultText,
                text="Incorrect! Try Again"
            )
        else:
            quizCanvas.itemconfig(
                resultText,
                text="No more Attempts :("
            )

            nextQuestion()

def nextQuestion():
    if questionNumber >=10:
        displayResults()
    else:
        displayProblem(difficulty)
    


def displayResults():

    for widget in resultsFrame.winfo_children():
        if widget is not resultsCanvas:
            widget.destroy()

    resultsCanvas.delete("all")

    resultsCanvas.create_image(
        0, 0,
        image=bgPhoto,
        anchor="nw"
    )

    quizFrame.grid_remove()
    resultsFrame.grid()
    resultsFrame.tkraise()

    # RESULTS TITLE
    resultsCanvas.create_text(
        350, 90,
        text="QUIZ FINISHED!",
        font=("Minecraft", 26),
        fill="white"
    )

    # FINAL SCORE
    resultsCanvas.create_text(
        350, 165,
        text=f"Final Score: {score}/100",
        font=("Minecraft", 20),
        fill="white"
    )

    # GRADE
    resultsCanvas.create_text(
        350, 220,
        text=f"Grade: {calculateGrade()}",
        font=("Minecraft", 20),
        fill="white"
    )

    # PLAY AGAIN BUTTON
    playAgainButton = Button(
        resultsFrame,
        text="Play Again?",
        font=("Minecraft", 14),
        width=15,
        bg="#777777",
        fg="white",
        relief=RAISED,
        bd=5,
        command=playAgain
    )

    resultsCanvas.create_window(
        350, 310,
        window=playAgainButton
    )

    # EXIT BUTTON
    exitButton = Button(
        resultsFrame,
        text="Leave",
        font=("Minecraft", 14),
        width=15,
        bg="#777777",
        fg="white",
        relief=RAISED,
        bd=5,
        command=root.destroy
    )

    resultsCanvas.create_window(
        350, 380,
        window=exitButton
    )

    
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
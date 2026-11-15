from tkinter import *
from random import randint

root = Tk()
root.geometry("500x500")
root.title("Math Quiz")

root.grid_columnconfigure(0, weight=1)
headingLabel = Label(root, text="Math Quiz", font=("Roboto", 18))
headingLabel.grid(row=0, column=0,pady=10, sticky="ew")

number1 = randint(1, 20) 
number2 = randint(1, 20)


question = str(number1) + " + " + str(number2)
question = str(number1) + " * " + str(number2)
answer = number1 + number2
answer = number1 * number2

def checkAnswer():
    if answer == int(givenAnswer.get()):
        print("Correct!")
    else:
        print("Incorrect!")

givenAnswer = StringVar()
    

# Menu Frame
menuFrame = Frame(root)
menuFrame.grid(row=0, column=0)

headingLabel = Label1(
    menuFrame, text="Math Quiz", font=("Roboto", 22)
)
headingLabel.grid(row=0, column=0, pady=20)

difficultyLabel = Label1(
    menuFrame, text="Select Difficulty Level", font=("Roboto", 16)
)
difficultyLabel.grid(row=1, column=0, pady=10)

print(question)
print(answer)

root.mainloop()
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
answer = number1 + number2

def checkAnswer():
    if answer == int(givenAnswer.get()):
        print("Correct!")
    else:
        print("Incorrect!")

givenAnswer = StringVar()
    

# GUI
questionLabel= Label(root, text=question, font=("Roboto", 14))
questionLabel.grid(row=1, column=0,)

answerentry = Entry(root, textvariable=givenAnswer, font=("Roboto", 14))
answerentry.grid(row=2, column=0, pady=10)

submitButton = Button(root, text="Submit", font=("Roboto", 14), command=checkAnswer)
submitButton.grid(row=3, column=0, pady=20,)

print(question)
print(answer)

root.mainloop()
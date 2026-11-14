from tkinter import *
from random import randint

root = Tk()
root.geometry("500x500")
root.title("Math Quiz")

headingLabel = Label(root, text="Math Quiz", font=("Roboto", 18))
headingLabel.pack(pady=10)

number1 = randint(1, 20) 

print(number1)

root.mainloop()
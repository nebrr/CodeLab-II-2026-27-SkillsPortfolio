from tkinter import *

root= Tk()
root.geometry("500x500")
root.title("Math Quiz")
root.grid_columnconfigure(0, weight=1)

#Difficulty Menu
def displayMenu():
    headingLabel = Label(
        root,
        text="Math Quiz",
        font= ("Roboto, 22")
    )
    headingLabel.grid(row=0, column=0, pady=20)     

difficultyLabel = Label(
    root,
    text="Select Difficulty",
    font= ("Roboto, 16")
)
difficultyLabel.grid(row=1, column=0, pady=10)

easyButton = Button(
    root,
    text="Easy",
    font= ("Roboto, 14"),
    width=15,)
easyButton.grid(row=2, column=0, pady=5)

moderateButton = Button(
    root,
    text="Moderate",
    font= ("Roboto, 14"),
    width=15,)
moderateButton.grid(row=3, column=0, pady=5)

advancedButton = Button(
    root,
    text="Advanced",
    font= ("Roboto, 14"),
    width=15,)
advancedButton.grid(row=4, column=0, pady=5)



displayMenu()
root.mainloop()    
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

displayMenu()
root.mainloop()    
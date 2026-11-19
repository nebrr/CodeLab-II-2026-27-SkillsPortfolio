from tkinter import *
from random import choice
root = Tk()

root.title ("JoJOKE")
root.geometry("500x400")
root['bg'] = '#926c4d'


# ALL THE FRAME
titleFrame = Frame(
    root,
    bg='#926c4d'
    )
titleFrame.pack(pady=10)

jokeFrame = Frame(
    root, 
    bg= '#f5e6d3'
    )
jokeFrame.pack(
    pady=10,
    padx=20,
    fill='both',
    expand=True
    )

titleLabel = Label(
    titleFrame,
    text = "JoJOKE",
    font=("Minecraft", 24, "bold"),
    bg="#926c4d",
    fg="white"
)
titleLabel.pack()

subtitleLabel = Label(
    titleFrame,
    text = "Wanna heat a Joke?",
    font = ("Minecraft", 15),
    bg="#926c4d",
    fg="white"
)
subtitleLabel.pack()

jokeLabel = Label(
    jokeFrame,
    text= "Your Jojoke appears here!",
    font= ("Minecraft", 14, "bold"),
    bg="#f5e6d3",
    fg="#4a3425",
    wraplength=400
)
jokeLabel.pack(pady = 30)

punchlineLabel = Label(
    jokeFrame,
    text="yoohoo dito ang tingin",
    font=("Minecraft", 12),
    bg="#f5e6d3",
    fg="#926c4d",
    wraplength=400
)
punchlineLabel.pack(pady=10)
 
 # BUTTONS
buttonFrame = Frame(
    jokeFrame,
    bg="#f5e6d3"
)
buttonFrame.pack(pady=20)
buttonFrame.grid_columnconfigure(0, weight=1)
buttonFrame.grid_columnconfigure(1, weight=1)


jokeButton = Button(
    buttonFrame,
    text = "Sure tell me the joke",
    font=("Minecraft",13),
    bg="#926c4d",
    fg="white"
)
jokeButton.grid(row=0, column=0, padx=15,pady=15)

punchlineButton = Button(
    buttonFrame,
    text="Hmm.. idk what is it?",
    font=("Minecraft", 13),
    bg="#926c4d",
    fg="white"
)
punchlineButton.grid(row=0, column=1, padx=15, pady=15)

nextButton = Button(
    buttonFrame,
    text="Another one",
    font=("Minecraft", 13),
    bg="#926c4d",
    fg="white"
)
nextButton.grid(row=1, column=0, padx=15, pady=15)

quitButton = Button(
    buttonFrame,
    text="Ok.. enough",
    font=("Minecraft", 12),
    bg="#926c4d",
    fg="white"
)
quitButton.grid(row=1, column=1, padx=15, pady=15)

    
    
root.mainloop()
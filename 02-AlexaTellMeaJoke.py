from tkinter import *
from random import choice

with open("Resources/randomJokes.txt", "r", encoding='utf-8') as file:
    jokes = file.readlines() # This reads all of the lines of the txt file
punchline_text = [""]

root = Tk()
root.title ("JoJOKE")
root.geometry("500x400")
root['bg'] = '#926c4d'

# Generates and choose random joke from the txt file
def genJoke():
    selected_joke = choice(jokes).strip()
    question, punchline = selected_joke.split("?",1)
    
    punchline_text[0] = punchline
    
    jokeLabel.config(text=question + "?")
    punchlineLabel.config(text="")

# This function is to show the punchline when the button is pressed
def revealPunchline():
   # this prevents the blank response when the button is pressed 
    if punchline_text[0]=="":
       punchlineLabel.config(text="I didn't even say the joke yet!")
    else:
       punchlineLabel.config(text=punchline_text[0])
    
# MAIN FRAME 
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
# MAIN TITLE
titleLabel = Label(
    titleFrame,
    text = "JoJOKE",
    font=("Minecraft", 24, "bold"),
    bg="#926c4d",
    fg="white"
)
titleLabel.pack()
# SUB TEXT BELOW THE TITLE
subtitleLabel = Label(
    titleFrame,
    text = "Wanna hear a Joke?",
    font = ("Minecraft", 15),
    bg="#926c4d",
    fg="white"
)
subtitleLabel.pack()
# JOKE LABEL 
jokeLabel = Label(
    jokeFrame,
    text= "Your Jojoke appears here!",
    font= ("Minecraft", 14, "bold"),
    bg="#f5e6d3",
    fg="#4a3425",
    wraplength=400
)
jokeLabel.pack(pady = 30)

# PUNCHLINE LABEL (Text)
punchlineLabel = Label(
    jokeFrame,
    text="Punchline appears here",
    font=("Minecraft", 12),
    bg="#f5e6d3",
    fg="#926c4d",
    wraplength=400
)
punchlineLabel.pack(pady=10)
 
 # BUTTONS SECTION
buttonFrame = Frame(
    jokeFrame,
    bg="#f5e6d3"
)
buttonFrame.pack(pady=20)
buttonFrame.grid_columnconfigure(0, weight=1)
buttonFrame.grid_columnconfigure(1, weight=1)

# BUTTON TO GENERATE THE JOKE
jokeButton = Button(
    buttonFrame,
    text = "Sure tell me the joke",
    font=("Minecraft",13),
    bg="#926c4d",
    fg="white",
    command=genJoke
)
jokeButton.grid(row=0, column=0, padx=15,pady=15)

# SHOWS THE PUNCHLINE
punchlineButton = Button(
    buttonFrame,
    text="Hmm.. idk what is it?",
    font=("Minecraft", 13),
    bg="#926c4d",
    fg="white",
    command=revealPunchline
)
punchlineButton.grid(row=0, column=1, padx=15, pady=15)
 # NEXT JOKE
nextButton = Button(
    buttonFrame,
    text="Another one",
    font=("Minecraft", 13),
    bg="#926c4d",
    fg="white",
    command= genJoke
)
nextButton.grid(row=1, column=0, padx=15, pady=15)

# QUIT BUTTON
quitButton = Button(
    buttonFrame,
    text="Ok.. enough",
    font=("Minecraft", 12),
    bg="#926c4d",
    fg="white",
    command = root.destroy
)
quitButton.grid(row=1, column=1, padx=15, pady=15)

    
    
root.mainloop()
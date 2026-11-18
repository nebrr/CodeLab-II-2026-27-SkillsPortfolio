from tkinter import*
root = Tk()
root.title("JoJoke")
root.geometry("500x300")

title_label = Label(
    text="JoJoke", 
    font=("Roboto", 16, "bold")
)
title_label.pack(pady=10)

setup_label= Label(root,
text="Wanna hear a Joke?",
font=("Roboto",12),
wraplength= 450
)
setup_label.pack(pady=15)
root.mainloop()

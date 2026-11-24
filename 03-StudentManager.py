from tkinter import * 
root = Tk()
root.title("Student Records")
root.geometry("700x500")
root.config(bg="#263445")

# Main Menu Frame
menuFrame = Frame(root,bg = "#263445" )
menuFrame.pack(fill="both", expand =True)

# Result Frame
resultsFrame = Frame( root,bg="#263445")
resultsFrame.pack(fill="both", expand= True)

# Search Frame 
searchFrame = Frame( root,bg="#263445")
searchFrame.pack( fill="both",  expand = True)

#Main Menu Title
titleLabel = Label(
    menuFrame,
    text = "STUDENT RECORDS",
    font = ("Roboto", 24, "bold"),
    bg="#263445",
    fg="white"
)
titleLabel.pack(pady=20)

#Subtext
subtextLabel = Label(
    menuFrame,
    text = "Student Marks Management System",
    font = ("Roboto", 12),
    bg="#263445",
    fg="white"
)
subtextLabel.pack(pady=5)

# View All Records
viewAllButton = Button(
    menuFrame,
    text = "View All Students Records",
    font= ("roboto", 12),
    width=30
)
viewAllButton.pack(pady=8)

# view individual Student
viewStudentButton = Button(
    menuFrame,
    text = "View Individual Student",
    font =("Roboto", 12),
    width = 30
)
viewStudentButton.pack(pady=8)

# Highest OVR Mark
highestOVRButton = Button(
    menuFrame,
    text = "Highest Overall Mark",
    font =("Roboto", 12),
    width = 30
)
highestOVRButton.pack (pady = 8)

# Lowest OVR Mark
LowButton = Button(
    menuFrame,
    text= "Lowest Overall Mark",
    font=("Roboto", 12),
    width= 30
)
LowButton.pack(pady=8)

# Exit Button
ExitButton = Button(
    menuFrame,
    text ="Exit",
    font = ("Roboto", 12),
    width=30,
    command=root.destroy 
)
ExitButton.pack(pady=8)
root.mainloop()
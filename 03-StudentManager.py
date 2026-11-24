from tkinter import * 
from tkinter import ttk
import json
root = Tk()
root.title("Student Records")
root.geometry("700x500")
root.config(bg="#263445")

# Main Menu Frame
menuFrame = Frame(root,bg = "#263445" )
menuFrame.pack(fill="both", expand =True)

# Result Frame
resultsFrame = Frame( root,bg="#263445")


# Search Frame 
searchFrame = Frame( root,bg="#263445")


#  ==============STUDENT TABLE===========

colulmns = ("Name", "Student Number", "Coursework", "Exam", "Percentage", "Grade")
table = ttk.Treeview(
    resultsFrame,
    columns=colulmns,
    show="headings"
)
for col in colulmns:
    table.heading(col, text=col)   

table.pack(fill="both", expand=True)

#====== Main Menu  ==========
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
    width=30,
    command = lambda: (
        menuFrame.pack_forget(),
        resultsFrame.pack(fill="both", expand=True),
        displayRecords()
    )
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

backButton = Button(
    resultsFrame,
    text="Back to Menu",
    font= ("Roboto", 12),
    command= lambda: (
        resultsFrame.pack_forget(),
        menuFrame.pack(fill="both", expand=True)
    )
)
backButton.pack(pady=10)

# ========== FUNCTIONS ============
def calculateGrade(percent):
    if percent >= 70:
        return "A"
    
    elif percent >= 60:
        return "B"
    
    elif percent >= 50:
        return "C"
    
    elif percent >= 40:
        return "D"
    
    else:
        return "F"

# ========== STUDENT ROW ==============
def addRow(name, num, marks, exam_marks):
    coursework_total = sum(marks)
    
    percent = (coursework_total + exam_marks)/ 160 * 100
    
    grade = calculateGrade(percent)
    
    values = (name,num, coursework_total,exam_marks, f"{percent:.1f}%", grade)
    table.insert("",END, values=values)

# ========= DISPLAY ALL RECORDS ============
def displayRecords():
    for row in table.get_children():
        table.delete(row)

    with open ("Resources/studentMarks.json", "r") as file:
        data = json.load(file)
    students = data["students"]
    
    for student in students:
        marks = [
            student["coursework1"],
            student["coursework2"],
            student["coursework3"]
        ]
        
        addRow(
            student["name"],
            student["studentNumber"],
            marks,
            student["examMark"]
        )

root.mainloop()
from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
# -------------------------
# Window setup
# -------------------------
root = Tk()
root.title('CCSU Mobile App')
root.geometry("700x400")
root.resizable(0, 0)
root.configure(bg='light blue')
# -------------------------
# Load and display logo
# -------------------------
logo_file = 'logo1.PNG' # make sure this matches your file name
img = Image.open(logo_file)
try:
img = img.resize((100, 100), Image.Resampling.LANCZOS)
except AttributeError:
img = img.resize((100, 100), Image.ANTIALIAS)
img = img.convert("RGBA")
data = img.getdata()
newData = []
for item in data:
if item[:3] == (255, 255, 255):
newData.append((255, 255, 255, 0))
else:
newData.append(item)
img.putdata(newData)
img.save("transparent.png")
logo = Image.open("transparent.png")
logo = ImageTk.PhotoImage(logo)
logoLabel = Label(root, image=logo, bg='light blue')
logoLabel.place(x=10, y=10)
# -------------------------
# Load CSV data
# -------------------------
data = pd.read_csv("midterm_exam.csv")
# -------------------------
# Label to display results
# -------------------------
lb = Label(root, justify="left", bg="light blue", anchor="w")
lb.place(x=130, y=150)
# -------------------------
# Button functions
# -------------------------
def calendar():
df = pd.DataFrame(data, columns=['CalendarDate'])
selected_rows = df[~df['CalendarDate'].isnull()]
lb.config(text=selected_rows.to_string(index=False))
def buildings():
df = pd.DataFrame(data, columns=['Buildings'])
selected_rows = df[~df['Buildings'].isnull()]
lb.config(text=selected_rows.to_string(index=False))
def faculty():
df = pd.DataFrame(data, columns=['FacultyName'])
selected_rows = df[~df['FacultyName'].isnull()]
lb.config(text=selected_rows.to_string(index=False))
def school_of_business():
courses = ["Accounting", "Finance", "Management & Organization",
"Marketing", "MIS", "Business Analytics"]
lb.config(text="\n".join(courses))
def mis_department():
courses = ["Intro to MIS", "Databases Management", "Systems Analysis & Design",
"Business Analytics / Data Visualization", "Network and Information Security",
"Project Management"]
lb.config(text="\n".join(courses))
# -------------------------
# Buttons
# -------------------------
button1 = Button(root, text='Calendar', command=calendar, bg="light green")
button1.place(x=50, y=120)
button2 = Button(root, text='Buildings', command=buildings, bg="light green")
button2.place(x=150, y=120)



button3 = Button(root, text='Faculty', command=faculty, bg="light green")
button3.place(x=250, y=120)
button4 = Button(root, text='School of Business', command=school_of_business, bg="light green")
button4.place(x=350, y=120)
button5 = Button(root, text='MIS Department', command=mis_department, bg="light green")
button5.place(x=520, y=120)
# -------------------------
root.mainloop()

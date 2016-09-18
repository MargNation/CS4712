from Tkinter import *

# Create Window
master = Tk()
master.title("Harriman Calculator")

# Create variable to display real time results
global current_answer
current_answer = StringVar()
current_answer.set("0.00")

# This will be where the results are displayed
Label(master, textvariable=current_answer, font=("Helvetica", 15)).grid(row=0, column=6, padx=14, pady=8)

# Create boxes to receive user input
first_term = Entry(master, width=5, borderwidth=5)
second_term = Entry(master, width=5, borderwidth=5)
first_term.grid(row=1, column=3, padx=25, pady=8, sticky=E)
second_term.grid(row=1, column=4, sticky=E)

# Create the functions each button will perform
def clear():
	current_answer.set("0.00")

def add():
	current_answer.set('{0:.2f}'.format(float(first_term.get()) + int(second_term.get())))

def subtract():
	current_answer.set('{0:.2f}'.format(float(first_term.get()) - int(second_term.get())))

def multiply():
	current_answer.set('{0:.2f}'.format(float(first_term.get()) * int(second_term.get())))

def divide():
	current_answer.set('{0:.2f}'.format(float(first_term.get()) / int(second_term.get())))

# Create buttons for calculator
Button(master, text="Clear", width=7, command=clear).grid(row=3, column=4, pady=8)
Button(master, text="+", width=4, command=add).grid(row=4, column=3, pady=8)
Button(master, text="-", width=4, command=subtract).grid(row=4, column=4, pady=8)
Button(master, text="*", width=4, command=multiply).grid(row=5, column=3, pady=8)
Button(master, text="/", width=4, command=divide).grid(row=5, column=4, pady=8)

# Run Window
mainloop()
from Tkinter import *

# Create Window
master = Tk()
master.title("Margaret Harriman  10-22-2016")

# Change background to black
master.configure(bg='Black')

# Create appropriate labels, change colors to Gold for KSU
Label(master, text="To:", bg='Black', fg='Gold').grid(row=0, padx=14, pady=8, sticky=E)
Label(master, text="From:", bg='Black', fg='Gold').grid(row=1, padx=14, pady=8, sticky=E)
Label(master, text="Subject:", bg='Black', fg='Gold').grid(row=2, padx=14, pady=8, sticky=E)
Label(master, text="Message", bg='Black', fg='Gold').grid(row=4, padx=14, pady=8, sticky=N)

# Create boxes to receive text at each label
to_field = Text(master, height=1, width=35)
from_field = Text(master, height=1, width=35)
subject = Text(master, height=1, width=35)
message = Text(master, height=20, width=35)

# Align elements on a grid
to_field.grid(row=0, column=1)
from_field.grid(row=1, column=1, sticky=W)
subject.grid(row=2, column=1)
message.grid(row=4, column=1)

# Create functions for each button
def connecting():
	# If any of the pertinent text fields are empty, print a warning message
	if (len(to_field.get("1.0", END)) == 1):
		print "Please enter a recipient"
	elif (len(from_field.get("1.0", END)) == 1):
		print "Please enter your email address in the From field"
	elif (len(subject.get("1.0", END)) == 1):
		print "Please enter a subject"
	else:
		window = Toplevel(master)
		sendEmail = Text(window, height=5, width=50, background="Black", foreground="White")
		sendEmail.pack()
		sendEmail.insert(END, "Sending email...")
		sendEmail.after(1000, lambda: sendEmail.quit())
		print "Your message has been sent."

def close():
	print "\nEmail Application Canceled"
	master.quit()

def help():
	window = Toplevel(master)
	helpText = Text(window, height=5, width=50, background="Black", foreground="White")
	helpText.pack()
	helpText.insert(END, "\nGo to www.kennesaw.edu for help topics.")
	# master.quit()

# Create buttons
Button(master, text="Send!", width=9, command=connecting, bd=5, bg='Black', fg='Gold').grid(row=25, column=0)
Button(master, text="Cancel", width=9, command=close, bd=5, bg='Black', fg='Gold').grid(row=25, column=1)
Button(master, text="Help", width=9, command=help, bd=5, bg='Black', fg='Gold').grid(row=25, column=2)

# Run Window
mainloop()
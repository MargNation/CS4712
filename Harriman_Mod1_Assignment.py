from Tkinter import *

# Create Window
master = Tk()
master.title("Margaret Harriman  08-27-2016")

# Create appropriate labels
Label(master, text="IP Address").grid(row=0, padx=14, pady=8, sticky=W)
Label(master, text="Port").grid(row=1, padx=14, pady=8, sticky=W)
Label(master, text="User Name").grid(row=2, padx=14, pady=8, sticky=W)
Label(master, text="Password").grid(row=3, padx=14, pady=8, sticky=W)

# Create boxes to receive text at each label
ip_addy = Entry(master)
port = Entry(master, width=6)
username = Entry(master)
password = Entry(master)

# Align elements on a grid
ip_addy.grid(row=0, column=1)
port.grid(row=1, column=1, sticky=W)
SSL_check = IntVar()
Checkbutton(master, text="Use SSL", variable=SSL_check).grid(row=1, column=2)
username.grid(row=2, column=1)
password.grid(row=3, column=1)

# Create functions for each button
def connecting():
	print "Now connecting..."
	print "IP Address:", ip_addy.get(), "Port:", port.get()

def close():
	print "END Connection"
	master.quit()

# Create buttons
Button(master, text="Connect", width=9, command=connecting).grid(row=4, column=1)
Button(master, text="Close", width=9, command=close).grid(row=4, column=2)

# Run Window
mainloop()
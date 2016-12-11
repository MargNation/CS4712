from Tkinter import *
import random

# Create Window
class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		self.master.title("Margaret Harriman Mod 6 - 11/6/16")
		radiovar1 = IntVar()
		checkvar1 = IntVar()
		checkvar2 = IntVar()
		checkvar3 = IntVar()
		checkvar4 = IntVar()
		checkvar5 = IntVar()
		checkvar6 = IntVar()
		checkvar7 = IntVar()
		checkvar8 = IntVar()
		checkvar9 = IntVar()
		global size
		global runningTotal
		global checkvars
		global printed_receipt
		printed_receipt = ""
		displayTotal = StringVar()

		for r in range(20):
			self.master.rowconfigure(r)
		for c in range(5):
			self.master.columnconfigure(c)

		# Print pizza size selection
		def pizzaSize():
			global size
			global runningTotal
			global printed_receipt
			if (radiovar1.get() == 0):
				size = 4.95
				displayTotal.set('{0:.2f}'.format(size))
			elif (radiovar1.get() == 1):
				size = 5.95
				displayTotal.set('{0:.2f}'.format(size))
			else:
				size = 7.25
				displayTotal.set('{0:.2f}'.format(size))
			runningTotal = size

		# Print selected pizza toppings
		def addTopping():
			global size
			global runningTotal
			global checkvars
			global printed_receipt
			checkvars = [checkvar1.get(), checkvar2.get(), checkvar3.get(), checkvar4.get(), checkvar5.get(), checkvar6.get(), checkvar7.get(), checkvar8.get(), checkvar9.get()]
			runningTotal = size + (0.95 * sum(checkvars))
			displayTotal.set('{0:.2f}'.format(runningTotal))

		# Method to print receipt to console
		# Sales tax is added here
		def receipt():
			global size
			global runningTotal
			global checkvars
			global printed_receipt
			runningTotal *= 1.06
			displayTotal.set('{0:.2f}'.format(runningTotal))
			toppings = ["Pepperoni", "Mushroom", "Onion", "Sausage", "Peppers", "Beef", "Tomatoes", "Pineapple", "Anchovies"]
			printed_receipt = ("Your order has been sent!\nYour order number is ")
			printed_receipt += str(order_number)
			printed_receipt += "\n\n"
			printed_receipt += name.get("1.0",END)
			printed_receipt += street_address.get("1.0",END)
			printed_receipt += city.get("1.0",END)
			printed_receipt += zip_code.get("1.0",END)
			printed_receipt += phone_number.get("1.0",END)
			printed_receipt += "\n"
			if (size == 4.95):
				printed_receipt += "Small pizza = $4.95"
				printed_receipt += "\n"
			elif (size == 5.95):
				printed_receipt += "Medium pizza = $5.95"
				printed_receipt += "\n"
			else:
				printed_receipt += "Large pizza = $7.25"
				printed_receipt += "\n"
			printed_receipt += "Toppings @ $0.95 each: "
			for item in range(len(checkvars)):
				if checkvars[item] == 1:
					printed_receipt += toppings[item]
					printed_receipt += "  "
			printed_receipt += "\n\nTotal == "
			printed_receipt += str('{0:.2f}'.format(runningTotal))
			printed_receipt += "\n\nCharged to "
			printed_receipt += payment_method.get("1.0", END)
			printed_receipt += "Ending in "
			printed_receipt += card_number.get("1.12", END)
			printed_receipt += "Exp: "
			printed_receipt += expiry.get("1.0", END)
			print printed_receipt
			app.quit()

		# Method to clear out total, cancel order
		def cancel():
			global printed_receipt
			print "Order Canceled, you have not been charged"
			displayTotal.set('CANCELED')
			app.quit()

		# Lay out all components of order form
		runningTotal = 0
		Frame1 = Frame(master, bg = "#BDB3B1", borderwidth=5, relief=RAISED)
		Frame1.grid(row=0, column=0, rowspan=8, columnspan=3, sticky=W+E+N+S)
		Frame2 = Frame(master, bg="#BDB3B1", borderwidth=5, relief=RAISED)
		Frame2.grid(row=1, column=0, rowspan=8, columnspan=4, sticky=W+E+N+S)
		Frame3 = Frame(master, bg="#BDB3B1", borderwidth=5, relief=RAISED)
		Frame3.grid(row=9, column=0, rowspan=12, columnspan=7, sticky=W+E+N+S)
		Label(master, image=phototop).grid(row=0, column=0, sticky=E)
		Label(master, image=phototop).grid(row=0, column=1, sticky=E)
		Label(master, image=phototop).grid(row=0, column=2, sticky=E)
		Label(master, image=phototop).grid(row=0, column=3, sticky=E)
		Label(master, text="Order Number:", bd = 12, bg='#F93109', fg='#fff', font=("Helvetica", 16)).grid(row=1, column=2, padx=14, pady=8, sticky=W)
		Label(master, text=order_number, bg='#F93109', fg='#fff', font=("Helvetica", 16)).grid(row=1, column=2, padx=14, pady=8, sticky=E)
		Label(master, text="Pizza Guys Order Form", bg='#F93109', fg='#fff', bd=12, font=("Helvetica", 16)).grid(row=1, padx=14, pady=8, sticky=W)
		Label(master, text="Name:", bg='#D8CAC8', fg='#000').grid(row=2, padx=14, pady=8, sticky=E)
		Label(master, text="Customer Info", borderwidth=5, relief=RAISED, bg='#ffffff', fg='#000', font=("Helvetica", 14)).grid(row=2, column=0, padx=14, pady=8, sticky=W)
		Label(master, text="Street Address:", bg='#D8CAC8', fg='#000').grid(row=3, padx=14, pady=8, sticky=NE)
		Label(master, text="City:", bg='#D8CAC8', fg='#000').grid(row=4, padx=14, pady=8, sticky=E)
		Label(master, text="Zip:", bg='#D8CAC8', fg='#000').grid(row=5, padx=14, pady=8, sticky=E)
		Label(master, text="Phone Number:", bg='#D8CAC8', fg='#000').grid(row=6, padx=14, pady=8, sticky=E)

		# Create boxes to receive text at each label
		name = Text(master, height=1, width=25)
		street_address = Text(master, height=3, width=25)
		city = Text(master, height=1, width=25)
		zip_code = Text(master, height=1, width=8)
		phone_number = Text(master, height=1, width=15)

		# Align elements on a grid
		name.grid(row=2, column=1, sticky=W)
		street_address.grid(row=3, column=1, sticky=W)
		city.grid(row=4, column=1, sticky=W)
		zip_code.grid(row=5, column=1, sticky=W)
		phone_number.grid(row=6, column=1, sticky=W)

		Label(master, text="Build Your Pizza",  borderwidth=5, relief=RAISED, bg='#ffffff', fg='#000', font=("Helvetica", 14)).grid(row=2, column=2, padx=14, pady=8)
		Label(master, text="Pizza Size",  borderwidth=5, relief=RAISED, bg='#ffffff', fg='#000', font=("Helvetica", 12)).grid(row=3, column=2, padx=14, pady=8, sticky=W)

		# Create pizza size options
		for i in range(3):
			textvals = ["Small", "Medium", "Large"]
			positions = [W, "", E]
			Radiobutton(master, text=textvals[i], value=i, variable=radiovar1, indicatoron=0, command=pizzaSize).grid(row=4, column=2, padx=14, pady=8, sticky=positions[i])

		Label(master, text="Toppings",  borderwidth=5, relief=RAISED, bg='#ffffff', fg='#000', font=("Helvetica", 12)).grid(row=5, column=2, padx=14, pady=8, sticky=W)

		# Create pizza toppings options
		Checkbutton(master, text="Pepperoni", variable=checkvar1, command=addTopping).grid(row=6, column=2, padx=5, pady=8, sticky=W)
		Checkbutton(master, text="Mushroom", variable=checkvar2, command=addTopping).grid(row=6, column=2, padx=5, pady=8)
		Checkbutton(master, text="Onion", variable=checkvar3, command=addTopping).grid(row=6, column=2, padx=5, pady=8, sticky=E)
		Checkbutton(master, text="Sausage", variable=checkvar4, command=addTopping).grid(row=7, column=2, padx=5, pady=8, sticky=W)
		Checkbutton(master, text="Peppers", variable=checkvar5, command=addTopping).grid(row=7, column=2, padx=5, pady=8)
		Checkbutton(master, text="Beef", variable=checkvar6, command=addTopping).grid(row=7, column=2, padx=5, pady=8, sticky=E)

		Label(master, image=photobottom).grid(row=8, column=0)
		Label(master, image=photobottom).grid(row=8, column=1)

		Label(master, text="Payment Information", borderwidth=5, relief=RAISED, bg='#ffffff', fg='#000', font=("Helvetica", 12)).grid(row=8, column=2, padx=14, pady=8)
		Label(master, text="Coupon Code:", bg='#D8CAC8', fg='#000').grid(row=9,  column=2, padx=14, pady=8, sticky=W)
		Label(master, text="Payment Method:", bg='#D8CAC8', fg='#000').grid(row=10,  column=2, padx=14, pady=8, sticky=W)
		Label(master, text="Credit Card #:", bg='#D8CAC8', fg='#000').grid(row=11,  column=2, padx=14, pady=8, sticky=W)
		Label(master, text="Expiration Date:", bg='#D8CAC8', fg='#000').grid(row=12,  column=2, padx=14, pady=8, sticky=W)

		coupon = Text(master, height=1, width=15)
		payment_method = Text(master, height=1, width=15)
		card_number = Text(master, height=1, width=18)
		expiry = Text(master, height=1, width=8)

		coupon.grid(row=9, column=2, sticky=E)
		payment_method.grid(row=10, column=2, sticky=E)
		card_number.grid(row=11, column=2, sticky=E)
		expiry.grid(row=12, column=2, sticky=E)

		Label(master, text="Current Total: ", bg='#D8CAC8', fg='#000').grid(row=16, column=1, padx=14, pady=8, sticky=W)
		Label(master, textvariable=displayTotal, bg='#D8CAC8', fg='#000').grid(row=16, column=1, padx=14, pady=8)
		Button(master, text="Print Receipt", command=receipt).grid(row=18, column=2)
		Button(master, text="Cancel Order", command=cancel).grid(row=18, column=3)

root = Tk()
root.geometry("1000x800")
phototop = PhotoImage(file="pizza.gif")
photobottom = PhotoImage(file="pizza3.gif")
order_number = random.randint(100, 999)

app = Application(master=root)
app.mainloop()
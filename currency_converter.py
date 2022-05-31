import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
from wsgiref import validate
from forex_python.converter import CurrencyRates

root = Tk()
root.title('Currency Conversion')
root.geometry('600x600')
root.config(background='lightgrey')

c = CurrencyRates()

variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)

variable1.set("Select")
variable2.set("Select")

def validate():
    return False

def conversion():
    i = variable1.get()
    o = variable2.get()
    # Makes sure the user didn't leave the input field blank
    if(input.get() == ""):
        tkinter.messagebox.showinfo("Error!", "Please enter a value.")
    # Makes sure the user selected two currencies
    elif(i == "Select" or o == "Select"):
        tkinter.messagebox.showinfo("Error!", "Please select a currency.")    
    else:
        # Checks if the user typed in a number
        try:
            float(input.get())
        except ValueError:
            tkinter.messagebox.showinfo("Error!", "Please enter only numbers.")
        else:
            calc = c.convert(i, o, float(input.get()))
            rate.set(calc)

rate = StringVar()

currency_list = ["USD", "CAD", "CNY", "DKK", "EUR", "INR", "JPY", "BGN", "ILS", "AUD"]

##### Input 1
from_option = tk.OptionMenu(root, variable1, *currency_list)
from_option.place(x=10,y=10)

##### Input 2
to_option = tk.OptionMenu(root, variable2, *currency_list)
to_option.place(x=10,y=100)

calculate_button = Button(text = "Calculate!", command = conversion)
calculate_button.place(x=10,y=200)

input = Entry(width=50, justify=tk.RIGHT)
input.place(x=10,y=300)

vcmd = (root.register(validate))
output = Entry(width=50, justify=tk.RIGHT, textvariable=rate, validatecommand=vcmd)
output.place(x=10,y=400)
output.update()
output.configure(validate='key')

root.mainloop()

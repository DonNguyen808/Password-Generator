import random
from tkinter import *
from tkinter.ttk import *


# Function for calculation of password
def low():
    entry.delete(0, END)

    # Length of password
    length = var1.get()

    # Define data
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    num = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""


    # Strength of low password
    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password

    # Strength of medium password
    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password

    # Strength of strong password
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(num)
        return password

    else:
        print("Please choose one")



# Function for generate button
def generate():
    password1 = low()
    entry.insert(10, password1)

# Make the GUI window
root = Tk()
var = IntVar()
var1 = IntVar()

# Title
root.title("Random Password Generator")


# Password Label
random_password = Label(root, text="Password")
random_password.grid(row=0)

# Entry for the password
entry = Entry(root)
entry.grid(row=0, column=1)

length_label = Label(root, text="Length")
length_label.grid(row=1)

# Generate Button
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=2)



# Radio button
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky="E")
radio_medium = Radiobutton(root, text="Medium", variable=var, value=0)
radio_medium.grid(row=1, column=3, sticky="E")

radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky="E")

combo = Combobox(root, textvariable=var1)

# Combo box for length of password
combo['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
combo.current(0)
combo.bind("<<ComboboxSelected>>")
combo.grid(column=1, row=1)

root.mainloop()







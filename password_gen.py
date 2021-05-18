import string
import random


# Define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# Intro
print("Welcome to the password generator!")

# Ask the length of password
while True:
    length = input("How many characters for this password?")
    if length.isalpha():
        print("Please enter a number")
    if length.isdigit():
        break

add_all = ""

while True:
    l_confirm = input("Include lowercase?")
    if l_confirm == "yes":
        add_all += lower
    else:
        pass

    u_confirm = input("Include uppercase?")
    if u_confirm == "yes":
        add_all += upper
    else:
        pass

    num_confirm = input("Include numbers?")
    if num_confirm == "yes":
        add_all += num
    else:
        pass

    s_confirm = input("Include symbols?")
    if s_confirm == "yes":
        add_all += symbols
    else:
        pass

    if add_all !="":
        break

temp = random.sample(add_all, int(length))

# Combine all
all = lower + upper + num + symbols

# Create the password
password = "".join(temp)

print(password)













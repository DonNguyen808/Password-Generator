import string
import random


# define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# intro
print("Welcome to the password generator!")

# ask the length of password
while True:
    length = input("How many characters for this password?")
    if length.isalpha():
        print("Please enter a number")
    if length.isdigit():
        break

add_all = ""

l_confirm = input("Include lowercase?")
if l_confirm == "yes":
    add_all += lower
else:
    pass

u_confirm = input("include uppercase?")
if u_confirm == "yes":
    add_all += upper
else:
    pass

num_confirm = input("include numbers?")
if num_confirm == "yes":
    add_all += num
else:
    pass

temp = random.sample(add_all, int(length))




# combine all
all = lower + upper + num + symbols

#use random
# temp = random.sample(all, length)

# create the password
password = "".join(temp)

print(password)













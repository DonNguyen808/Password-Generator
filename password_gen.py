import string
import random

# intro
print("Welcome to the password generator!")

# ask the length of password
length = int(input("how many characters for this password?"))

# define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# combine all
all = lower + upper + num + symbols

#use random
temp = random.sample(all, length)

# create the password
password = "".join(temp)

print(password)













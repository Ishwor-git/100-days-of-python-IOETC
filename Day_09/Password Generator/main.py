print("""
    PASSWORD GENERATOR USING PYTHON (PyPassword Generator)
""")

import random
import string


print("Welcome to the PyPassword Generator!\n")


alphabets = list(string.ascii_letters)
numerals = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '+', '=', '/', '?', ';']


print("""Please specify: 
1. No. of letters you'd like in your password.
2. No. of symbols.
3. How many numbers you'd like.\n""")



letters = int(input("How many letters would you like in your password? "))
sym = int(input("How many symbols would you like? "))
nums = int(input("How many numbers would you like?\n "))


items = []


for j in range(letters):
    l = random.choice(alphabets)
    items.append(l)

for k in range(sym):
    m = random.choice(symbols)
    items.append(m)

for n in range(nums):
    o = random.choice(numerals)
    items.append(o)

random.shuffle(items)

password = ""
for elems in items:
    password = password + elems


print(f"Here is your password: {password}\n")

if len(password) <= 6:
    print("Weak Password!")
elif len(password) == 7:
    print("Password strength is medium.")
else:
    print("Your password is strong.")

    
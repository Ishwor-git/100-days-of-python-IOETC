print("Welcome to the tip calculator!")


bill_amount = float(input("What is the total bill amount? ($) "))

tip = float(input("How much tip would you like to give? (in %) "))

no_of_people = int(input("How many people to split the bill? "))

total = bill_amount + (tip / 100 * bill_amount)
split_amount =  total / no_of_people

print(f"Each person should pay: ${split_amount}")





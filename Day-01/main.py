
print("Welcome to tip calculator")
print("What is the total bill amount ? ")
bill_amount = float(input("> Rs "))

print("How much tip would you like to give ? (in percentage) ")
tip_perc = float(input("> "))

print("How many people to split the bill ?")
no_people = int(input("> "))

tot_amount = bill_amount *(100+tip_perc)/100
split_amount = tot_amount / no_people

print("Each person should pay Rs {}".format(split_amount))
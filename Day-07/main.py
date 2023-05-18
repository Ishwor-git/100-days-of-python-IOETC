print("Welcome to factor finder ")

base_num = int(input("Enter Number >> "))
factors = []

for i in range(1,base_num + 1):

    if base_num % i == 0:
        factors.append(i)

print("Factors are : {}".format(factors))

if len(factors) == 2:
    print("This is prime number")
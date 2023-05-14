"""
    Factor Finder
"""
print("Factor Finder")
print()

while True:
    num = input("Enter a number to factor (or press 'q' to exit): ")
    if num == 'q':
        break
    else:
        num = int(num)
        print(f"Factors of {num} are:")
        print()
        for i in range(1, num+1):
            if num % i == 0 and i == num:
                print(i)
            elif num % i == 0:
                print(i, end=', ')



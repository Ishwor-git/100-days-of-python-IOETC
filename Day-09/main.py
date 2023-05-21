import random
from string import ascii_uppercase,ascii_lowercase,digits,punctuation

def make_list_str(input,option):
    if option.upper() == 'S':
        output = ''
        for i in input:
            output += i
    elif option.upper() == 'L':
        output = [i for i in input]
    else:
        raise Exception
    
    return output

def random_char(values,no_char):
    output = ''
    for i in range(no_char):
        output += random.choice(values)
    return output

def suffle_str(input):
    lst_inp = make_list_str(input,'L')
    random.shuffle(lst_inp)
    return make_list_str(lst_inp,'S')
    pass

# Start main code here

print("Please specify no of following character you want.")
uc = int(input("Uppercase  >> "))
lc = int(input("Lowercase  >> "))
nc = int(input("Numeric character >> "))
sc = int(input("Speical character >> "))

raw_passwd = ''
raw_passwd += random_char(ascii_uppercase,uc) + random_char(ascii_lowercase,lc) + random_char (digits,nc) + random_char(punctuation,sc)
print("Your Password : >> {}".format(suffle_str(raw_passwd)))

if len(raw_passwd) < 8:
    print("\nYour password is weak. We advise you to use at least 8 character long password")
elif len(raw_passwd) == 8:
    print("\nYour password is average")
else:
    print("Your password is strong")
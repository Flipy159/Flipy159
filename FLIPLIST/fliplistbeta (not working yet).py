####---Libraries---####
import os
import random
from itertools import product
import string
import time
from os import system, name
####---Strings---####
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

passwrd = ""
pass2 = ""
pass3 = ""
pass4 = ""

upper, lower, nums, syms = False, False, False, False


per_name = ""
per_email = ""
per_add = ""
per_num = ""
per_hob = ""
passrab = ""



####---Clear Functions---####
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

####---counter---####
counter = 0
####---Colored Text---####
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
    #e.g. print(colored(0, 0, 0, 'Hello, World'))
####---LOGO--####
print(colored(0,255,0," _________   __           __   ________   __           __      __________       ____________"))    
print(colored(0,255,0,"|   ______| |  |         |  | |   __   | |  |         |  |    /        * | __y |____    ____|  "))
print(colored(0,255,0,"|  |        |  |         |  | |  |__|  | |  |         |  |   /  ---------\/         |  |     "))
print(colored(0,255,0,"|  |_____   |  |         |  | |   _____| |  |         |  |  /  /                    |  |      "))
print(colored(0,255,0,"|   _____|  |  |         |  | |  |       |  |         |  |  \  \______              |  |     "))
print(colored(0,255,0,"|  |        |  |         |  | |  |       |  |         |  |   \_____   |             |  |  "))
print(colored(0,255,0,"|  |        |  |_______  |  | |  |       |  |_______  |  |    _____|  |             |  |    "))
print(colored(0,255,0,"|__|        |__________| |__| |__|       |__________| |__|   |________|             |__|       "))

####---Options---####
print("Choose a option: ")
print("(1) Personal")
print("(2) Random")
print("(3) Custom")
opts = int(input())
clear()




####---Custom---####
while opts == 3:
    file_open = open("flipcustomlist.txt", 'w')
    print("Select which options you would like to have on your custom dictionary")
    if upper:
        print("(1) Uppercase Letters     " + str(colored(0,255,0, upper)))
    else:
        print("(1) Uppercase Letters     " + str(colored(255,0,0, upper)))
    if lower:
        print("(2) Lowercase Letters     " + str(colored(0,255,0, lower)))
    else:
        print("(2) Lowercase Letters     " + str(colored(255,0,0, lower)))
    if nums:
        print("(3) Numbers               " + str(colored(0,255,0, nums)))
    else:
        print("(3) Numbers               " + str(colored(255,0,0, nums)))
    if syms:
        print("(4) Symbols               " + str(colored(0,255,0, syms)))
    else:
        print("(4) Symbols               " + str(colored(255,0,0, syms)))
    cust = int(input(": "))
    if cust == 1:
        upper = True
        if upper:
            passwrd += uppercase_letters
    if cust == 2:
        lower = True
        if lower:
            passwrd += lowercase_letters
    if cust == 3:
        nums = True
        if nums:
            passwrd += numbers
    if cust == 4:
        syms = True
        if syms:
            passwrd += symbols
    cont = input("Do you want to add more? ")
    if cont == "y":
        clear()
        continue
    if cont == "y":
        clear()
    if cont == "n":
        clear()
    else:
        print("Invalid argument (y or n)")
        clear()
        continue
    break
        
    
        

####---Random---####
while opts == 2:
    file_open = open("flipcustomlist.txt" 'w')
    upper = True
    lower = True
    nums = True
    syms = True
    if upper:
        passwrd += uppercase_letters
    if lower:
        passwrd += lowercase_letters
    if nums:
        passwrd += numbers
    if syms:
        passwrd += symbols
    break


####---Personal---####
while opts == 1:
    clear()
    file_open = open("fliplist.txt" , 'w')

    print("If you have information about this person please select the following options")
    print("(1) Name")
    print("(2) E-mail")
    print("(3) Address")
    print("(4) Phone Number")
    print("(5) Hobby")
    print("(6) Check Information")
    print("(7) Make Wordlist")
    choice = int(input(": "))
    


    if choice == 1:
        clear()
        per_name = input("Targets Name: ")
        continue
    if choice == 2:
        clear()
        per_email = input("Targets E-mail: ")
        continue
    if choice == 3:
        clear()
        per_add = input("Targets Address: ")
        continue
    if choice == 4:
        clear()
        per_num = input("Targets Phone Number: ")
        continue
    if choice == 5:
        clear()
        per_hob = input("Targets Hobby: ")
        continue
    if choice == 6:
        clear()
        print("Name: "+ str(per_name))
        print("E-mail: " + str(per_email))
        print("Address: " + str(per_add))
        print("Phone Number: " + str(per_num))
        print("Hobby: " + str(per_hob))
        cont = input("Continue? ")
        if cont == "":
            continue

    elif choice == 7 :
        if per_name == "":
            per_name == False
        if per_email == "":
            per_email == False
        if per_hob == "":
            per_hob == False
        if per_num == "":
            per_num == False
        if per_add == "":
            per_add == False
        
        print("Type the Following (in lowercase) to add to the password: ")
        print("Upper case letters")
        print("Lower case letters")
        print("Numbers")
        print("Symbols")
        print("All")
        opts2 = input(": ")
        opts2 = opts2.lower()
        if opts2 == "uppercase" or "upper" or "uppercaseletters" or "upper case letters" or "upper case letter" or "uppercaseletter":
            upper = True
        if opts2 == "lowercase" or "lower" or "lowercaseletters" or "lower case letters"  or "lower case letter" or "lowercaseletter":
            lower = True
        if opts2 == "numbers" or "number":
            nums = True
        if opts2 == "symbols" or "symbol": 
            syms = True
        if opts2 == "all":
            upper = True
            lower = True
            nums = True
            syms = True
        if upper:
            passran += uppercase_letters
        if lower:
            passran += lowercase_letters
        if nums:
            passran += numbers
        if syms:
            passran += symbols
        per_name = str(per_name)
        per_email = str(per_email)
        per_add = str(per_add)
        per_num = str(per_num)
        per_hob = str(per_hob)
        passran = str(passran)
    
    break

    
#For Loop for finding out amount, length messurements, and opening and writing the file that took me ages
if per_name == True:
    passwrd_name = per_name
if per_email == True:
    passwrd_email = per_email
if per_hob == True:
    passwrd_hob = per_hob
if per_num == True:
    passwrd_num = per_num
if per_add == True:
    passwrd_add = per_add

total_amount = int(input("Total Number of Passwords "))
amount = int(input("Number of each section of Passwords "))
min_length = int(input("Minimum Length of Passwords "))
max_length = int(input("Maximum Length of Passwords "))
password = ""
for j in range(total_amount):
    for l in range(amount):
        for q in range(min_length, max_length):  
            password = int(passwrd_name + 1)
            password = str(password)
            file_open.write(password)
            file_open.write('\n')
    for m in range(amount):
        for z in range(min_length, max_length):
            if per_add:
                password = int(passwrd_add + 1)
                password = str(password)
                file_open.write(password)
                file_open.write('\n')
    for n in range(amount):
        for e in range(min_length, max_length):
            if per_email:
                password = int(passwrd_email + 1)
                password = str(password)
                file_open.write(password)
                file_open.write('\n')
    for o in range(amount):
        for b in range(min_length, max_length):
            if per_num:
                password = int(passwrd_num + 1)
                password = str(password)
                file_open.write(password)
                file_open.write('\n')
    for p in range(amount):
        for a in range(min_length, max_length):
            if per_hob:
                password = int(passwrd_hob + 1)
                password = str(password)    
                file_open.write(password)
                file_open.write('\n')
    counter += 1

print("Generated " + str(counter) + " possible custom combonations")


        










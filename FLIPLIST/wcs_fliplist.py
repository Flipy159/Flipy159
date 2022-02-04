##--Libraries--##
import os
import random
import time
import string
from os import system , name
##--Clear Functions--##
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

##--Colored Text--##
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
    #e.g. print(colored(0, 0, 0, 'Hello, World'))

###--LOGO--###
print(colored(0,255,0," _________   __           __   ________   __           __      __________       ____________     ____        __          ___       ______          __________            "))    
print(colored(0,255,0,"|   ______| |  |         |  | |   __   | |  |         |  |    /        * | __y |____    ____|   \    \      /  \        /   /     /  ____*| y     /   ______ /     "))
print(colored(0,255,0,"|  |        |  |         |  | |  |__|  | |  |         |  |   /  ---------\/         |  |         \    \    /    \      /   /     /  /     \/     /   /            "))
print(colored(0,255,0,"|  |_____   |  |         |  | |   _____| |  |         |  |  /  /                    |  |          \    \  /   -  \    /   /     /  /            /   /_______            "))
print(colored(0,255,0,"|   _____|  |  |         |  | |  |       |  |         |  |  \  \______              |  |           \    \/   / \  \ _/   /     /  /             \_______    /              "))
print(colored(0,255,0,"|  |        |  |         |  | |  |       |  |         |  |   \_____   |             |  |            \       /   \       /      \  \________             /  /     "))
print(colored(0,255,0,"|  |        |  |_______  |  | |  |       |  |_______  |  |    _____|  |             |  |             \     /     \     /        \          /     _____ /  / "))
print(colored(0,255,0,"|__|        |__________| |__| |__|       |__________| |__|   |________|             |__|              \__ /       \__ /          \________/     /________/      "))
##--Vars--##
pass_inp = input("Type in the targets first three initials (ex. Abc, Doe) : ")
pos_nums = 0
usr_pass = ""
##--Opens File--##
txt = open("wcs_fliplist.txt", "w")



##--Ask For Verbose--##
ask = input("Do you want to run it verbose? (y/n) : ")

##--Adds 5 digits to the end of the pass_inp var--##
for i in range(99999):
    pos_nums += 1
    usr_pass = pass_inp + str(pos_nums)
    if ask == "y":
        print(usr_pass , '\n')
    
    txt.write(usr_pass)
    txt.write('\n')
txt.close()





    




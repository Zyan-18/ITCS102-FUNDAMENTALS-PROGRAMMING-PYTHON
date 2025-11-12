from activity25_1 import *

name = input("Hello! Please enter your name: ")

print(f"Hello {name}, welcome to My Compiler Program.")

isContinue = True

while isContinue == True:
    print("Please select a program.")
    print(" a - activity12\n b - activity13\n c - activity14\n d - activity15\n e - Exit the compiler program")

    choose = input("Please enter the chosen program: ")

    if choose == "a":
        activity12()
        continue
    elif choose == "b":
        activity13()
        continue
    elif choose == "c":
        activity14()
        continue
    elif choose == "d":
        activity15()
        continue
    elif choose == "e":
        print("You have exited the program. Thank you!")
        break
    else:
        print("Invalid input. Please try again.")
        continue
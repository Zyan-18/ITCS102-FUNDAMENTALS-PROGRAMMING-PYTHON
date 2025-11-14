from activity25_1 import *
from activity25_2 import *

name = input("Hello! Please enter your name: ")

print(f"Hello {name}, welcome to My Compiler Program.")

isContinue = True

while isContinue == True:
    print("Please select a program.")
    folder = input("Choose the folder that you wanted to open.\n\t Enter f1 for folder1 and f2 for for folder2.\n\t Input here: ").lower()

    if folder == "f1":
        print(" a - activity11\n b - activity12\n c - activity13\n d - activity14\n e - activity15\n f - Exit the compiler program")

        choose = input("Please enter the chosen program: ")

        if choose == "a":
            activity11()
            continue
        elif choose == "b":
            activity12()
            continue
        elif choose == "c":
            activity13()
            continue
        elif choose == "d":
            activity14()
            continue
        elif choose == "e":
            activity15()
            continue
        elif choose == "f":
            print("You have exited the program. Thank you!")
            break
        else:
            print("Invalid input. Please try again.")
            continue
    elif folder == "f2":
        print(" a - activity16\n b - activity17\n c - activity18\n d - activity19\n e - activity20\n f - Exit the compiler program")
        
        choose = input("Please enter the chosen program: ")

        if choose == "a":
            activity16()
            continue
        elif choose == "b":
            activity17()
            continue
        elif choose == "c":
            activity18()
            continue
        elif choose == "d":
            activity19()
            continue
        elif choose == "e":
            activity20()
            continue
        else:
            print("Invalid input. Please try again.")
            continue
    else:
        print("Invalid input. Please try again.")

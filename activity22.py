import random

num = random.randint(1,20)

tries = 0
con = True

while con == True:
    a = int(input("What number do you think it is (1-20): "))
    tries += 1

    if a == num:
        print("Congratulations")
        print(f"The number is {num}")
        print(f"You took {tries} tries!")
        break

    elif a > 20:
        print("Wrong input only 1-21")
        continue
    elif a < 1:
        print("Wrong input only 1-21")
        continue

    else:
        print("Sorry try again ")
        continue
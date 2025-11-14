def activity11():
    temp = eval(input("Enter temperature: "))

    if temp <= 20:
         print("The temperature is cold.")
    elif 21 <= temp <= 30:
         print("The temperature is lukewarm.")
    elif 31 <= temp <= 40:
         print("The temperature is warm.")
    elif 41 <= temp <= 50:
         print("The temperature is hot.")
    elif 51 <= temp:
         print("The temperature is boiling hot.")
    else:
        print("Invalid temperature.")

def activity12():
    number = 0
    for y in range (1,16):
        n = eval(input("Enter a number: "))
        number += n
    print('Total number is', number)

def activity13():
    for y in range (1,21,1):
        print(y, "-Hello World")

def activity14():
    for y in range (1,11,1):
        print(y)

    for y in reversed(range(1,11,1)):
        print(y)

def activity15():
    name = input("Enter your name: ")
    course = input("Enter your course: ")
    year = eval(input("Enter your year lever: "))
    section = input("Enter your section: ")
    
    print(f"\n Hello! My name is {name}. I'm from {course.upper()}-{year}{section.upper()}. Nice to meet you!")

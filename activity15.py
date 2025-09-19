#STRING FORMATTING

name = input("Enter your name: ")
course = input("Enter your course: ")
year = eval(input("Enter your year lever: "))
section = input("Enter your section: ")

print(f"\n Hello! My name is {name}. I'm from {course.upper()}-{year}{section.upper()}. Nice to meet you!")
def intro(name):
    print(f"Hi {name}! Welcome to my program.")

intro("Zyan")
intro("Kloe")
intro("Sanchez")

def sum(z):
    total = 0
    for y in range(z, 0, -1):
        total += y
    print(f"The sum of {z} is {total}")

sum(12)
sum(45)
sum(65)
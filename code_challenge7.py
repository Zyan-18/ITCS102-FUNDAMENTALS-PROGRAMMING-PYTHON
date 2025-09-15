print("ODD NUMBER SUMMATION")

sum = 0

for x in range(1,11,1):
    number = eval(input("Enter a number: "))
    if number % 2 != 0:
        sum += number

print("The sum of all odd numbers is:", sum)
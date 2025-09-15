print("FACTORIAL PROGRAM")

aa = eval(input("Enter a number: "))
print(aa, "!\n")
bb = 1

for x in range(aa,0,-1):
    print(x)
    bb *= x
print("The factorial of", aa, "is", bb)
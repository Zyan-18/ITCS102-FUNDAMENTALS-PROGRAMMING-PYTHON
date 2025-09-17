#Multiplication Table

print("MULTIPLICATION TABLE MAKER")
num = eval(input("Enter a number: "))
print("\nMultiplication Table for", num, ":")

for a in range(1,11):
    product = num * a
    print(num, "x", a, "=", product)
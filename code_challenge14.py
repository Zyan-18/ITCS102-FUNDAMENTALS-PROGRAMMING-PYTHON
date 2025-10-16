name = input("Hi! What is your name? ")
print("~~~"*20)
print("ODD number compiler, type '0' to terminate the loop.")

sum = 0
odd = ""
con = True

while con == True:
    num = eval(input("Please input a number: "))

    if num % 2 == 1:
        print("ODD number was detected.")
        odd += str(num) + ","
        sum += num
        continue
    elif num == 0:
        print("Loop Terminated.")
        break
    else:
        if num % 2 == 0:
            print("EVEN number was detected. Skipping...")
        else:
            print("Invalid number.")
            continue

print(f"Hello {name}, the sum of all the ODD numbers you input are {sum}.")
print(f"ALL the ODD number you input are {odd}")

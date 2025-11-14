def activity16():
    for a in range(1,11,1):
        print(a, end=" ")

def activity17():
    for a in range(1,11,1):
        for b in range(1,11):
            print(b, end=" ")
        print()

def activity18():
    for a in range(1, 12, 1):
        for b in range(1, a, 1):
            print(b, end=" ")
        print()

def activity19():
    for a in range(1, 12, 1):
        for b in range(1, a, 1):
            print("*", end=" ")
        print()

def activity20():
    for z in range(0, 11, 1):
        for y in range(0, z, 1):
            print(" ", end=" ")
        for a in range(10, z, -1):
            print(a, end=" ")
        print()
for z in range(1,8,1):
    for y in range(11,z,-1):
        print(" ", end=" ")
    for a in range(z,0,-1):
        print(a, end=" ")
    for n in range(2,y,1):
        print(n, end=" ")
    print()
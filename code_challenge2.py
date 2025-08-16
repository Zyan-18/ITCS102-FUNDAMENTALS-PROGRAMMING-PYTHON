amount = eval(input("Enter amount to deposit --> "))

z = amount // 1000
amount = amount % 1000
y = amount // 500
amount = amount % 500
a = amount // 200
amount = amount % 200
n = amount // 100
amount = amount % 100
k = amount // 50
amount = amount % 50
l = amount // 20
amount = amount % 20
o = amount // 10
amount = amount % 10
e = amount // 5
amount = amount % 5
s = amount // 1
amount = amount % 1



print("These are the breakdown of your deposit:")
print("\t", str(z) + "           ₱1000")
print("\t", str(y) + "            ₱500")
print("\t", str(a) + "            ₱200")
print("\t", str(n) + "            ₱100")
print("\t", str(k) + "             ₱50")
print("\t", str(l) + "             ₱20")
print("\t", str(o) + "             ₱10")
print("\t", str(e) + "              ₱5")
print("\t", str(s) + "              ₱1")

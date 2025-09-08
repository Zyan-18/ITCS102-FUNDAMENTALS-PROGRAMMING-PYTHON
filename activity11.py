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
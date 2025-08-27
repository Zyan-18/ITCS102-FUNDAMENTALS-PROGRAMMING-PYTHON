from getpass import getpass

user_name = "Zyan"
pass_word = "18"

username = input("Enter your username: ")
password = getpass("Enter your password: ")


if user_name == username and pass_word == password:
	print("Access Granted")
else:
	print("Access Denied")


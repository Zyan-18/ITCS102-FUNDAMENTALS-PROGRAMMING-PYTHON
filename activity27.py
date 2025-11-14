print("Adding Data to dictionary.")
print("=================================")
con = True

empty_dictionary = {}

def print_anime():
    for a,b in empty_dictionary.items():
        print(f"CODE {a} TITLE {b}")

def for_search(keys):
    print("Searching...")
    print(f"Results: {empty_dictionary[keys].upper()}")

while con == True:
    keys = input("Input keys for this anime: ") 

    value = input("Enter anime title: ")

    empty_dictionary[keys] = value

    choice = input("Would you like to continue adding anime \n y-Yes\n n-No \n p-PRINT\n s-Search\nanswer: ").lower()

    if choice == "y":
        print("Continuing...")
        continue
    elif choice == "n":
        print("Program stops...")
        break
    elif choice == "p":
        print_anime()
        continue
    elif choice == "s":
        for_search(keys)
        continue
    else:
        print("Invalid input. Please try again.")
        continue
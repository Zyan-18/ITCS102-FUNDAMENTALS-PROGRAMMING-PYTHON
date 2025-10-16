stillDirty = True

while stillDirty == True:
    confirm = input("Do you want to continue cleaning? (yes/no): ").lower()

    if confirm == 'yes':
        print("Continue cleaning...")
    elif confirm == 'no':
        print("Cleaning stopped.")
        break
    else:
        print("Invalid answer. Please try again.")
        continue
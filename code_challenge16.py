import os
import json

os.system('cls') 
print("STUDENT INFORMATION SYSTEM")
print("------------------------------------------------")


student_records = {}

while True:
    print("\nSELECT FROM THE OPTIONS BELOW \n  A - Add Student Record \n  B - Print All Record \n  C - Search Student Record \n  D - Delete a student record \n  E - Edit student record \n  F - Export data \n  G - Print \n H - Exit program")

    choice = input("\nYour choice: ").upper()

# add information
    if choice == "A":
        os.system('cls')
        print("\n\t ADDING STUDENT INFORMATION")
        print("-----------------------------------------------")
        student_id = input("Key search (student ID) for this student: ")

        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        course = input("Enter student's course: ")
        email = input("Enter student's email address: ")
        isSingle = input("Are you single? (yes/no): ")
        
        student_records = {student_id : [first_name, last_name, course, email, isSingle]}
        print("DATA SAVED")

        os.system('cls')
        continue

# for search
    elif choice == "B":
        print("\nPRINTING STUDENT RECORD\n")

        for id, record in student_records.items():
             print(f"STUDENT ID {id} in STUDENT RECORD {record}")
        continue

    elif choice == "C":
        os.system('cls')
        print("SEARCH STUDENT RECORD\n")

        search_id = input("\nEnter the ID to search: ").lower()

        for id in student_records.keys():
            if search_id in student_records.keys():
                 print("\nRECORD FOUND.")
                 
            else:
                print("NO RECORD FOUND.")
        continue

    elif choice == "D":
        os.system('cls')
        print("DELETE EXISTING RECORD...")
        
        search_id = input("Input ID to search: ").lower()

        for id in student_records.keys():
            if search_id in student_records.keys():
                print("\nRECORD FOUND.")
                for a in student_records[search_id]:
                      print(f"-- {a}")
                      
                student_records.pop(search_id)
                print("\nRECORD DELETED.")
            else:
                print("\n NO RECORD FOUND.")
                continue

    elif choice == "E":
        os.system('cls')
        print("EDIT / MODIFY STUDENT RECORD \n")
        search_id = input("Input ID to search: ").lower()

        for id in student_records.keys():
            if search_id in student_records.keys():
                print("RECORD FOUND.")
                for i in student_records[search_id]:
                    print(f" - {i}")
            else:
                print("NO RECORD FOUND.")
            break
        continue

    elif choice == "F":
        os.system('cls')
        print("Export Student Record")
        with open('student_record.json', 'w') as new_file:
            json.dump(student_records, new_file, indent=4)

    elif choice == "G":
        os.system('cls')
        print("Import Student Record")
        with open('student_record.json', 'r') as new_file:
            student_json = json.load(new_file)

        student_records = student_json
        print("DATA IMPORTED TO JSON.")
        continue
    
    elif choice == "H":
        print("System Exit")
        break

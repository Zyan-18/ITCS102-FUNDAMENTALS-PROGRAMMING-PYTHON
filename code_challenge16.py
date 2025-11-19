import os

os.system('cls')
print("STUDENT INFORMATION SYSTEM")
print("------------------------------------------------")


student_records = {}

while True:
    print("SELECT FROM THE OPTIONS BELOW \n  A - Add Information \n  B - Search a record \n  C - Delete a record \n  D - Modify a record \n  P - Print \n E - Exit program")

    choice = input("Your choice: ").upper()

    if choice == "A":
        print("ADDING STUDENT INFORMATION")
        print("-------------------------------------------------")
        search_code = input("Key search for this student: ")

        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        course = input("Enter student's course: ")
        email = input("Enter student's email address: ")
        isSingle = input("Are you single? (yes/no)")
        
        student_record = {search_code : [first_name, last_name, course, email, isSingle]}
        print("DATA SAVED")

    elif choice == "B":
        os.system('cls')
        code = input("Enter search code")

        for j in student_record.keys():
            if code in student_record.keys():
                print("Record found.")

                for i in student_record[code]:
                    print(i)
            else:
                    print("NO RECORD FOUND")
        continue
    elif choice == "C":
        pass
        continue
    elif choice == "D":
         print("EDITING EXISTING RECORD...")
         continue
    elif choice == "P":
         for i,j in student_record.items():
              print(f"CODE - {i} STORD INFORMATION: {j}")
              continue
    elif choice == "E":
         print("SYSTEM EXIT")
         break
    else:
         print("\n INVALID CHOICE, please RE-ENTER YOUR CHOICE.")



# import os

# os.system('cls') 
# print("STUDENT INFORMATION SYSTEM")
# print("------------------------------------------------")


# student_records = {}

# while True:
#     print("\nSELECT FROM THE OPTIONS BELOW \n  A - Add Student Record \n  B - Print All Record \n  C - Search Student Record \n  D - Delete a student record \n  E - Edit student record \n  F - Export data \n  G - Print \n E - Exit program")

#     choice = input("\nYour choice: ").upper()

# # add information
#     if choice == "A":
#         os.system('cls')
#         print("\n\t ADDING STUDENT INFORMATION")
#         print("-----------------------------------------------")
#         student_id = input("Key search for this student: ")

#         first_name = input("Enter student's first name: ")
#         last_name = input("Enter student's last name: ")
#         course = input("Enter student's course: ")
#         email = input("Enter student's email address: ")
#         isSingle = input("Are you single? (yes/no): ")
        
#         student_record = {student_id : [first_name, last_name, course, email, isSingle]}
#         print("DATA SAVED")

#         os.system('cls')
#         continue

# # for search
#     elif choice == "B":
#         print("PRINTING STUDENT RECORD\n")

#         for id, record in student_records.items():
#              print(f"STUDENT ID {id} in STUDENT RECORD {record}")
#         continue

#     elif choice == "C":
#         os.system('cls')
#         print("SEARCH STUDENT RECORD\n")

#         search_id = input("\nEnter the ID to search: ").lower()

#         for id in student_records.keys():
#              print("\nRECORD FOUND.")

#         else:
#              print("NO RECORD FOUND.")
#         continue

#     elif choice == "D":
#          os.system('cls')
#          print("DELETE EXISTING RECORD...")

#          search_id = input("Input ID to search: ").lower()
#          if search_id in student_records.keys():
#               print("\nRECORD FOUND.")
#               for a in student_records[search_id]:
#                 print(f"-- {a}")

#                 student_records.pop(search_id)
#                 print("RECORD DELETED.")
#     else:
#         print("\n NO RECORD FOUND.")
#     continue

    # elif choice == "P":
    #      for i,j in student_record.items():
    #           print(f"CODE - {i} STORD INFORMATION: {j}")
    #           continue
    # elif choice == "E":
    #      print("SYSTEM EXIT")
    #      break
    # else:
    #      print("\n INVALID CHOICE, please RE-ENTER YOUR CHOICE.")


                  


                  


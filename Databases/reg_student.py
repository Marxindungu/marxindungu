from databases import student

try:
    name = input("Enter Name\n")
    phone = input("Enter phone\n")
    age = input("Enter Age\n")
    gender = input("Enter Gender\n")
    code = input("Enter student code\n")


    print("Student Created Successfully")

except:
    print("Failed to create user")

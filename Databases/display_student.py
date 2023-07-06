from databases import student

student = student.select()
#use forloop to display
for student in student:
    print(student.name, student.phone, student.age, student.gender, student.code)

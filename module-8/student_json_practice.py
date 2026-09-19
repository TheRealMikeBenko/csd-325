# Michael Benko
# 2026-09-19
# CSD325-302E Advanced Python (2267-DD)
# Module 8.2 Assignment

import json
from os import  path

filename = 'c:/csd/csd-325/module-8/student.json'

# Check if file exists
if path.isfile(filename) is False:
  raise Exception("File not found")
 
# Read JSON file
with open(filename) as fp:
  students = json.load(fp)

def print_students(student_list):
   for student in student_list:
    print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

print("Original Student list")
print_students(students)

# Add your student record
new_student = {
    "F_Name": "Michael",
    "L_Name": "Benko",
    "Student_ID": 99999,   # fictional ID
    "Email": "mbenko@my635.bellevue.edu"
}

students.append(new_student)

print("\nUpdated Student list")
print_students(students)

# Write updated list back to JSON file
with open(filename, "w") as fp:
    json.dump(students, fp, indent=4)

print("\nstudent.json file updated")
# Student Grade Tracker
# Master Branch - Base File

students = {}

print("Student Grade Tracker")
print("=====================")

num = int(input("How many students do you want to enter? "))

for i in range(num):
    name = input(f"Enter name of student {i + 1}: ")
    mark = int(input(f"Enter mark for {name}: "))
    students[name] = mark

print("\n--- Student Grades ---")
for name, grade in students.items():
    print(f"{name}: {grade}")
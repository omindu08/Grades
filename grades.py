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

def calculate_average(grades):
    return sum(grades.values()) / len(grades)

avg = calculate_average(students)
print(f"\nClass Average: {avg:.2f}")

def check_pass_fail(grades, threshold=50):
    results = {}
    for name, grade in grades.items():
        results[name] = "Pass" if grade >= threshold else "Fail"
    return results

results = check_pass_fail(students)
print("\nPass/Fail Results:")
for name, result in results.items():
    print(f"{name}: {result}")

def get_highest(grades):
    top = max(grades, key=grades.get)
    return top, grades[top]

def get_lowest(grades):
    bottom = min(grades, key=grades.get)
    return bottom, grades[bottom]

top_student, top_grade = get_highest(students)
low_student, low_grade = get_lowest(students)
print(f"\nHighest Score: {top_student} ({top_grade})")
print(f"Lowest Score:  {low_student} ({low_grade})")
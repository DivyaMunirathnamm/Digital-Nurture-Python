import json

students = {}

def add_grade(name, grade):
    if grade < 0 or grade > 100:
        print("Invalid Grade")
        return

    students.setdefault(name, []).append(grade)

def calculate_gpa(name):
    grades = students[name]
    return sum(grades) / len(grades)

add_grade("John", 80)
add_grade("John", 90)

print("GPA:", calculate_gpa("John"))

class_avg = sum(sum(v) for v in students.values()) / sum(len(v) for v in students.values())

print("Class Average:", class_avg)

with open("grades.json", "w") as file:
    json.dump(students, file)
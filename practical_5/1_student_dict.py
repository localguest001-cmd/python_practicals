# Students scoring above 75

n = int(input("Enter number of students: "))
students = {}

for i in range(n):
    roll = input(f"Enter roll number of student {i+1}: ")
    name = input(f"Enter name of student {i+1}: ")
    marks = int(input(f"Enter marks of student {i+1}: "))
    students[roll] = {"name": name, "marks": marks}

print("Students who scored above 75:")
for student in students.values():
    if student["marks"] > 75:
        print(student["name"])

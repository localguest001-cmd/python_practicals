# Student class with operator overloading

class Student:
    def __init__(self, roll_no, name, age, total_marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.total_marks = total_marks

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Total Marks:", self.total_marks)

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.total_marks == other.total_marks
        return False


students = [
    Student(1, "{{NAME}}", 18, 85),
    Student(2, "mahesh", 19, 90),
    Student(3, "raj", 20, 85),
    Student(4, "Nisha", 21, 92)
]

print("All Students:")
for student in students:
    student.display()
    print()

print("Students with Same Total Marks:")
for i in range(len(students)):
    for j in range(i+1, len(students)):
        if students[i] == students[j]:
            print("Student 1:")
            students[i].display()
            print("Student 2:")
            students[j].display()
            print()

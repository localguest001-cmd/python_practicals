# Student class with getters and setters

class Student:
    def __init__(self, name, id, age, grade, school):
        self.name = name
        self.id = id
        self.age = age
        self.grade = grade
        self.school = school

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade


student = Student("{{NAME}}", 2227, 20, 11, "UPL University")

print("Before setting values:")
print("Name:", student.get_name())
print("Grade:", student.get_grade())

student.set_name("Raju cloud")
student.set_grade(12)

print("\nAfter setting values:")
print("Name:", student.get_name())
print("Grade:", student.get_grade())

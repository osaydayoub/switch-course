# EX:
# Create a Student class with name and age.
# Create 2 students.
# print their name and age.
# Add a method add_grade that stores a new grade.
# Add a method did_fail that returns True if any grade is below 60, otherwise False
# Add 5 random grades to each student, and check if any of them has failed using the did_fail method.
import random

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
    def add_grade(self,grade):
        self.grades.append(grade)
    def did_fail(self):
        for grade in self.grades:
            if(grade < 60):
                return True
        return False

student1 = Student("Adam",25)
student2 = Student("Rami",28)

print(f"student 1 name :{student1.name} age:{student1.age}")
print(f"student 2 name :{student1.name} age:{student2.age}")

# for i in range(5):
#     grade = random.randint(0, 100)
#     student1.add_grade(grade)

grades1=[100,50,80,77,60]
grades2=[100,95,86,77,60]

for g in grades1:
    student1.add_grade(g)

for g in grades2:
    student2.add_grade(g)


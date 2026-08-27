class Student:

    school = "VCTI"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def change_school(cls, new_school):
        cls.school = new_school

    def display(self):
        print(self.name, self.age, self.school)


name1 = input()
age1 = int(input())

name2 = input()
age2 = int(input())

new_school = input()

student1 = Student(name1, age1)
student2 = Student(name2, age2)

student1.display()
student2.display()

Student.change_school(new_school)

student1.display()
student2.display()
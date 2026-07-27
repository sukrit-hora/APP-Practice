class Student:
    college = "MIT ADT"

    def __init__(self, name, age):
        self.name = name
        self.age=age

    def display(self):
        print("Student Name: ",self.name)
        print("Student Age: ",self.age)

student1=Student("Sukrit",18)
student2=Student("Tina",19)

student1.display()
print()
student2.display()
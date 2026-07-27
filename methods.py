class Student:
    college = "MIT ADT"

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name: ",self.name)
        print("College: ",self.college)

    @classmethod
    def change_college(cls):
          print("College: ",cls.college)

    @staticmethod 
    def greet():
            print("Welcome to Python")

s=Student("Sukrit")
s.show()

Student.greet()
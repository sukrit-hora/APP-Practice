# Parent class
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

# Child class
class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def show(self):
        self.display()
        print("Roll No:", self.roll_no)

# Create object
s = Student("Sukrit", 39)
s.show()
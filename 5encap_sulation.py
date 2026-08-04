class Student:
    def __init__(self, name, marks):
        self.name = name          
        self.__marks = marks      

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.__marks)

    def setMarks(self, marks):
        self.__marks = marks

    def getMarks(self):
        return self.__marks

s = Student("Sukrit", 85)

s.display()

s.setMarks(95)

print("Updated Marks:", s.getMarks())
class Student:
    def message(self, msg):
        print("Message:", msg)

class Teacher:
    def __init__(self):
        self.student = Student()

    def notify(self):
        self.student.message("Class starts at 10 AM")

obj = Teacher()
obj.notify()
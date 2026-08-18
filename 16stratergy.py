class Add:
    def calculate(self, a, b):
        print("Addition =", a + b)

class Multiply:
    def calculate(self, a, b):
        print("Multiplication =", a * b)

class Calculator:
    def __init__(self, operation):
        self.operation = operation

    def solve(self, a, b):
        self.operation.calculate(a, b)

obj = Calculator(Add())
obj.solve(5, 3)

obj = Calculator(Multiply())
obj.solve(5, 3)
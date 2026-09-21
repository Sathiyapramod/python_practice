"""
Two numbers 10 and 20

addition -> 30
subtraction -> -10
multiplication -> 200
division -> 0.5


pass your inputs 10 and 20 only once

"""


# using my class
class Calculator:
    # constructor
    def __init__(self, x, y):
        # instantiate my parameters
        self.a = x  # a
        self.b = y  # b

    # methods
    # add
    def add(self):
        print(self.a + self.b)  # 10+20 = 30

    # subtract
    def subtract(self):
        print(self.a - self.b)  # 10-20 => -10

    def multiply(self):
        print(self.a * self.b)

    def divide(self):
        if self.b != 0:
            print(self.a / self.b)


# object1
test1 = Calculator(10, 20)

# how to print the added value
test1.add()
# how to print the subtracted value
test1.subtract()
test1.multiply()
test1.divide()

# object2
sample = Calculator(45, 30)
sample.add()  # 75
sample.subtract()  # 15
sample.multiply()  # 1350
sample.divide()  # 1.5


"""
word = "hello world"
word.upper()
word.lower()
"""

"""
Create a class called Student to store exam marks.

1. Attributes in __init__:
name (string)
mark1 (integer)
mark2 (integer)

2. Methods to write:

calculate_total(): Returns or prints the sum of mark1 + mark2.
calculate_average(): Divides the total by 2 and prints the average mark.
"""


class Student:
    # constructor
    def __init__(self, name, mark1, mark2):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2

    # methods
    def calculate_total(self):
        total = self.mark1 + self.mark2
        print("Total = ", total)

    def calculate_average(self):
        total = self.mark1 + self.mark2
        average = total / 2
        print("the average is", average)

    """
    write a method to print the student name
    """

    def student_name(self):
        print("Student name is = ", self.name)


sample = Student(name="John", mark1=85, mark2=95)
sample.calculate_total()
sample.calculate_average()
sample.student_name()

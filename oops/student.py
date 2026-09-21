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
        self.name = 
        self.mark1 = mark1
        self.mark2 = mark2

    # methods
    def calculate_total(self):
        print(self.mark1 + self.mark2)

    def calculate_average(self):
        total = self.mark1 + self.mark2
        average = total / 2
        print(average)


# calling my object

my_student = Student("Vetri", 75, 80)  # Attributes are passed here

# calling my methods here
my_student.calculate_total()
my_student.calculate_average()

print("Checking for another student below::::::")

test = Student("Sathish", 60, 60)
test.calculate_total()
test.calculate_average()

"""
How many key-value pairs are there ?
expected output: 3
"""

student = {"name": "Arun", "age": 21, "course": "Python"}
count = 0

for key in student:
    print(student[key])
    count = count + 1
print(count)


"""
Create a dictionary called my_book containing:
 
title → Python Basics
author → ABC
price → 450
"""

my_book = {
    "title": "Python Basics",
    "author": "ABC",
    "price": 450,
    "": "I dont know",  # dont do this
    " ": "This is a double space",  # dont do this tooo !!!!
}

print(my_book)
print(my_book["title"])


"""
Given:
 
employee = {
    "name": "Riya",
    "age": 25,
    "department": "IT"
}
 
Write statements to print:

Riya

IT
"""
employee = {"name": "Riya", "age": 25, "department": "IT"}

print(employee["name"])
print()
print(employee["department"])


inventory = {"apples": 50, "bananas": 30, "oranges": 20}


for key in inventory:
    print(key.upper())


"""
Given the dictionary:

prices = {
"laptop": 800,
"mouse": 25,
"keyboard": 50
}

Tasks:

Use for loop to print values alone from "prices"
Print each value on a "single" line.
Calculate and print the total price of all items.
"""
prices = {"laptop": 800, "mouse": 25, "keyboard": 50}

output = 0

for key in prices:
    value = prices[key]
    output = output + value

print(output)


"""
student_grades = {
    "Alex": "A",
    "Sarah": "B+",
    "Mike": "A-"
}

Print in the below format:
Alex got a grade of A
Sarah got a grade of B+
Mike got a grade of A-

"""
student_grades = {"Alex": "A", "Sarah": "B+", "Mike": "A-"}


for name in student_grades:
    print(name, "got a grade of", student_grades[name])

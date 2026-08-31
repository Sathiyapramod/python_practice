"""
Write a function named student_intro that accepts a student's name, age, and course.
The function should:
Receive all three values.
Create a sentence using the given information.

Print the sentence.

Sample Input: student_intro(“john”, 25, “python”)
Output: My name is John, I am 25 years old and I am learning python

"""


def student_intro(name, age, course):
    result = (
        "My name is "
        + name
        + " ,I am "
        + str(age)
        + " years old and I am learning "
        + course
    )

    print(result)


student_intro(name="john", age=30, course="python")

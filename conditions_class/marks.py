marks = int(input("enter your marks :"))

if marks > 100 or marks < 0:
    print("invalid mark")


if marks >= 85 and marks <= 100:
    print("grade is S")
if marks >= 70 and marks <= 84:
    print("grade is A")
if marks >= 55 and marks <= 69:
    print("grade is B")
if marks >= 30 and marks <= 54:
    print("grade is C")
if marks >= 0 and marks <= 29:
    print("grade is D")

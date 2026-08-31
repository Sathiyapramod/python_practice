"""
Write a Python program to print numbers from 1 to 50.
If the number is divisible by 5, use pass.
If the number is divisible by 3, print "Divisible by 3".
Otherwise, print the number.

"""

for i in range(1, 50 + 1, +1):
    if i % 5 == 0:
        pass
    elif i % 3 == 0:
        print("Divisible by 3")
    else:
        print(i)

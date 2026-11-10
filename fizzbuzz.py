"""
Write a Python program that accepts a positive integer N from the user and prints all numbers
from 1 to N based on the following conditions:


If a number is divisible by both 3 and 5, print "FizzBuzz".
If a number is divisible only by 3, print "Fizz".
If a number is divisible only by 5, print "Buzz".
If a number is not divisible by either 3 or 5, print the number itself.

TC 7
1 to 7

1 -> 1
2 -> 2
3 -> Fizz
4 -> 4
5 -> Buzz
6 -> Fizz
7 -> 7

TC 15 
1 to 15
1 -> 1
2 -> 2
3 -> Fizz
4 -> 4
5 -> Buzz
6 -> Fizz
7 -> 7
8 -> 8
9 -> Fizz
10 -> Buzz
11 -> 11
12 -> Fizz
13 -> 13 
14 -> 14
15 -> FizzBuzz

"""

n = int(input("Enter the number \n"))

for i in range(1, n + 1, +1):
    # print(i)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

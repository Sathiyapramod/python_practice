"""
Write a Python function named calculate_sum that accepts a positive integer n as a parameter.
The function should:

* Receive the value of n.
* Start from the number 1.
* Add every number up to and including n.
* Print the final sum.

"""


def calculate_sum(x):
    # if number x is less than zero, return invalid
    if x <= 0:
        return "invalid"
    else:
        total = 0
        for i in range(1, x + 1, +1):
            total = total + i
        # print(total)
        return total


print(calculate_sum(5))  # 15
print(calculate_sum(9))  # 45
print(calculate_sum(-8))  # invalid
print(calculate_sum(18))  # 171
print(calculate_sum(0))  # invalid
print(calculate_sum(-1))  # invalid

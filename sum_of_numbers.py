"""Find the sum of all numbers from 1 to 5 (both inclusive) using a while loop.

total =
1 + 2 + 3 + 4 + 5
= 15


1 + 2 + 3 + ... + 5 =>
1 + 2 +3 + .... + 7 =>

1 +2 +3 + .... + n => Sum of N numbers from 1

=> n * (n + 1) / 2

"""

start = 1
end = 5


total = 0

while start <= end:
    total = total + start
    #print(total)
    start = start + 1

print(total)

"""
Print the multiplication table of 2 (from 2 × 1 up to 2 × 10) using a while loop.

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
.
.
.

2 x 10 = 20

CONDITIONS:
- use only while loop
- no if conditions allowed
"""

start = 1
end = 10

nmb = 2

while start <= end:
    print(nmb, "x", start, "=", nmb * start)
    start = start + 1

# Print the multiplication table of 2 (from 2 × 1 up to 2 × 10) using a for loop.

nmb = int(input("enter the largest number"))
print(nmb)

for i in range(1, nmb + 1, +1):
    print(2, "x", i, "=", 2 * i)

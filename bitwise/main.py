a = 3
# Left Shift operator
# general formula is a * 2^n

print(a << 1)  # this is returning  3 X 2^1 = 6
print(a << 2)  # this is returning 3 X 2^2 = 12
print(a << 3)  # this is returning 3 X 2^3 = 24

a = 256
# Right Shift operator
# general formula is a // 2^n

print(a >> 1)  # this is returning 256 // 2^1
print(a >> 2)  # this is returning 256 // 2^2
print(a >> 3)  # this is returning 256 // 2^3

x = 7  # 111
y = 4  # 100

# everywhere at the bits place, and operation is performed
print(x & y)  # 100 i.e. 4
print(3 & 4)  # 011 & 100 ,so the answer is  000 which is 0
print(2 & 6)  # 010 & 110 ,so the answer is  010 which is 2

# even numbers
print(14 & 1)  # definitely 0
print(26 & 1)  # definitely 0

# odd numbers
print(13 & 1)  # definitely 1
print(29 & 1)  # definitely 1


# finding whether the given number is a power of 2 or not
def power_of_two(x):
    return x & (x - 1) == 0


print(power_of_two(15))
print(power_of_two(16))
print(power_of_two(255))
print(power_of_two(256))

# bitwise NOT
# ~x = -(x+1)
print(~1)  # -2
print(~3)  # -4
print(~-5)  # 4
print(~-100)  # 99

# bitwise XOR
print(1 ^ 1)  # this will return 0
print(1 ^ 0)  # this will return 1
print(0 ^ 1)  # this will return 1
print(0 ^ 0)  # this will return 0

print(2 ^ 3)  # 010 ^ 011 , so this will be returning => 0001 -> 1
print(4 ^ 8)  # 0100 ^ 1000, so this will be returning => 1100 -> 12
print(5 ^ 7)  # 0101 ^ 0111, so this will be returning =>    0010 -> 2

print(~5)



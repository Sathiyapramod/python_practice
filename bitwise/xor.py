# print(12 ^ 3)  # 15
# print(8 ^ 5)  # 13

print(3 ^ 4)  # 7
"""
0011
0010
----
0001
"""

# right shift operator
# print(-512 >> 1)  # 256 #negative ->
# print(512 >> 4)  # 512 / 2^4 = 512 / 16 = 32
# print(512 >> 22)  # 2^9 / 2^22 = 1 // 2^13 = 0

# negative
print(3 ^ -4)
print(-3 ^ -4)
"""
1101
1100
----
0001



"""

"""
0011
1100
----
1111

"""


print(2 & 1)
print(21 & 1)

"""
0010 &
0001
----
"""


def find_even_or_odd(x):
    return x & 1 == 0


print(find_even_or_odd(2))
print(find_even_or_odd(21))

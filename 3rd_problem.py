x = 11
y = 6

a = x & y  # 2
b = x | y  # 15
c = a ^ b  # 13
d = c >> 1  # x >> y = x // 2 power y => 13 // 2 = 6
e = ~d  # ~n => -(n+1) = -(6+1) = -7

print(a)
print(b)
print(c)
print(d)
print(e)

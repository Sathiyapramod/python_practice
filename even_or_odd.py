# write a python function to find whether the given input parameter is even or odd


def even_or_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"


print(even_or_odd(5))
print(even_or_odd(7))
print(even_or_odd(-1))
print(even_or_odd(0))
print(even_or_odd(20))

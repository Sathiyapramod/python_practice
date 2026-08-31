x = "hello world"
# global scope
pi = 3.14


def do_something():
    # local scope
    y = "I am doing something"
    z = "inside the classroom"
    print(y + z)

    print(x)
    print(100)


do_something()
print(x)  # hello world
print(y)


def add(a, b):
    print(x)
    return a + b


add(10, 20)


def find_square(n):
    # welcome the function with x value
    # hello world
    print(x, "user")
    return n**2


def find_area(radius):
    # find the area of the circle
    area = pi * radius * radius
    return area


def triangle_area(base, height):
    area = 0.5 * base * height
    return area


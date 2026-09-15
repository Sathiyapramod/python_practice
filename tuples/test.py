"""
1.  Given fruits = ("apple", "banana", "cherry", "mango", "banana"), determine the length of the tuple.
2.  Identify the index of the initial occurrence of "banana" in the fruits tuple.
3.  Attempt to modify "cherry" to "grape" within the fruits tuple. Explain the outcome and the reason behind it.
4.  Given colors = ("red", "green", "blue") and shapes = ("circle", "square", "triangle"), combine colors and shapes to create a new tuple called art.

5.  Demonstrate how to repeat a tuple, specifically colors three times.
6.  Add an element called "Diamond" to the art tuple.
7.  Extract and print the middle element from the art tuple using slicing.
8.  Verify if the string "square" exists within the art tuple.
9.  Given marks = (78, 85, 69, 90, 85), determine the maximum and minimum marks.
10. Count the occurrence of 85 in the marks tuple. -> marks.count(85)
11. Calculate the average marks using the sum() and len() functions.

"""

# Given fruits = ("apple", "banana", "cherry", "mango", "banana"), determine the length of the tuple.
fruits = ("apple", "banana", "cherry", "mango", "banana")
print(len(fruits))

# Identify the index of the initial occurrence of "banana" in the fruits tuple.
print(fruits.index("banana"))

# Attempt to modify "cherry" to "grape" within the fruits tuple. Explain the outcome and the reason behind it.
# tuples -> immutable

# Given colors = ("red", "green", "blue") and shapes = ("circle", "square", "triangle"),
# combine colors and shapes to create a new tuple called art.
colors = ("red", "green", "blue")

shapes = ("circle", "square", "triangle")
art = colors + shapes
print(art)

# Demonstrate how to repeat a tuple, specifically colors three times.
# ("red", "green", "blue","red", "green", "blue","red", "green", "blue")

result = ()
for i in range(1, 4):
    result = result + colors
print(result)

new_colors = colors * 3
# print(new_colors)

new_colors = colors + colors + colors
# print(new_colors)

# Add an element called "Diamond" to the art tuple.
result = ("red", "green", "blue", "circle", "square", "triangle") + ("Diamond", "Ruby")
print(result)

# Extract and print the middle element from the art tuple using slicing.
print(art[3:4])

# Verify if the string "square" exists within the art tuple.
print("square" in art)

# Given marks = (78, 85, 69, 90, 85), determine the maximum and minimum marks.
marks = (78, 85, 69, 90, 85)
print(marks)
total = sum(marks)
count = len(marks)
avg = total / count
print(avg)

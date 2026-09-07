# =====================================================================
# PYTHON LIST COMPREHENSION PRACTICE EXERCISES
# Instructions: Complete the code for each problem using list comprehension.
# Do NOT use traditional for-loops or external libraries.
# =====================================================================

# ---------------------------------------------------------------------
# PART 1: MAPPING (Transforming Numbers)
# ---------------------------------------------------------------------

# Problem 1: Multiply by 3

# Given numbers = [1, 2, 3, 4, 5]
# Expected Output: [3, 6, 9, 12, 15]

numbers = [1, 2, 3, 4, 5]
#
ans1 = [numbers[i] * 3 for i in range(0, len(numbers))]
# Write your list comprehension here
print("Problem 1:", ans1)


# Problem 2: Convert to Negative Numbers
# Given values = [10, 20, 30, 40]
# Expected Output: [-10, -20, -30, -40]
values = [10, 20, 30, 40]
ans2 = [el * -1 for el in values]
# Write your list comprehension here
print("Problem 2:", ans2)


# Problem 3: Add 10 to Each Element
# Given scores = [50, 65, 70, 85]
# Expected Output: [60, 75, 80, 95]
scores = [50, 65, 70, 85]
ans3 = [el + 10 for el in scores]  # Write your list comprehension here
print("Problem 3:", ans3)


# ---------------------------------------------------------------------
# PART 2: FILTERING (Selecting Specific Numbers)
# ---------------------------------------------------------------------

# Problem 4: Extract Odd Numbers
# Given data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected Output: [1, 3, 5, 7, 9]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ans4 = [el for el in data if el % 2 != 0]  # Write your list comprehension here
print("Problem 4:", ans4)


# Problem 5: Numbers Greater Than 15
# Given numbers = [5, 12, 18, 7, 25, 30, 3]
# Expected Output: [18, 25, 30]
numbers = [5, 12, 18, 7, 25, 30, 3]
ans5 = [el for el in numbers if el > 15]  # Write your list comprehension here
print("Problem 5:", ans5)


# Problem 6: Filter Positive Numbers (Keep numbers >= 0)
# Given temperatures = [-5, 10, -2, 0, 15, -8, 22]
# Expected Output: [10, 0, 15, 22]
temperatures = [-5, 10, -2, 0, 15, -8, 22]
ans6 = [el for el in temperatures if el >= 0]
# Write your list comprehension here
print("Problem 6:", ans6)
# sorting the numbers
ans6.sort()
print(ans6)


# ---------------------------------------------------------------------
# PART 3: COMBINING MAPPING & FILTERING
# ---------------------------------------------------------------------

# Problem 7: Double Only Even Numbers
# Given numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Expected Output: [4, 8, 12, 16]
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
ans7 = []  # Write your list comprehension here
print("Problem 7:", ans7)


# Problem 8: Square Numbers Greater Than 5
# Given values = [2, 4, 6, 8, 10]
# Expected Output: [36, 64, 100]
values = [2, 4, 6, 8, 10]
ans8 = []
# Write your list comprehension here
print("Problem 8:", ans8)

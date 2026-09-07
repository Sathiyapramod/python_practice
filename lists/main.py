# ==========================================
# INTERACTIVE QUIZ: PYTHON LISTS
# Guess the output before running each line!
# ==========================================

# ------------------------------------------
# SECTION 1: INDEXING & SLICING
# ------------------------------------------
nums = [10, 20, 30, 40, 50, 60]
print(nums[0:3])  # Q1: What is the output?

data = [1, 2, 3, 4, 5, 6, 7, 8]
print(data[-3:])  # Q2: What is the output?

values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(values[::2])  # Q3: What is the output?













# ------------------------------------------
# SECTION 2: BUILT-IN METHODS
# ------------------------------------------
items = [10, 30, 40]
items.insert(1, 20)
print(items)  # Q4: What is the output?

items.reverse()
print(items)  # Q5: What is the output?

group1 = [1, 2, 3]
group2 = [4, 5, 6]
group1.extend(group2)
print(group1)  # Q6: What is the output?

grades = ["A", "B", "A", "C", "B", "A"]
print(grades.count("A"))  # Q7: What is the output?

grades.sort()
print(grades)  # Q8: What is the output?




# ------------------------------------------
# SECTION 3: INDEX-BASED WHILE LOOPS
# ------------------------------------------
# Print elements using index positions
colors = ["red", "green", "blue"]
i = 0
while i < len(colors):
    print(colors[i])  # Q9: What gets printed?
    i += 1

# Sum of first and last element
numbers = [5, 12, 18, 7, 25]
first_and_last_sum = numbers[0] + numbers[len(numbers) - 1]
print(first_and_last_sum)  # Q10: What is the output?

















# ------------------------------------------
# SECTION 4: INDEX-BASED FOR LOOPS (range + len)
# ------------------------------------------
# Print only positive numbers
vals = [10, -5, 20, -15, 30]
i = 0
while i < len(vals):
    if vals[i] > 0:
        print(vals[i], end=" ")  # Q11: What gets printed on one line?
    i += 1
print()

# Print 1-based position and element
names = ["Alice", "Bob", "Charlie"]
for i in range(len(names)):
    print(f"{i + 1}: {names[i]}")  # Q12: What gets printed?

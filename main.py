marks = [175, 180, 180, 192, 194, 189]

start = len(marks) - 1
end = 0

# print the marks in reverse
for i in range(start, end - 1, -1):
    print(marks[i])

# print the marks at odd indices
for j in range(1, len(marks), +2):
    print(marks[j])


# print the marks at even indices
for k in range(0, len(marks), +2):
    print(marks[k])

# print the marks above 90% (assume all marks out of 200)
for i in range(0, len(marks), +1):
    answer = 0.90 * 200  # 180
    if marks[i] > answer:
        print(marks[i])

# find and print the total marks
total = 0
for i in range(0, len(marks), +1):
    total = total + marks[i]
print("My total is", total)

# find the mean of all the marks
print(total / len(marks))

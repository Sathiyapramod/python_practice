# APPEND

marks = [88, 91, 94, 87]
print(marks)
# i want to add 85
marks.append(85)
print(marks)
# marks.append(100, 85)

# EXTEND
marks.extend([100, 85])
print(marks)

# INSERT
fruits = ["apple", "banana", "mango"]
print(fruits)  # ['apple', 'banana', 'mango']
fruits.insert(2, "orange")
print(fruits)  # ["apple", "banana", "orange", "mango"]


# REMOVE
a = [1, 2, 3, 1, 1, 1]
a.remove(1)
print(a)


# POP
b = [10, 20, 30, 40]
temp = b.pop()
print(b)
print(temp)

# clear()
names = ["john", "siva", "arjun", "daniel"]
print(names)
names.clear()
print(names)

# count()

print(a)
print(a.count(1))

# copy()
a = ["ram", "madurai muthu", "rithanya", "annalaxmi", "pugal"]
b = a.copy()
print(a)
print(b)

# making some change inside a
a.append("smartest_squad")
print(a)
print(b)


# join()
left = ["a", "b", "c"]
right = ["d", "e", "f"]
# option 1
# result = left + right
# print(result)


# index()
print(right.index("d"))
print(right.index("f"))
# print(right.index())


# sort()
height = [100, 120, 110, 140, 90]
height.sort()
print(height)


women = ["sangvi", "annalaxmi", "swetha", "rithanya", "sharmila", "harinisri"]
women.sort(reverse=True)
print(women)


# reverse()

# inbuilt functions
# max()
height = [100, 120, 110, 140, 90]
print(max(height))
a = ["a", "b", "c"]
print(max(a))

# min()
print(min(height))
# sum()
print(sum(height))
# print(sum(a))


names = ["zvetri", "tirumalesh", "zvetri"]
print(max(names))

marks = [180, 195, 192, 194, 189, 180]
print(max(marks)) 

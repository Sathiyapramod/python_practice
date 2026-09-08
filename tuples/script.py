# enum
cities = (
    "kallakuruchi",
    "tiruvallur",
    "ariyalur",
    "salem",
    "chennai",
    "coimbatore",
    "pudukottai",
    "tiruppur",
    "trichy",
    "kanyakumari",
    "tenkasi",
    "thanjavur",
    "erode",
)  # tuple of strings

marks = (35, 85, 73, 91, 96)  # tuple of numbers
# marks -> use your index

print(marks[2])
print(cities[2])

# print(marks[10]) #index out of range

print(len(cities))
print(len(marks))

# for i in range(0, len(cities)):
#     print(cities[i])

for each_city in cities:
    print(each_city)

# 91 -> 90 in marks tuple
# marks[3] = 90
# print(marks)

id = (1, 2, 3)
print(id)
# tuple -> ("started","progressing","finished")
id = ("started", "progressing", "finished")
print(id)

# slicing in the tuple
print(cities[2:7])
print(cities[9:11])

# print upto salem
print(cities[:4])
# print cities in even index
print(cities[::2])

# print the cities from a to z
print(type(sorted(cities)))
print(sorted(cities, reverse=True))

marks = (35, 85, 73, 91, 96)

print(max(marks))
print(min(marks))
print(sum(marks))

status = (1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1)
print(status.count(1))  # 6
print(status.count(0))  # 5

left = (1, 2, 3)
# right = left.copy()
# print(right)


# immutable
# cannot be changed


# lists
# mutable -> can be changed

# append() -> add an element
# pop() -> last (or) any element with an index
# remove() -> remove an element


nums = [10, 20, 30]
print(nums)
nums.clear()
print(nums)
print(nums.clear())
nums = nums.clear()  # list will be empty ->
# variable assigned -> None
# just print -> [] empty list

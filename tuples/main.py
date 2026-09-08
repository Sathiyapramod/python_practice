# creating a tuple
nums = (10, 20, 30)

print(nums)
print(type(nums))

# accessing an element inside a tuple
print(nums[0])
print(nums[2])

# print(nums[9]) Will print index out of range

# Slicing tuples
data = (75, 85, 95, 100, 105, 110, 75)
print(data[0:4])
print(data[1:6])
print(data[3:])
print(data[::-1])

# tuple concatenation
left = ("chennai", "coimbatore", "salem")
right = ("madurai", "trichy", "tiruppur")

result = left + right


# length of a tuple
print(len(data))
# minimum of a tuple
print(min(data))
# maximum of a tuple
print(max(data))
# count of a particular element inside a tuple
print(data.count(75))
# sorted
print(sorted(data))
# membership
print(75 in data)


# tuple unpacking

data = ("chennai", "salem", "trichy")
first, *pending = data

print(first, pending)

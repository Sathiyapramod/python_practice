# creating a new dictionary

employee = {
    "name": "john",  # string
    "id": 100,  # integer
    "address": "100 New York",
    "gender": "male",
    "skills": ["html", "css", "python", "git"],  # list
    # need to remove the vehicle_no
    "vehicle_no": None,  # none type
    "food_coupon": False,  # boolean
    "salary": 25943.72,  # float
    "assets": ("laptop", "charger", "mouse"),  # tuple
    "food_plan": {"breakfast", "lunch"},  # set
    "0": "nothing",  # here zero is key
}

# JSON

# name
# id number
# address
# gender
# contact number
# skills
# experience

print(employee)
print(type(employee))

# accessing an element through dictionary
# print(employee["gender"])
# print(employee["salary"])

# updating an existing key in the dictionary

# adding a new element to the dictionary
employee["date_of_birth"] = "16-09-2000"


# change the salary to 28000
employee["salary"] = 28000
# print(employee)


# Iterating through the dictionary

# printing the keys alone in a list format

# printing the values alone in a list format

# printing both key and values in a list format


nums = [88, 90, 34, 57, 29]
# print(nums[0])  # index

# option 1
# for i in range(0, len(nums), +1):
# print(nums[i])

# option 2
# for el in nums:
# print(el)

content = {"section": "A", "tag": "Gems of Academy", "count": 19}

del content["name"]

for key in content:
    print(content[key])
    # del content[key]
    # not possible


# del employee["vehicle_no"]

print(employee)

print("Hello world")

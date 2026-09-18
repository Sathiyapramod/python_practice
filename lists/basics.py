academy = {"section-a": 19, "section-b": 18, "section-c": 18}

# 1. adding a new key "classrooms":3
academy["classrooms"] = 3
print(academy)

# 2. printing the keys alone from a dictionary
# nums = [10,20,30]
# for i in range(0,len(nums)):
# for element in nums:
#      print(element)

# for key in academy:
#     print(key)

# 3. printing the values alone from the dictionary
# for x in academy:
#     print(academy[x])
# 4. deleting a particular k:v using key
del academy["classrooms"]
print(academy)

# 5. printing both keys and values in dictionary
for key in academy:
    print(key, academy[key])


# 6. count the total entries in dictionary
count = 0
for key in academy:
    # increment each entry through count variable
    count = count + 1
print(count)

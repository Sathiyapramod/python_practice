# unique collection of elements

"""
john
alexa
peter
steve
kevin
"""

# {} - flower bracket -> set & dictionary
# () = circular bracket -> tuple
# [] => square bracket -> list
nums = {88, 57, 42, 78, 90}
empty_set = set()
print(nums)
print(empty_set)

print(type(nums))
print(type(empty_set))

# length of the set
print(len(nums))

# adding an element to a set
batsman = {"rohitsharma", "kohli", "dhoni"}
print(batsman)
batsman.add("hardik")
print(batsman)


# remove an element from the given set
batsman.remove("dhoni")
print(batsman)
batsman.discard("dhoni")
print(batsman)


# this will remove the  from the names

# replace dhoni with shubman
batsman.add("dhoni")

# remove dhoni
batsman.remove("dhoni")
batsman.add("shubman gill")
print(batsman)

# update
batsman.update(["suryavanshi"])
batsman.update(["sky", "tilak", "jadeja"])
batsman.remove("tilak")

print(batsman)

# union of two different sets
bangalore = {"electronic city", "mg road", "cubbon park"}
chennai = {"guindy", "omr road", "chepauk", "besant nagar", "mg road", "cubbon park"}
friends = bangalore.union(chennai)

print(friends)

# intersection of two set
print(bangalore.intersection(chennai))

# check if an element is present inside

chennai = {"guindy", "omr road", "chepauk", "besant nagar"}
for area in chennai:
    if area == "guindy":
        print(True)

print("guindy" in chennai) # el in set / tuple / list
print("Guindy" in chennai)
print("guindy" in chennai)

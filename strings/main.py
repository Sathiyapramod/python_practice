name = "john doe john"

# printing the first character of the string
print(name[0])


# printing the last character of the string
print(name[len(name) - 1])


# slicing the string
# 1st to 3rd
print(name[0:3])  # joh
# 2nd to 4th
print(name[2:5])  # hn
# 5th to 8th
print(name[5:9])  # doe


# 3rd character onwards
print("3rd character onwards ", name[2:])

# upto 8th character
print("upto 8th character", name[:8])


# reversing
print(name[::-1])

# print every 2nd character from the string
content = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(content[0 : len(content) : 2])


# upper()
print(name.upper())  # JOHN DOE JOHN
# lower()
print(name.lower())  # john doe john
# capitalize()
print(name.capitalize())  # John doe john
# replace()
print(name.replace(" ", "-"))  # john-doe-john
print(name.replace(",", "0"))  # same output: john doej
# count() ->
print(name.count("j"))  # 2
# strip()

content = " hello world "
print(content)  #  hello world
print(content.strip())  # hello world


# find() -> find substring

sentence = "the sun rises in the east"
print(sentence.find("rises"))  # 8
print(sentence.find("-"))  # -1

# split()
students = "maria,steve,john"
print(students.split(","))  # ["maria","steve","john"]

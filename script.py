name = "dulquer salmaan"

# output : quer sal
result = ""
for i in range(3, 10 + 1, +1):
    result = result + name[i]
print(result)


print(name[3 : 10 + 1])

# r salmaan
print(name[6 : 14 + 1])

# dul
print(name[0 : 2 + 1])

# quer salmaan
print(name[3:])

address = "pune,delhi ,bangalore,chennai"
length = len(address)
print(address[0 : length - 10])
print(address[0 : length - 11])

# first 20 characters
print(address[: 28 + 1])

print(address.upper())

name = "D VIJAYAKUMAR"
print(name.lower())

student = "hello world"
print(student[6:].capitalize())

names = "apple,banana, orange"
print(names.split(","))
print(names.split("-"))
print(names.split("+"))
print(names.split("a"))
print(names.split())
# print(names.split(""))
print(names.split(" "))


content = "    hello   world         "
print(content)
print(content.strip(""))


# find()
name = "Dulquer Salmaan"
print(name)
print(name.find("S"))
print(name.find("s"))
# print(name.find(8))
print(name.find("8"))
print(name.find("uer"))


# replace()
# u with a
print(name.replace("u", "a"))

sentence = "delhi is the capital of india"
# delhi to chennai
print(sentence.replace("delhi", "chennai"))
print(sentence.replace("Delhi", "chennai"))


# count
name = "avadi vijayakumar"
print(name.count("a"))
print(name.count("y"))  # 1
print(name.count(""))
print(len(name))

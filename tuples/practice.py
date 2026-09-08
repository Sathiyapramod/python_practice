a = (1, 2, 3, 4)
b = ("sathish", "siva", "rithanya")

print(a + b)

for i in zip(a, b):
    print(i)

gifts = ("pen", "paper", "book", "greeting", "cards")

# first = gifts[0]
# second = gifts[1]
first, second, third, fourth, fifth = gifts
# ("pen", "paper", "book", "greeting", "cards")

print(first)  # pen
print(second)  # paper
print(third)  # ['book','greeting']
print(fourth)  # cards
print(fifth)


marks = (88, 91, 96, 98, 93)

tamil, *others, social = marks
print(tamil)
print(social)
print(others)

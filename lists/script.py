students = ["rithanya", "vetri", "kevin", "pugazh"]
name_greater_than_5 = []

for name in students:
    l = len(name)
    print(l)
    if l > 5:
        # append
        name_greater_than_5.append(name)

# print(name_greater_than_5)

# output = [students[i] for i in range(0, len(students)) if len(students[i]) > 5]

output = [name for name in students if len(name) > 5]


print(output)

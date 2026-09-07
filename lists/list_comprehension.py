nums = [10, 20, 30, 40, 50]

# each element I am making some changes
# mapping

# add 2 to each number
# [12,22,32,42,52]

# option 1
# output = []
# for i in range(0, len(nums)):
#     output.append(nums[i] + 2)
# print(output)

# option 2
# [<expression> for <variable> in <range/full_list> <condition>]

output = [nums[i] * 2 for i in range(0, 3)]
print(output)
students = ["RITHANYA", "VETRI", "KEVIN", "PUGAZH"]

# revised_list = []
# for i in range(0, len(students), +1):
#     temp = students[i].upper()
#     revised_list.append(temp)
# print(revised_list)

# option 2
revised_list = [el.capitalize() for el in students]
print(revised_list)

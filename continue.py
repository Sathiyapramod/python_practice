# print the day address as follows
# 1 for sunday
# 2 for monday a
# and so on
# 7 for saturday

# skip wednesday


for i in range(1, 7 + 1):
    if i == 4:  # wednesday address is 4
        continue
    print("Day is", i)

# Find the sum of all even numbers from 1 to N using a for loop. (get user input)

x = int(input("enter the numbers"))
total = 0

for i in range(2, x + 1, +2):
    # print(i)
    total = total + i
    #print(total)

print("total of all even numbers is ", total)

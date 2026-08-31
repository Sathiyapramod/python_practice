"""
take a number as input (parameter)
1 -> print sunday
2 -> print monday
3 -> tuesday

7 -> saturday

any other input
greater than 7
lesser than 1

print "invalid"

"""


def print_days(x):
    if x == 1:
        print("sunday")
    elif x == 2:
        print("monday")
    elif x == 3:
        print("tuesday")
    elif x == 4:
        print("wednesday")
    elif x == 5:
        print("thursday")
    elif x == 6:
        print("friday")
    elif x == 7:
        print("saturday")
    else:
        print("invalid")


print_days(x=7) # ok
print_days(10) # ok
print_days(True) # true is taken as 1 # some problem is there
print_days("2") # error
print_days(0)

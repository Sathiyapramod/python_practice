def display_weekdays(x):
    if x > 7 or x < 1:
        print("invalid")
    elif x == 1:
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


display_weekdays(-2)
display_weekdays(3)
display_weekdays(83)
display_weekdays(5)
display_weekdays(1)

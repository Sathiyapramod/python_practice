# get 10 batsman scores from the user
# store the scores inside the list
# list name => india

india = []  # length here is zero

# start from zero
# end at 10

for i in range(0, 10):
    # get score one by one from zero to 10
    user_score = int(input("enter your score"))

    # append each "user_score" one by one
    india.append(user_score)
    print(india)

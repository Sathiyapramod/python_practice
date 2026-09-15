'''
days => 900

2 years => 365 * 2 = 730
5 months => 5 * 30 = 150
2 weeks => 2 * 7 = 14
6 days => 6 

'''

n = int(input("enter the total days here \n"))
years = n // 365  # 2
# 170 days
# 900 - 2*365
years_bal = n % 365  # 170
print(years, "years")
# print(years_bal)
months = years_bal // 30  # 5
print(months, "months")
months_bal = years_bal % 30
# print(months_bal)
weeks = months_bal // 7
print(weeks, "weeks")
days = months_bal % 7
print(days, "days")

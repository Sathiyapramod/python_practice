# ==============================================================================
#                      PYTHON DEBUGGING CONTEST
# Find and fix the bugs in each problem so the program runs correctly!
# ==============================================================================

# ------------------------------------------------------------------------------
# PROBLEM 1: Discount Eligibility Checker (Shopping & Finance)
# Goal: Calculate the final price after a discount.
# Rules:
# 1. apply_discount(price, rate) computes: price - (price * rate / 100).
# 2. is_eligible(age, total) checks if age >= 60 OR total > 1000.
# 3. get_final_price(age, total) applies 20% discount if eligible, else 5%.
# ------------------------------------------------------------------------------

"""
def apply_discount(price, rate):
    return price - price * rate / 100

def is_eligible(age, total):
    if age >= 60 or total > 1000:
        return True
    else:
        return False

def get_final_price(age, total):
    if is_eligible:
        final = apply_discount(total, 20)
    else:
        final = apply_discount(total, 5)
    return Final

user_age = int(input("Age: "))
user_total = float(input("Total: "))
print("Final Amount:", get_final_price(user_age, user_total))
"""

# ------------------------------------------------------------------------------
# PROBLEM 2: Temperature Alert System (Physics & Environment)
# Goal: Convert Celsius to Fahrenheit and determine the alert level.
# Rules:
# 1. to_fahrenheit(c) formula is: (c * 9/5) + 32.
# 2. get_alert(temp_f) returns: "HOT" if temp_f > 100, "COLD" if temp_f < 32,
#    else "NORMAL".
# 3. process_temp(c_list) loops through temperatures, converts them,
#    and prints each alert.
# ------------------------------------------------------------------------------

"""
def to_fahrenheit(c):
    return c * 9/5 + 32

def get_alert(temp_f):
    if temp_f > 100:
        return "HOT"
    elif temp_f < 32:
        return "COLD"
    else
        return "NORMAL"

def process_temp(c_list):
    i = 0
    while i <= len(c_list):
        f = to_fahrenheit(c_list[i])
        alert = get_alert(f)
        print("Temp:", f, "Status:", alert)
        i += 1

temps = [0, 25, 40]
process_temp(temps)
"""


# ------------------------------------------------------------------------------
# PROBLEM 3: Grade Classifier & Honor Roll (Education & Grading)
# Goal: Compute the average of 3 marks and check honor roll status.
# Rules:
# 1. calculate_avg(m1, m2, m3) returns the average of the 3 marks.
# 2. is_honor_roll(avg, attendance) returns True if avg >= 85 AND attendance >= 90.
# 3. evaluate_student(m1, m2, m3, att) prints "Honor Roll" or "Regular Pass".
# ------------------------------------------------------------------------------

"""
def calculate_avg(m1, m2, m3):
    return m1 + m2 + m3 / 3

def is_honor_roll(avg, attendance):
    if avg >= 85 and attendance >= 90:
        return True
    return False

def evaluate_student(m1, m2, m3, att):
    average = calculate_avg(m1, m2, m3)
    if is_honor_roll(average, att) = True:
        print("Honor Roll")
    else:
        print("Regular Pass")

evaluate_student(80, 90, 95, 92)
"""


# ------------------------------------------------------------------------------
# PROBLEM 4: Electricity Bill Calculator (Utility Billing)
# Goal: Calculate total utility charge based on units consumed and tax.
# Rules:
# 1. compute_base_bill(units) charges 5 per unit if units <= 100,
#    else 8 per unit.
# 2. add_tax(bill_amount) adds a 10% tax (multiply bill by 1.10).
# 3. generate_receipt(units) calculates final bill and prints the result.
# ------------------------------------------------------------------------------


"""
def compute_base_bill(units):
    if units <= 100:
        return units * 5
    else:
        return units * 8


def add_tax(bill_amount):
    return bill_amount * 1.10


def generate_receipt(units):
    base = compute_base_bill(units)
    total = add_tax(base)
    return total


unit_input = int(input("Enter Units: "))
final_bill = generate_receipt
print("Total Bill:", final_bill)
"""


# ------------------------------------------------------------------------------
# PROBLEM 5: ATM Cash Withdrawal Verifier (Banking System)
# Goal: Verify if a user can withdraw a requested amount from their balance.
# Rules:
# 1. is_multiple_of_hundred(amount) checks if amount % 100 == 0.
# 2. has_sufficient_balance(balance, amount) checks if balance >= amount.
# 3. process_withdrawal(balance, amount) prints "Transaction Successful"
#    if BOTH rules are satisfied, otherwise prints "Transaction Failed".
# ------------------------------------------------------------------------------


"""
def is_multiple_of_hundred(amount):
    if amount % 100 == 0:
        return True
    return False


def has_sufficient_balance(balance, amount):
    if balance >= amount:
        return True
    return False


def process_withdrawal(balance, amount):
    if is_multiple_of_hundred(amount) and has_sufficient_balance(balance, amount):
        print("Transaction Successful")
    else:
        print("Transaction Failed")


acc_balance = 5000
req_amount = 1250
process_withdrawal(acc_balance)
"""

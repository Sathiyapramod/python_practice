# ==========================================
# INTERACTIVE QUIZ: TODAY'S BITWISE OPERATORS
# (Left Shift, Bitwise AND, Bitwise OR)
# Guess the output before running each line!
# ==========================================

# ------------------------------------------
# SECTION 1: LEFT SHIFT (<<)
# Formula hint: a * (2^n)
# ------------------------------------------
a = 5
print(a << 1)  # Q1: What is the output? 10
print(a << 2)  # Q2: What is the output? 20
print(a << 3)  # Q3: What is the output? 40


b = 12
print(b << 1)  # Q4: What is the output? 24


# ------------------------------------------
# SECTION 2: BITWISE AND (&)
# Hint: 1 & 1 = 1, otherwise 0
# ------------------------------------------
print(5 & 3)  # Q5: What is 101 & 011? #   001 -> 1
print(8 & 4)  # Q6: What is 1000 & 0100? #   0000 -> 0
print(15 & 7)  # Q7: What is 1111 & 0111?   0111 -> 7
print(12 & 10)  # Q8: What is 1100 & 1010? #     1000 -> 8
print(9 & 9)  # Q9: What is 1001 & 1001? 1001


# ------------------------------------------
# SECTION 3: BITWISE OR (|)
# Hint: 0 | 0 = 0, otherwise 1 (If either bit is 1, result is 1)
# ------------------------------------------
print("Or operation in bitwise")
print(5 | 3)  # Q10: What is 101 | 011?
print(8 | 4)  # Q11: What is 1000 | 0100?
print(12 | 10)  # Q12: What is 1100 | 1010?
print(0 | 7)  # Q13: What is 000 | 111?
print(6 | 6)  # Q14: What is 110 | 110?


# ------------------------------------------
# SECTION 4: MIXED CHALLENGES FOR TODAY
# ------------------------------------------
# Check if a number is Odd or Even using & 1
print(14 & 1)  # Q15: What is the output?
print(27 & 1)  # Q16: What is the output?

# Combining Left Shift and Bitwise AND
print((4 << 1) & 7)  # Q17: What is the output?

# Combining Left Shift and Bitwise OR
print((3 << 1) | 1)  # Q18: What is the output?

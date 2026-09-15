'''
import math
side = float(input("enter the side of the triangle:"))

# Formula: Area = (Root 3 / 4) * sideSquare
area = (math.sqrt(3) / 4) * side

print("Area of the equilateral triangle:", area)
'''

import math
side = float(input("enter the side of the triangle:"))

# Formula: Area = (Root 3 / 4) * sideSquare
# option 1
area = (math.sqrt(3) / 4) * side * side

# option 2
area = ((3 ** 0.5) / 4) * (side ** 2)

print("Area of the equilateral triangle:", area)





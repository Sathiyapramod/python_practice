# Write a function named calculate_square(x)


# It should take a positive integer as parameter
def calculate_square(x):

    # Calculate the square
    # Store the result in a variable named result.
    global result 
    result = x**2

    # Print the result inside the function
    print("inside function", result)


# first time call
calculate_square(10)
# After calling the function, try to print result outside the function.

print("outside function", result)

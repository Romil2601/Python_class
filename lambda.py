# What is lambda function in Python?
# A lambda function is a small anonymous function that can take any number of arguments, 
# but can only have one expression.

# Syntax:
# lambda arguments: expression


# Example 1: Difference between normal function and lambda function
# Regular function
# def add(x, y):
#     return x + y
# print(add(5, 3))

# Using lambda function
# add_lambda = lambda x, y: x + y
# print(add_lambda(5, 3))


# Example 2: Using lambda with reduce()
# from functools import reduce
# ans = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
# print(ans)

# Example 3: Using lambda with map()
# from functools import reduce
# ans = list(map(lambda x: x * x, [ 2, 3, 4, 5]))
# print(ans)

# Example 4: Celsius to Fahrenheit conversion using lambda
# temp = int(input("Enter temperature in Celsius: "))
# ans = list(map(lambda x: (x * 9/5) + 32, [temp]))
# print(f"Temperature in Fahrenheit: {ans[0]}")
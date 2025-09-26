# What is list?
# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
# Lists are used to store multiple items in a single variable.
# Collections is of data types that are used to store multiple data which can be string, integer, float, boolean etc.

# List functions and methods:
# list() function: It creates a list in Python.
# sum() function: It returns the sum of all items in an iterable.

# Why List is changeable?
# Lists are mutable, meaning their content can be changed after creation. You can add, remove, or modify elements in a list.

# Example 1: 
# my_list = [3, 25.78, "Hello", True]
# print(my_list)  # Output: [3, 25.78, 'Hello', True]
# for i in my_list:
#     print(i, type(i)) #type() function is used to know the data type of the variable.
    
# Example 2: Add all elements of the list
num_list = [3,34,56,23,89]
# print(f"Sum of all elements in the List is: {sum(num_list)}")
sum = 0
for i in num_list:
    sum += i
print(f"Sum of all elements in the List is: {sum}")
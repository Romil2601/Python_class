# What is a tuple?
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
# Tuples are used to store multiple items in a single variable.

# Tuple functions and methods:
# tuple() function: It creates a tuple in Python.
# count() method is used to return the number of occurrences of a specified value in the tuple
# index() method is used to return the index of the first occurrence of a specified value in the tuple.
# len() function: It returns the length of the tuple.
# sorted() function: It returns a sorted list of the tuple's elements.
# type() function: It returns the data type of the variable.
# del statement is used to delete the entire tuple.

# Example 1:
# a = (11, 45, 23, 67, 89)
# print(a)  # Output: (11, 45, 23, 67, 89)
# print(type(a))  # Output: <class 'tuple'>

# b = 45, 78, 90, 23
# print(b)  # Output: (45, 78, 90, 23)

# c = 11, 
# print(c)  # Output: (11,)

# d = ('Romil', 'Abhijit', 'Dhruv', 'Dharmishta')
# print(d)  # Output: ('Romil', 'Abhijit', 'Dhruv', 'Dharmishta')
# print(type(d))  # Output: <class 'tuple'>
# print(f"{d.count('Romil')} is present at index {d.index('Romil')} in the tuple.")
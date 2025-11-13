# What is File Handling ?
# File handling in Python refers to the process of creating, reading, writing, and manipulating files using built-in functions and methods.
# Python provides various functions to handle files, such as open(), read(), write(), and close().
# Files can be of different types, such as text files, binary files, CSV files, etc.

# read() - This function reads the entire content of a file as a single string.
# readline() - This function reads a single line from a file.
# readlines() - This function reads all the lines of a file and returns them as a list of strings.
# tell() - This function returns the current position of the file pointer.
# seek() - This function is used to change the position of the file pointer.

# Example 1: Creating and Writing to a File with open('example.txt', 'w') as file:
# file = open('lambda.py', 'r')
# content = file.read(50)  # Read first 50 characters
# print(content)

# Example 2: Reading from a File which is other folder ||  \ is taken as a character, so for the path we use \\.
# file = open('C:\\Users\\romil\\Downloads\\Practice 1.txt', 'r') 
# content = file.read()
# print(content)

# Example 3: Using readlines() to read all lines into a list
# file = open('file_handling.py', 'r')
# lines = file.readline() # readline reads only one line
# print(lines)
# -------------------------------------------
# file = open('lambda.py', 'r')
# lines = file.readlines() # readlines reads all lines and stores in list 
# print(lines)

# Example 4: Reading a whole file using readline().
# file = open('lambda.py', 'r')
# while True:
#     line = file.readline()
#     if not line:
#         break
#     print(line)

# Example 5: Using tell().
# file = open('lambda.py', 'r')
# print(f"Before Reading {file.tell()}")
# lines = file.readlines() 
# print(lines)
# print(f"After Reading {file.tell()}")

# Example 6: Using seek().
# file = open('lambda.py', 'r')
# file.seek(10)
# print(f"Before Reading {file.tell()}")
# lines = file.readlines() 
# print(lines)
# print(f"After Reading {file.tell()}")
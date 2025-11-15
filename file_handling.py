# What is File Handling ?
# File handling in Python refers to the process of creating, reading, writing, and manipulating files using built-in functions and methods.
# Python provides various functions to handle files, such as open(), read(), write(), and close().
# Files can be of different types, such as text files, binary files, CSV files, etc.

# read() - This function reads the entire content of a file as a single string.
# readline() - This function reads a single line from a file.
# readlines() - This function reads all the lines of a file and returns them as a list of strings.
# tell() - This function returns the current position of the file pointer.
# seek() - This function is used to change the position of the file pointer.
# write() - This function is used to write a string to a file.
# writelines() - This function is used to write a list of strings to a file.


# ------------ Read Method ------------


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


# ------------ Write Method ------------


# Example 7: Writing to a File
# file = open('example.txt', 'w') 
# file.write("Hello, World!\n")
# file.writelines(["This is line 1.\n", "This is line 2.\n"])
# file.close()
# data = input("Enter data to write to file: ")
# file.write(data)
# print("Data written to file successfully.")
# file.close()

# Example 8: Using for loop until the keyword 'exit' is entered
# file = open('user_input.txt', 'w')
# while True:
#     data = input("Enter data to write to file (type 'exit' to stop): ")
#     if data.lower() == 'exit':
#         break
#     file.write(data + '\n')
# file.close()

# Example 9: Different syntax
# with open('lambda.py', 'r') as file:
#     data = file.read()
#     print(data)

# Example 10: Menu Driven Program with Function
#   1. Read
#   2. Write
#   3. CopyFile
#   4. Append
#   5. Exit
# def read_file():
#     file_name = input("Enter the file name to read: ")
#     with open(file_name, 'r') as file:
#         data = file.read()
#         print(data)

# def write_file():
#     file_name = input("Enter the file name to write: ")
#     with open(file_name, 'w') as file:
#         data = input("Enter data to write to file: ")
#         file.write(data)
#         print("Data written to file successfully.")

# def copy_file():
#     file_name = input("Enter the file name to copy: ")
#     copy_file_name = input("Enter the name for the copied file: ")
#     with open(file_name, 'r') as file:
#         data = file.read()
#     with open(copy_file_name, 'w') as file:
#         file.write(data)
#         print("File copied successfully.")
        
# def append_file():
#     file_name = input("Enter the file name to append: ")
#     with open(file_name, 'a') as file:
#         data = input("Enter data to append to file: ")
#         file.write(data + '\n')
#         print("Data appended to file successfully.")
        
# while True:
#     print("Menu:")
#     print("1. Read")
#     print("2. Write")
#     print("3. CopyFile")
#     print("4. Append")
#     print("5. Exit")
#     choice = input("Enter your choice (1-5): ")
    
#     if choice == '1':
#         read_file()
#     elif choice == '2':
#         write_file()
#     elif choice == '3':
#         copy_file()
#     elif choice == '4':
#         append_file()
#     elif choice == '5':
#         print("Exiting the program.")
#         break
#     else:
#         print("Invalid choice. Please try again.")


# Example 11: Dumping JSON Data
# import json
# data = {'Age': 24, 'Address': 'CG Road'}
# with open('file1.json' , 'w') as file:
#     json.dump(data, file) # ----- Dump method
#     print(" Data entered successfully")

# Example 12: Using While Loop with writelines
# file = open('user_input.txt', 'w')
# lines = []
# while True:
#     data = input("Enter data to write to file (type 'exit' to stop): ")
#     if data.lower() == 'exit':
#         break
#     lines.append(data + '\n')
# file.writelines(lines)
# file.close()

# Example 13: Copy File.
# f1 = open('user_input.txt', 'r')
# f2 = open('copy_user_input.txt', 'w')
# f2.write(f1.read())
# f1.close()
# f2.close()
# print("File copied successfully.")

# Example 14: Loading JSON Data
# import json
# with open('file1.json' , 'r') as file:
#     data = json.load(file) # ----- Load Method
#     print(" Data entered successfully")
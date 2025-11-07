# What is file in python?
# In Python, a file is a resource used to store data on a persistent storage device, such as a hard drive or SSD. 
# Files can be used to read and write data, allowing programs to save information between executions. 
# Python provides built-in functions and modules to work with files, such as opening, reading, writing, and closing files.

# what is __init__.py file in python?
# The __init__.py file is used to mark a directory as a Python package.
# It can also be used to execute package initialization code or set the __all__ variable, 
# which defines the public interface of the package.

# Built-in functions in python:
# open() - Opens a file and returns a file object.
# read() - Reads the content of a file.
# write() - Writes data to a file.
# close() - Closes a file.

# Example of open file handling in python:
# file = open("example.txt", "w")  # Open a file in write mode
# file.write("Hello, World!")      # Write data to the file
# file.close()                      # Close the file

# Example of reading a file in python:
# file = open("example.txt", "r")  # Open a file in read mode
# content = file.read()             # Read the content of the file
# print(content)                    # Print the content
# file.close()                      # Close the file

# Example of appending to a file in python:
# file = open("example.txt", "a")  # Open a file in append mode
# file.write("\nAppended line.")    # Append data to the file
# file.close()                      # Close the file
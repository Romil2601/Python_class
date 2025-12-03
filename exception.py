# What is Exception in Python?
# Exception in Python is a built-in class that serves as the base class for all built-in exceptions. 
# It is used to handle errors and other exceptional conditions that may occur during the execution of a program. 
# When an error occurs, Python raises an exception, which can be caught and handled using try-except blocks.

# try - The try block is used to wrap the code that may potentially raise an exception.
# except - The except block is used to catch and handle the exception.
# else - The else block is executed if no exceptions are raised in the try block.
# finally - The finally block is executed regardless of whether an exception was raised or not.
# raise - The raise statement is used to manually raise an exception.
# custom exceptions - You can create your own custom exceptions by defining a new class that inherits from the Exception class.

# Types of Exceptions in Python:
# ValueError - Wrong type/value (e.g., int("abc"))
# ZeroDivisionError - Dividing by zero
# TypeError - Wrong type of operation
# FileNotFoundError - File doesn't exist
# IndexError - List index out of range
# KeyError - Dictionary key not found
# NameError - Variable not defined
# CustomException - Custom rules

# Types of Built-in Exceptions:
# ArithmeticError
# BufferError
# LookupError
# ImportError
# ModuleNotFoundError
# SyntaxError
# IndentationError

# Example 1: Handling Division by Zero Exception
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = num1 / num2
# except ValueError:
#     print("Invalid input! Please enter numeric values.")
# except ZeroDivisionError:
#     print("Error! Division by zero is not allowed.")
# else:
#     print("The result is:", result)
# finally:
#     print("Execution completed.")
    
    
# Example 2: Custom Exception
# import traceback
# class LenghtException(Exception):
#     pass
# try:
#     name = input("Enter your name: ")
#     if len(name) > 20:
#         raise LenghtException("Name must be at most 20 characters long.")
#     address = input("Enter your address: ")
#     if len(address) < 15:
#         raise LenghtException("Address must be at least 15 characters long.")
# except LenghtException as le:
#     print("LenghtException:", le)
#     traceback.print_exc()
    
# Example 3:

# no =int(input("Enter a number: "))
# print(no)
# ans = no/2
# print(f"After division {ans}")
# dict1 = {"name": "Vishwraj" , "age": 24}
# print(f"Dictnary value is {dict1['name']}")
# with open("abc", "r") as file:
#     data = file.read()

# Example 4:    
# try:
#     no = input("Enter a number: ")
#     no1 =int(no)
#     print(f"value is {no1}")
#     ans = no1/2
#     print(f"(Ans){ans}")
# except:
#     print("There is an exception")

# Example 5:
 
# try: 
#     no = input("Enter a number: ")
#     no_1 =int(no)
#     print(f"value is {no_1}")

#     ans = no_1/2
#     print(ans)
# except ZeroDivisionError:
#     print("There is a zero division error")
# except ValueError:
#     print(" There is value error")
# finally:
#     print("Have Great Day Ahead!")

# Example 6:

# import traceback
# try:
#     no = input("Enter a number: ")
#     no1 =int(no)
#     print(f"value is {no1}")

#     ans = no 1/0
#     print(f"Ans"{ans})
# except ZeroDivisionError:
#     print("There is a zero division error")
#     traceback.print_exc()
# except ValueError:
#     print(" There is value error")
#     traceback.print_exc()
# finally:
#     print("Have glorious Day Ahead!")
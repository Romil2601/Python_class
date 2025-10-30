# What is a function?
# A function is a block of code that performs a specific task.

# Types of functions:
# 1. Built-in functions: Functions that are pre-defined in Python.
# 2. User-defined functions: Functions that are defined by the user to perform specific tasks.
#    More Types of user-defined functions:
#    a. Default functions: Functions that do not take any parameters.
#    b. Keyword functions: Functions that take parameters with keywords.
#    c. Variable functions: Functions that take a variable number of parameters: *args and **kwargs.

# *args - Allows a function to accept any number of positional arguments as a tuple.
# **kwargs - Allows a function to accept any number of keyword arguments as a dictionary.

# Function declaration using def keyword.
# def greet():
#     print("Hello from user_defined.py!")

# def close():
#     print("Goodbye from user_defined.py!")

# # Calling the function.
# greet()
# close()


# def greet(name): # Here 'name' is a parameter.
#     return f"Hello, {name}! Welcome to user_defined.py!"

# def close(name):
#     return f"Goodbye, {name}! See you next time!"

# # Calling the function.
# print(greet("Romil"))
# print(close("Romil"))


# def data(name, grade, age):
#     print(f"Name : {name}", f"Grade : {grade}", f"Age : {age}")
    
# num = int(input(" Enter the number of students : "))    
# for i in range(num):
#     name = input("Enter Name : ")
#     grade = input("Enter Grade : ")
#     age = input("Enter Age : ")
#     print(" ")
#     data(name, grade, age)


# Function to check even or odd
# def num(k):
#     if k % 2 == 0:
#         return f"{k} is Even"
#     else:
#         return f"{k} is Odd"

# number = int(input(" Enter the number of values you want to check : "))
# for i in range(number):
#     value = int(input("Enter a number: "))
#     print(num(value))


# Function to check if the number is prime or not.
# def prime(n):
#     if n <= 1:
#         return f"{n} is not a Prime Number"
#     for i in range(2, n):
#         if n % i == 0:
#             return f"{n} is not a Prime Number"
#     return f"{n} is a Prime Number"
# num = int(input("Enter a number to check if it's prime: "))
# print(prime(num))

# Create a function to check if string is palindrome or not.
# def palindrome(s):
#     if s == s[::-1]:
#         return f'"{s}" is a Palindrome'
#     else:
#         return f'"{s}" is not a Palindrome'

# str = input("Enter a string to check if it's palindrome: ")
# print(palindrome(str))


# Default Function
# def greet():
#     return "Hello! Welcome to user_defined.py!"
# def close():
#     return "Goodbye! See you next time!"

# print(greet())
# print(close())


# Keyword Function
# def greet(name="Guest"):
#     return f"Hello, {name}! Welcome to user_defined.py!"
# print(greet())
# print(greet(name="Romil"))

# def personDetails(**kwargs):
#     print("Person Details:", kwargs)
#     if kwargs['Age'] >=30:
#         print (f"{kwargs['Name']} is eligible for Senior Citizen benefits.")
#     else:    
#         print (f"{kwargs['Name']} is not eligible for Senior Citizen benefits.")
# personDetails(Name="Romil", Age=24, Course="Python", Grade="A")
# personDetails(Name="Vishwraj", Age=35, City="Dholka")


# Variable Function
# def student_info(*args, **kwargs):
#     for i in args:
#         print(f"Student Name: {i}")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
        
# student_info("Romil", "Aarav", "Saanvi", Age=20, Grade="A", Course="Python")

# def data(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)
    
# data(101, "Romil", 24, Course="Python", Grade="A")


# Lab Task : Create a function which has fix 'name' parameter and other details as variable parameters.
# def student_details(name, *args, **kwargs):
#     print(f"Student Name: {name}")
#     print("Other Details (Positional):", args)
#     print("Other Details (Keyword):", kwargs)

# student_details("Romil", 24, "A", Course="Python", City="New York")


# Example : 
# def addition(*args):
#     # sum(args)
#     # total = 0
#     # for num in args:
#     #     if type(num) == int or type(num) == float:
#     #         total += num
#     # return total

# print(addition (12,23))
# print(addition (23,657,"abhs",5656))
# print(addition (23,345,5656,6789))
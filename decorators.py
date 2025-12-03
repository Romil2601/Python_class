# What is a Decorator in Python?
# A decorator in Python is a special type of function that modifies the behavior of another function or method.
# Decorators allow you to wrap another function to extend its behavior without modifying its code.
# They are often used for logging, access control, instrumentation, and caching.

# Example 1: Simple Decorator
# def decorat(func):
#     def wrapper():
#         print("Before executing the function.")
#         func()
#         print("After executing the function.")
#     return wrapper
# @decorat
# def greet():
#     print("Good Morning!")
# @decorat
# def add():
#     print(12 + 23)
# greet()
# add()

# Example 2: Time Check
# import time
# def time_check(func):
#     def wrapper():
#         print(f"Start at {time.time():.2f}")
#         func()
#         print(f"End at {time.time():.2f}")
#     return wrapper

# @time_check
# def count():
#     c = 0
#     for i in range(100):
#         c += 1
# count()

# Example 3: Decorator with Arguments
# def decorat(func):
#     def wrapper(name, age):
#         print("Before executing the function.")
#         func(name, age)
#         print("After executing the function.")
#     return wrapper
# @decorat
# def person_info(name, age):
#     print(f"Name: {name}, Age: {age}")
# person_info("Alice", 30)

# Example 4: Arguments
# def decorator_Parameter(func):
#     def wrapper(*args,**kwargs):
#         print(args)
#         print(kwargs)
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
# @decorator_Parameter
# def greet(name, age, address):
#     print(f"Hello, {name}! You are {age} years old. You live at {address}.")
# greet("Romil", 25, address = "CG Road")

# Example 5: Logging Example
# from functools import wraps
# import logging
# logging.basicConfig(level=logging.INFO)

# def log_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         logging.info(f"Executing {func.__name__}")
#         logging.info(f"Arguments: args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"Returned: {result}")
#         return result
#     return wrapper
# @log_decorator
# def count(num):
#     c = 0
#     for i in range(1, num):
#          c += 1
#          return c
# @log_decorator
# def greet(name, msg):
#     return f"Hello {name}, {msg}"

# greet(name = "Romil", msg = "Welcome!")
# count(20)
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
#     reversed_str = ""
#     for char in s:
#         reversed_str = char + reversed_str
#     if s == reversed_str:
#         return f"{s} is a Palindrome"
#     else:
#         return f"{s} is not a Palindrome"

# str = input("Enter a string to check if it's palindrome: ")
# print(palindrome(str))
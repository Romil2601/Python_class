# Encapsulation : It is like a capsule which wrap different type of data in a single unit using on encapsulation we can prevent data from outside the users.
# There are two types of encapsulation in python:
# 1. Getter - Setter Method
# 2. Prevent Data (Private - Public)

# Example : Getter - Setter Method
# class Student:
#     def __init__(self, name, subject, score):
#         print("Welcome to Student Class: ")
#         self.name = name      # Private Attribute
#         self.subject = subject  # Public Attribute
#         self.score = score    # Public Attribute

#     def setName(self, name):      # Setter Method
#         self.name = name
        
#     def getName(self):            # Getter Method
#         return self.name
        
#     def setSubject(self, subject):
#         self.subject = subject
        
#     def getSubject(self):
#         return self.subject
        
#     def setScore(self, score):
#         self.score = score
        
#     def getScore(self):
#         return self.score
        
# obj = Student("Vishwraj", "DA", 95)
# print(obj.getName())                # Accessing Private Attribute using Getter Method
# obj.setName("Romil")             # Modifying Private Attribute using Setter Method
# print(obj.getName())               # Accessing Modified Private Attribute using Getter Method
# obj.setSubject("Python")
# print(obj.getSubject())



# Data Hiding : Using of encapsulation we can hide or prevent data from outside the users.
# There are 3 Visibility Modes in Python:
# 1. Public: Accessible from anywhere.
# 2. Protected: Accessible within the class and its subclasses.
# 3. Private: Accessible only within the class.

# Public : by default all the attributes and methods are public in python. We can access from anywhere from the class and outside the class.
# Eg. :  name, subject (no underscore is used to declare public members)

# Private : This kind of data member or member function can only access by class which is restricted by outside of class. 
#           This is used for data hiding and preventing data from outside the class.
# Eg. :  __score, __name (double underscore is used to declare private members)

# Protected : This is only access by own class and subclass but this is not working 100% as a data hiding because we can access protected members outside the class using single underscore(_).
# Eg. : _subject, _name (single underscore is used to declare protected members)

# Example 1: Private and Public
# class Student:
#     def __init__(self):
#         self.name = "Riya"
#         self.__score = 95
        
#     def display(self):
#         print(self.name)
#         print(self.__score)
        
# obj = Student()
# print(obj.name)
# print(obj.__score)  # This will raise an AttributeError
# print(obj._Student__score)  # Accessing private member using name mangling

# obj.display()

# Example 2: Private and Public
# class Products:
#     def __init__(self):
#         self.mobile = 15000          # Public Attribute
#         self.__laptop = 25000      # Private Attribute

#     def display(self):
#         print(f"Product Name: {self.mobile}")
#         print(f"Product Price: {self.__laptop}")
    
#     def changePrice(self, newPrice):
#         self.__laptop = newPrice
        
# obj = Products()
# obj.display()

# obj.mobile = 20000
# obj.display()

# obj.__laptop = 85000   # This will not change the private attribute and also not raise any error
# obj.display()

# print("---------------------------")
# obj.changePrice(115000)
# obj.display()
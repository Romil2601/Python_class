# Polymorphism : Poly means many and morphism means forms
#                Polymorphism is derived from greek word which means one named method has different forms.

# Polymorphism has 2 methods:
# 1. Method Overloading     - compile time polymorphism
# 2. Method Orriding        - runtime polymorphism

# Method Overloading: When one class contain same name method with different parameters, it is called method overloading.
#                     In Python method overloading , which is not supported.

# Method Overriding: When parent and child have same name methods, it is called method overriding.

# Example 1: Overloading
# class Student:
#     def dsiplay(self):
#         print("Student class is here")
        
#     def display(self, name):
#         print("This is 2nd method", name)

# obj = Student()
# obj.display("Romil") # In Python, Method Overloading is not working 100%.

# Example 2: Overriding
# class Parent:
#     def display(self):
#         print("This is parent class.")
        
# class Child(Parent):
#     def display(self):
#         Parent.display(self)  # Parent Property Called
#         print("This is child class.")
        
# obj = Child()
# obj.display()

# Example 3:
# class Parent():
#     def __init__(self, name):
#         self.name = name
        
#     def display(self):
#         print(self.name)
        
# class Child(Parent):
#     def __init__(self, name, subject):
#         Parent.__init__(self, name)
#         self.subject = subject
        
#     def display(self):
#         Parent.display(self)
#         print(self.subject)
        
# obj = Child("Romil","Python")
# obj.display()
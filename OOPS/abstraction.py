# Abstraction : ABC : Abstract Base Class
#               Abstraction which is represent only few information not allocated background information.
#               For data hiding purpose, we use abstraction.
#               Abstract class which contain only method declaration without method deffination.


# Example 1:
# from abc import abstractclassmethod,ABC

# class Parent(ABC):
#     @abstractclassmethod
#     def display():
#         pass
    
# class A(Parent):
#     def display(self):
#         print("A class is here.")
        
# class B(Parent):
#     def display(self):
#         print("B class is here.")
        
# a = A()
# a.display()
# b = B()
# b.display()


# Example 2:
# from abc import ABC, abstractclassmethod

# class RBI(ABC):
#     @abstractclassmethod
#     def ROI():
#         pass
    
# class SBI(RBI):
#     def ROI(self):
#         return 8.5
    
# class HDFC(RBI):
#     def ROI(self):
#         return 7.5
    
# sbi = SBI()
# hdfc = HDFC()

# print(sbi.ROI())
# print(hdfc.ROI())
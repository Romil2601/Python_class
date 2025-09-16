# c_no = 12345678 #numeric
# name = "romil" #string
# subject = ['python', 'java', 'c++'] #list
# day_shift = True #boolean

# print(type(c_no))
# print(type(name))
# print(type(subject))
# print(type(day_shift))
# print(type(23.567))

# number1 = input("Enter first number ")
# number2 = input("Enter second number ")
# add = int(number1) + int(number2)
# print("Addition is ", add)

# pi = input("Enter value of pi ")
# num = input("Enter your number ")
# name = input("Enter your name ") 

# print("Hello ", name)
# print("Value of pi is ", float(pi)) 
# print("Your number is ", int(num))

# add = float(pi) + int(num)
# print("Addition is ", add)

# print("romil","Ahmedabad",sep="###",end="100")
# print("380002","parimal-garden",sep="$$")

# name="Tops\tTechnologies"
# print(name)
# name="Tops\bTechnologies"
# print(name)
# print("tops","technogies",sep="\n")
# print("tops","technogies",sep="\t")
# print("tops technogies",end="\n")
# print("tops technogies",end="\t")

# name="Romil\tRaja"
# print(name)
# name="Romil\bRaja"
# print(name)
# print("Romil","Raja",sep="\n")
# print("Romil","Raja",sep="\t")
# print("Romil Raja",end="\n")
# print("Romil Raja",end="\t")

# a = input("Enter value: ")
# print(f"{a} * 10 is {a * 3}")


# Swap two numbers without using third variable
# num1 = 12 
# num2 = 22
# num1 , num2 = num2 , num1
# print(f"num1 is {num1} and num2 is {num2}")

# Swap two numbers using third variable
# num1 = 12 
# num2 = 22
# temp = num1
# num1 = num2
# num2 = temp
# print(f"num1 is {num1} and num2 is {num2}")

month = input("Enter month: ")
if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    print("31 Days")
elif month == "April" or month == "June" or month == "September" or month == "November":
    print("30 Days")
elif month == "February":
    print("28 Days")
else:
    print("Invalid month")

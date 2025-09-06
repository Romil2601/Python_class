#match case
# print("\n1. Addition")
# print("\n2. Subtraction")
# print("\n3. Multiplication")
# print("\n4. Division")
# num1 = int(input("\nEnter first number: "))
# num2 = int(input("\nEnter second number: "))
# choice = int(input("\nEnter your choice: "))
# match choice:
#     case 1:
#         print(f"\nAddition of {num1} and {num2} is {num1 + num2}")
#     case 2:
#         print(f"\nSubtraction of {num1} and {num2} is {num1 - num2}")
#     case 3:
#         print(f"\nMultiplication of {num1} and {num2} is {num1 * num2}")
#     case 4:
#         if num2 != 0:
#             print(f"\nDivision of {num1} and {num2} is {num1 / num2}")
#         else:
#             print("\nDivision by zero is not allowed")
#     case _:
#         print("\nInvalid choice")

#Calculator using match case
print("\n1. Addition : + ")
print("\n2. Subtraction : - ")
print("\n3. Multiplication : * ")
print("\n4. Division : / ")
num1 = int(input("\nEnter first number: "))
num2 = int(input("\nEnter second number: "))
choice = input("\nEnter your choice symbol: ")
match choice:
    case '+':
        print(f"\nAddition of {num1} and {num2} is {num1 + num2}")
    case '-':
        print(f"\nSubtraction of {num1} and {num2} is {num1 - num2}")
    case '*':
        print(f"\nMultiplication of {num1} and {num2} is {num1 * num2}")
    case '/':
        if num2 != 0:
            print(f"\nDivision of {num1} and {num2} is {num1 / num2}")
        else:
            print("\nDivision by zero is not allowed")
    case _:
        print("\nInvalid choice")

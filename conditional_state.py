# Conditional Statements -  1. if
# 						    2. if-else
# 						    3. if-elif-else

num = int(input("Enter a number: "))
# if statement - executes a block of code if the condition is true
if num > 0:
    print(f"{num} is a positive number")
# if-else statement - executes one block of code if the condition is true, otherwise executes another block of code
else:
    print(f"{num} is not a positive number")
# if-elif-else statement - checks multiple conditions and executes the corresponding block of code for the first true condition
if num > 0:
    print(f"{num} is a positive number")
elif num == 0:
    print(f"{num} is zero")
else:
    print(f"{num} is a negative number")



age = int(input("Enter your age: "))
if age >= 0 and age <=2:
    print("You are a infant.")
elif age >= 3 and age <18:
    print("You are minor.")
elif age >= 18 and age <=50:
    print("You are an adult.")
else:
    print("You are a senior.")


marks = int(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    print("You got A+ grade.")
elif marks >= 80 and marks < 90: # else-if = elif
    print("You got A grade.")
elif marks >= 70 and marks < 80:
    print("You got B grade.")
elif marks >= 50 and marks < 70:
    print("You got C grade.")
else:
    print("You got D grade.")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 != num2:
    print(f"{num1} is not equal to {num2}")
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")

# nested if-else statement - an if-else statement inside another if or else block
num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is a positive number")
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")
elif num == 0:
    print(f"{num} is zero")
else:
    print(f"{num} is a negative number")
# Loops : 1. for loop -  used to iterate over a sequence (like a list, tuple, dictionary, set, or string).
#         2. while loop - repeatedly executes a block of code as long as a specified condition remains true.

# for loop
# for i in range(5):
#     print(f"Iteration {i}")

# while loop
# count = 1
# while count <= 10:
#     print(f"Count is {count}")
#     count += 1

# print the sum of first 10 natural numbers
# sum = 0
# for i in range(1, 11):
#     sum += i
# print(f"The sum of numbers from 1 to 10 is {sum}")

# print the multiplication of the first 5 numbers (factorial of 5)
# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))
# product = 1
# for i in range(start, end + 1):
#     product *= i
# print(f"The multiplication of numbers from {start} to {end} is {product}")

#addition of even numbers between 1 to 20
# sum = 0
# for i in range(2, 21):
#     if i % 2 == 0:
#         sum += i
# print(f"The addition of even numbers between 1 to 20 is {sum}")

# print odd numbers between 1 to 20
# sum = 0
# for i in range(1, 21):
#     if i % 2 != 0:
#         sum += i
# print(f"The addition of odd numbers between 1 to 20 is {sum}")


# print multiplication table of a number :

# for-loop
# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")

# while-loop
# num = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(f"{num} x {i} = {num * i}")
#     i += 1


# Sum of digits of a number
# lst_num = [1, 2, 3, 4, 5]
# sum = 0
# for i in lst_num:
#     sum += i
# print(f"The sum of digits is {sum}")

#while loop+
# j = 10 
# while j >= 1:
#     print(f"Iteration {j}")
#     j -= 1 

# Multiplication Table of a number in
# num = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(f"{num} x {i} = {num * i}")
#     i += 1

# Multiplication Table of a number in reverse order
# num = int(input("Enter a number: "))
# i = 10
# while i >= 1:
#     print(f"{num} x {i} = {num * i}")
#     i -= 1

# Prime Number Check
# num = int(input("Enter a number: "))
# for i in range(2, num):
#     if num % i == 0:
#         print(f"{num} is not a prime number")
#         break
# else:
#     print(f"{num} is a prime number")

# Print Prime Numbers from 1 to 100
# for num in range(1, 101):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(f"{num} is a prime number")

# Print Prime Numbers from 1 to 100 using while loop
# num = 1
# while num <= 100:
#     i = 2
#     while i < num:
#         if num % i == 0:
#             break
#         i += 1
#     else:
#         print(f"{num} is a prime number")
#     num += 1

# Find the prime number given by the user using for loop
# num = int(input("Enter no "))
# temp = 1
# for i in range(2,num):
#     if num%i==0:
#         print(f"{num} is not prime number")
#         temp=1
#         break
#     else:
#         print(f"{num} is prime number")
#         temp=0

# if temp==1:
#     print(f"{num} is not prime number")
# else:
#     print(f"{num} is prime number")



# Find Number of Digits in a Number
# count = 0
# num = int(input("Enter a number: "))
# while num != 0:
#     rem = num % 10
#     num = num // 10
#     print(f"Remainder is {rem} and number is {num}")
#     count += 1
# print(f"Number of digits is {count}")

# Sum of the numbers in a specific range with a increment of 3
# sum = 0
# for x in range(2,21,3):
#     print(x)
#     sum += x
# print(f"The sum is {sum}")

# Sum of the numbers in a specific range with a decrement of 2
# sum = 0
# for x in range(20, 1, -2):
#     print(x)
#     sum += x
# print(f"The sum is {sum}")

# Armstrong Number
# num = int(input("Enter a number: "))
# sum = 0
# temp = num
# while temp != 0:
#     digit = temp % 10
#     sum += digit ** 3
#     temp //= 10
# if num == sum:
#     print(f"{num} is an Armstrong number")
# else:
#     print(f"{num} is not an Armstrong number")


# Fibonacci Series
# num = int(input("Enter the number of series: "))
# prev = 0
# next = 1
# for i in range(num):
#     print(prev)
#     sum = prev + next
#     prev = next
#     next = sum


# Fibonacci Series using while loop
# num = int(input("Enter the number of series: "))
# prev = 0
# next = 1
# i = 0
# while i < num:
#     print(prev)
#     sum = prev + next
#     prev = next
#     next = sum
#     i += 1

# Pattern Printing
# rows = int(input("Enter number of rows: "))
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()


# Reverse Pattern Printing
# rows = int(input("Enter number of rows: "))
# for i in range(rows, 0, -1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

# Pattern Printing in numbers
# rows = int(input("Enter number of rows: "))
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# Number Pattern Printing as below : 1 , 3 , 5 , 7 ...
# num = int(input("Enter number of rows: "))
# count = 1
# for i in range(1, num + 1):
#     for j in range(1, i + 1):
#         print(count, end=" ")
#     print()
#     count += 2

# Loop with continue statement
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)

# Loop with pass statement
# for i in range(1, 11):
#     if i == 5:
#         pass
#     print(i)
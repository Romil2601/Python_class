#Loops : 1. for loop -  used to iterate over a sequence (like a list, tuple, dictionary, set, or string).
#        2. while loop - repeatedly executes a block of code as long as a specified condition remains true.

# for loop
# for i in range(5):
#     print(f"Iteration {i}")

# while loop
# count = 0
# while count < 5:
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
sum = 0
for i in range(2, 21):
    if i % 2 == 0:
        sum += i
print(f"The addition of even numbers between 1 to 20 is {sum}")

# print odd numbers between 1 to 20
sum = 0
for i in range(1, 21):
    if i % 2 != 0:
        sum += i
print(f"The addition of odd numbers between 1 to 20 is {sum}")
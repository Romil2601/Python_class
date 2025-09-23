# Find area of circle using PI
pi = 3.14
r = float(input("Enter radius of circle: "))
area = pi * r * r
print(f"Area of circle with radius {r} is: {area}")

# Find maximum number using max function
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
max_num = max(num1, num2, num3)
print(f"Maximum number is: {max_num}")

# Find maximum number using ternary function
max_num_ternary = num1 if num1 > num2 and num1 > num3 else num2 if num2 > num3 else num3
print(f"Maximum number using ternary function is: {max_num_ternary}")

# Find Simple Interest
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))
si = (p * r * t) / 100
print(f"Simple Interest is: {si}")

# Find Compound Interest
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))
ci = p * (1 + r / 100) ** t - p
print(f"Compound Interest is: {ci}")

# Print Character using ASCII value
ascii_value = int(input("Enter ASCII value: "))
character = chr(ascii_value)
print(f"Character corresponding to ASCII value {ascii_value} is: {character}")

# Convert binary to decimal using int()
binary_num = input("Enter a binary number: ")
decimal_num = int(binary_num, 2)
print(f"Decimal equivalent of binary {binary_num} is: {decimal_num}")

# Convert Fahrenheit to Celsius and vice versa
Fah = float(input("Enter temperature in Fahrenheit: "))
Cel = (Fah - 32) * 5 / 9
print(f"Temperature in Celsius is: {Cel}")

Cel = float(input("Enter temperature in Celsius: "))
Fah = (Cel * 9 / 5) + 32
print(f"Temperature in Fahrenheit is: {Fah}")

# Print Multiplication table of given number
num = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Print Number of days for given month name
month = input("Enter month name: ").lower()
if month in ['january', 'march', 'may', 'july', 'august', 'october', 'december']:
    days = 31
elif month in ['april', 'june', 'september', 'november']:
    days = 30
else:
    days = 28
print(f"Number of days in {month.capitalize()} is: {days}")

# Print number of digits and character in a string accepted from user 
# [ c is variable for looping through each character of string & sum() is function to count the number of digits and characters]
str1 = input("Enter a string: ")
num_digits = sum(c.isdigit() for c in str1)
num_chars = sum(c.isalpha() for c in str1)
print(f"Number of digits in the string is: {num_digits}")
print(f"Number of characters in the string is: {num_chars}")

# Accept and print number from a user until it enters zero
num = int(input("Enter a number (0 to stop): "))
while num != 0:
    print(f"You entered: {num}")
    num = int(input("Enter a number (0 to stop): "))
print("Program ended as you entered 0.")

# Count number of digits in a number
num = int(input("Enter a number: "))
num_digits = sum(c.isdigit() for c in str(num))
print(f"Number of digits in {num} is: {num_digits}")

# Print list of items iteratively [using split() to separate items by commas & strip() to remove any extra spaces]
items = input("Enter items separated by commas: ").split(',')
for i in items:
    print(f"Item: {i.strip()}")

# Print even numbers fall between two given numbers
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
print(f"Even numbers between {start} and {end} are:")
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i)

# Write a program to display number names of a entered numbers between 0-999
num = input("Enter a number between 0 and 999: ")
words = ["zero", "one", "two", "three", "four", 
         "five", "six", "seven", "eight", "nine"]
if num.isdigit() and 0 <= int(num) <= 999:
    result = " ".join(words[int(d)] for d in num)
    print(result)
else:
    print("Invalid input! Please enter a number between 0 and 999.")

# Write a program to write series like 1/1! + 2/2! + 3/3! + .....n/n!
n = int(input("Enter a number n to calculate the series 1/1! + 2/2! + ... + n/n!: "))
factorial = 1
series_sum = 0
for i in range(1, n + 1):
    factorial *= i
    series_sum += i / factorial
print(f"Sum of the series 1/1! + 2/2! + ... + {n}/{n}! is: {series_sum}")

# Write a program to display numbers which are divisible by 13 from range
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print(f"Numbers divisible by 13 between {start} and {end} are:")
for i in range(start, end + 1):
    if i % 13 == 0:
        print(i)

# Print even numbers from a given range without using % operator
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print(f"Even numbers between {start} and {end} are:")
for i in range(start, end + 1):
    if (i // 2) * 2 == i:
        print(i)

# Print pattern like odd column is 1 and even column is 2 but in pyramid form
rows = int(input("Enter number of rows for the pyramid pattern: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j % 2 == 0:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()

# Print pattern like column goes A B C D E but in pyramid form
rows = int(input("Enter number of rows for the pyramid pattern: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    print()

# Print Arithmetic Progression series
a = int(input("Enter the first term (a): "))
d = int(input("Enter the common difference (d): "))
n = int(input("Enter the number of terms (n): "))
print("Arithmetic Progression series:")
for i in range(n):
    term = a + i * d
    print(term, end=" ")

# Print Fibonacci series
n = int(input("Enter the number of terms in Fibonacci series: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Print Factorial
n = int(input("Enter the number of terms in Factorial series: "))
print("Factorial series:")
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    print(factorial, end=" ")

# Check whether the given number is prime or not
num = int(input("Enter a number to check if it's prime: "))
temp = 0
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not a prime number")
        temp = 1
        break
if temp == 0:
    print(f"{num} is a prime number")

# Print list of prime numbers between given range
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print(f"Prime numbers between {start} and {end} are:")
for num in range(start, end + 1):
    temp = 0
    for i in range(2, num):
        if num % i == 0:
            temp = 1
            break
    if temp == 0 and num > 1:
        print(num, end=" ")

# Check whether the given number is armstrong or not
num = int(input("Enter a number to check if it's Armstrong: "))
sum_of_cubes = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_cubes += digit ** 3
    temp //= 10
if sum_of_cubes == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

# Print half of string in uppercase and other half in lower case
str1 = input("Enter your name: ")
mid = len(str1) // 2
print("Output:", str1[:mid].upper() + str1[mid:].lower())

# Write a program to check whtether the character is vowel or consonant
char = input("Enter a character: ").lower()
if char in 'aeiou':
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant.")

# Print the count of vowels and consonants in a string
str1 = input("Enter a string: ").lower()
vowels = 0
consonants = 0
for char in str1:
    if char in 'aeiou':
        vowels += 1
    elif char.isalpha():
        consonants += 1
print(f"Vowels: {vowels}, Consonants: {consonants}")

# Write all prime numbers from 1 to n
n = int(input("Enter a number: "))
print(f"Prime numbers from 1 to {n} are:")
for num in range(2, n + 1):
   temp = 0 
   for i in range(2, num):
       if num % i == 0:
           temp = 1
           break
   if temp == 0:
       print(num, end=" ")

# Write a program to find GCD of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
while num2 != 0:
    temp = num2
    num2 = num1 % num2
    num1 = temp
print(f"GCD is: {num1}")

# Write a program to find all perfect numbers from given range
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print(f"Perfect numbers between {start} and {end} are:")
for num in range(start, end + 1):
    if num > 1:
        divisor = 0
        for i in range(1, num):
            if num % i == 0:
                divisor += i
        if divisor == num:
            print(num, end=" ")

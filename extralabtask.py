

# -------- Extra Lab Tasks ---------


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
for i in range(1, num + 1):
    multiply = num * i
    print(f"{num} * {i} = {multiply}")

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

# Check whether the given number is armstrong or not
num = int(input("Enter a number to check if it's Armstrong: "))
sum_of_cubes = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_cubes += digit ** 3 # sum_of_cubes = sum_of_cubes + digit ** 3
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

# Accept a string from the user and print it in uppercase if the length of the string is greater than 5, else print it in lowercase using a function.
name = input("Enter Your Name: ")
if len(name) > 5:
    print(name.upper())
else:
    print(name.lower())
    
    
# -------- Functions based programs ---------

    
# Write a function that accepts a string and returns the string in alternating uppercase and lowercase characters.
msg = input("Enter the sentence")
def lower_upper(msg):
    result = ""
    for i in range(len (msg)):
        if i % 2 == 0:
            result += msg[i].upper()
        else:
            result += msg[i].lower()
    return result
print(lower_upper(msg))

# Write a function that accepts a list of numbers and returns the average of the numbers, excluding any zero values.
nums_input = input("Enter the list of numbers: ")
nums = []
def average(nums):
    total = 0
    count = 0
    for num in nums:
        if num != 0:
            total += num
            count += 1
    return total / count if count > 0 else 0
print("Average (excluding zeros):", average)

# Write a function that accepts a string and returns True if the string is a valid email address (contains "@" and "."), otherwise False.
email = input("Enter Valid Email: ")
def valid_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False
print(valid_email(email))
    
# Write a function that accepts a list of integers and returns the second largest number in the list.
num1 = input("Enter the list of numbers: ")
num_lst = []
def second_largest(num_lst):
    num_lst = list(set(num_lst))
    num_lst.sort()
    return num_lst[-2] if len(num_lst) >= 2 else None

print(f"The Second Largest Number is {second_largest(num_lst)}")

# Write a function that accepts a list of numbers and returns a new list with only the numbers that are divisible by 3.
def divisible(num):
   for i in num :
       if i % 3 == 0:
           print(i)
num = input("Enter the list of numbers: ")
new_lst = list(map(int, num.split(",")))
divisible(new_lst)

# Write a function that accepts a list of numbers and returns a new list with the squares of all the numbers in the list.
def square(num):
    for i in num:
        print(i * i)
num = input("Enter the list of numbers: ")
new_lst = list(map(int, num.split(",")))
square(new_lst)

# Write a function that accepts a string and counts how many vowels are in the string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))

# Write a function that accepts a list of strings and returns the longest string in the list.
def longest_string(str_lst):
    longest = ""
    for s in str_lst:
        if len(s) > len(longest):
            longest = s
    return longest
str_input = input("Enter the list of strings: ")
str_lst = str_input.split(",")
print("Longest string:", longest_string(str_lst))

# Write a function that accepts a number and checks if it is an Armstrong number.
def armstrong(num):
    sum_of_cubes = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit ** 3
        temp //= 10
    return sum_of_cubes == num
number = int(input("Enter a number: "))
if armstrong(number):
    print(f"{number} is an Armstrong number.")

# Write a function that accepts a number and returns the sum of its digits.
def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total
num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))

# Write a function that accepts a list of strings and returns a new list with only the strings that have an odd length.
def odd(str_lst):
    result = []
    for s in str_lst:
        if len(s) % 2 != 0:
            result.append(s)
    return result
str_input = input("Enter the list of strings: ")
str_lst = str_input.split(",")
print("Strings with odd length:", odd(str_lst))

# Write a function that accepts a string and a substring, and returns True if the substring is found in the string, otherwise False.
def substring(s, sub):
    if sub in s:
        return True
    else:
        return False
string = input("Enter a string: ")
sub_string = input("Enter a substring: ")
print(substring(string, sub_string))

# Write a function that accepts a list of numbers and returns a new list with all the numbers that are divisible by both 2 and 3.
def divisible(num):
    for i in num:
        if i % 2 == 0 and i % 3 == 0:
            print(i)
num = input("Enter the list of numbers: ")
new_lst = list(map(int, num.split(",")))
divisible(new_lst)

# Write a function that accepts two strings and returns the common characters between them.
def common(str1, str2):
    common_chars = set(str1) & set(str2)
    return ''.join(common_chars)
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
print("Common characters:", common(string1, string2))

# Write a function count_character(string, char) that accepts a string and a character, and returns the number of times the character appears in the string.
def count(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count
string = input("Enter a string: ")
char = input("Enter a character to count: ")
print(f"Character '{char}' appears {count(string, char)} times in the string.")

# Write a function concatenate_with_separator(lst, separator) that accepts a list of strings and a separator string, then returns a new string where all elements of the list are joined using the separator.
def concatenate(lst, separator):
    return separator.join(lst)
str_input = input("Enter the list of strings: ")
str_lst = str_input.split(",")
sep = input("Enter a separator: ")
print("Concatenated string:", concatenate(str_lst, sep))

# Write a function merge_dicts(dict1, dict2) that accepts two dictionaries and returns a single dictionary that contains the merged key-value pairs from both dictionaries.
def merge(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print("Merged dictionary:", merge(dict1, dict2))

# Write a function longest_word(sentence) that accepts a sentence and returns the longest word in the sentence.
def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
sentence = input("Enter a sentence: ")
print("Longest word:", longest_word(sentence))

# Write a function create_frequency_dict(lst) that accepts a list and returns a dictionary where the keys are the elements of the list, and the values are the count of how often each element appears.
def create_frequency_dict(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
lst_input = input("Enter the list of items: ")
lst = lst_input.split(",")
print("Frequency dictionary:", create_frequency_dict(lst))

# Write a function merge_lists_into_dict(list1, list2) that accepts two lists of equal length and merges them into a dictionary where the keys are the indices (0 to n-1) and the values are the elements from both lists.
def merge_lists_into_dict(list1, list2):
    merged_dict = {}
    for i in range(len(list1)):
        merged_dict[i] = (list1[i], list2[i])
    return merged_dict
list1 = ['key1', 'key2', 'key3']
list2 = ['value1', 'value2', 'value3']
print("Merged dictionary from lists:", merge_lists_into_dict(list1, list2))


# -------- Dictionary based programs ---------


# Count frequency of list items and write in into dictionary :input List1 = [1, 2, 2, 3, 4, 1, 4, 5, 5, 6, 7, 7]
List1 = [1, 2, 2, 3, 4, 1, 4, 5, 5, 6, 7, 7]
freq = {}
for i in List1:
    if i in freq:
        freq[i] += 1   
    else:
        freq[i] = 1    
print(freq)

# Convert keys in upper case and put it in value
city_names = {'ahmedabad' : "" , 'baroda': "" , 'surat' : ""}
for k in city_names.keys():
    v = k.upper()
print(city_names)

# Find the length of keys and put in value
city_names = {'ahmedabad' : "" , 'baroda': "" , 'surat' : ""}
for k in city_names.keys():
    v = len(k)
    city_names[k] = v
print(city_names)


# -------- Map Function based programs ---------


# Write a Python program that uses `map()` to convert a list of strings to uppercase. Input: `['apple', 'banana', 'cherry']` - Output: `['APPLE', 'BANANA', 'CHERRY']`
fruits = ['apple', 'banana', 'cherry']
upper_fruits = list(map(str.upper, fruits))
print(upper_fruits)

# Write a Python program that uses `map()` to apply a function that converts a list of temperature values in Celsius to Fahrenheit. Input: `[0, 25, 100]` Output: `[32.0, 77.0, 212.0]`
celsius = [0, 25, 100]
def c_to_f(c):
    formula = (c * 9/5) + 32
    return formula
fahrenheit = list(map(c_to_f, celsius))
print(fahrenheit)


# -------- Tuple based programs ---------


# Write a program to accepts a list of integers and returns a tuple with the sum of all positive numbers and the sum of all negative numbers
num = [10, -5, 3, -1, 7, -2]
sum_positive = sum(i for i in num if i > 0)
sum_negative = sum(i for i in num if i < 0)
print("Tuple of sums:", tuple((sum_positive, sum_negative)))

# Write a program that takes a list of numbers and returns a tuple containing the sum and product of all the numbers.
num = [1, 2, 3, 4, 5, 6]
total = tuple(sum(num))
product = 1
for i in num:
    product *= i
print("Sum:", total)
print("Product:", tuple(product))


# -------- List based programs ---------


# Write a program to remove all items from a list that are less then 5.
num = [2, 3, 5, 6, 8, 1, 4, 9, 7]
num = [i for i in num if i >= 5]
print(num)  # Output: [5, 6, 8, 9, 7]

# Write a program to find common among 2 lists.
lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]
common = [i for i in lst1 if i in lst2]
print("Common elements:", common)

# Write a program to sort a list of strings by their length
str_list = ["apple", "banana", "cherry", "date"]
str_list.sort(key=len)
print("Sorted by length:", str_list)

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
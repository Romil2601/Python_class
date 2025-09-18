# What is string in python?
# A string is a sequence of characters enclosed within single quotes (' ') or double quotes (" ").
# Strings are immutable, meaning once created, their content cannot be changed.

# str() function: It converts other data types to string.
# len() function: It returns the length of the string.
# lower() method: It converts all characters in the string to lowercase.
# upper() method: It converts all characters in the string to uppercase.
# title() method: It capitalizes the first letter of each word in the string.
# capitalize() method: It capitalizes the first letter of the string.
# strip() method: It removes leading and trailing whitespace from the string.
# find() method: It returns the lowest index of the substring if found in the string. If not found, it returns -1.
# replace() method: It replaces occurrences of a specified substring with another substring.
# count() method: It returns the number of occurrences of a substring in the string.
# isdigit() method: It checks if all characters in the string are digits.
# isalpha() method: It checks if all characters in the string are alphabetic.
# isalnum() method: It checks if all characters in the string are alphanumeric.
# split() method: It splits the string into a list of substrings based on a specified delimiter.
# join() method: It joins a list of strings into a single string with a specified delimiter

# Example usage of string functions and methods
# my_string = "  Hello, World! Welcome to Python programming.  "
# print(f"Original String: '{my_string}'")
# print(f"Length of String: {len(my_string)}")
# print(f"Lowercase: '{my_string.lower()}'")
# print(f"Uppercase: '{my_string.upper()}'")
# print(f"Title Case: '{my_string.title()}'")
# print(f"Capitalized: '{my_string.capitalize()}'")
# print(f"Stripped: '{my_string.strip()}'")


# Example 
# c_name = "Tops Technologies"
# print(c_name.upper())
# print(c_name.lower())
# print(c_name.title())
# print(c_name.capitalize())

# Accept 5 strings from user and Perform all 4 operations on each string
# for i in range(5):
#     user_input = input(f"Enter string {i+1}: ")
#     print(user_input.upper())
#     print(user_input.lower())
#     print(user_input.title())
#     print(user_input.capitalize())

# Example of Find Methods
# str1 = "Hello, welcome to the world of Python programming. Python is great!"
# str2 = str1.find("Python")
# print(f"First occurrence of 'Python': {str2}")
# not_found = str1.find("Java")
# print(f"First occurrence of 'Java': {not_found}")

# Example of Replace Methods
# original_str = "I love programming. Programming is fun."
# new_str = original_str.replace("Programming", "Coding")
# print(f"Original String: {original_str}")
# print(f"Modified String: {new_str}")

# Example of Replace method by taking input from user
# str1 = input("Enter a string: ")
# old_substr = input("Enter the substring to be replaced: ")
# new_substr = input("Enter the new substring: ")
# modified_str = str1.replace(old_substr, new_substr)
# print(f"Original String: {str1}")
# print(f"Modified String: {modified_str}")

# Example of Count Methods
# text = "Python is great. Python is dynamic. Python is easy to learn."
# count = text.count("Python")
# print(f"Occurrences of 'Python': {count}")

# Example program of Count method
# str1 = "Cat is a animal and Dog is also a animal"
# str_find = str1.count("animal")
# print(f"Occurrences of 'animal': {str_find}")

# Example of Split Methods
# sentence = "Python is a popular programming language"
# words = sentence.split()
# print(f"Original Sentence: {sentence}")
# print(f"List of Words: {words}")

# Example of Join Methods
# words_list = ["Python", "is", "fun"]
# joined_string = " ".join(words_list)
# print(f"List of Words: {words_list}")
# print(f"Joined String: {joined_string}")

# Declare 4 strings and check whether they are digit, alpha or alnum
# str1 = "Tops"
# str2 = "12345"
# str3 = "Tops@123"
# str4 = "Tops tech"
# print(str1.isdigit() , str1.isalpha() , str1.isalnum())
# print(str2.isdigit() , str2.isalpha() , str2.isalnum())
# print(str3.isdigit() , str3.isalpha() , str3.isalnum())
# print(str4.isdigit() , str4.isalpha() , str4.isalnum())
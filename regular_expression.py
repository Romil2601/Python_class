# What is a Regular Expression in Python?
# A regular expression (regex or regexp) is a sequence of characters that forms a search pattern.
# Regular expressions are used for pattern matching within strings, allowing for complex search and manipulation operations.
# In Python, the 're' module provides support for working with regular expressions.

# Core Functions in the 're' Module:
# 1. re.match(pattern, string): Checks for a match only at the beginning of the string.
# 2. re.search(pattern, string): Searches the entire string for a match.
# 3. re.findall(pattern, string): Returns a list of all non-overlapping matches in the string
# 4. re.sub(pattern, repl, string): Replaces occurrences of a pattern with a specified string.
# 5. re.split(pattern, string): Splits a string by the occurrences of a pattern.



# Example 1: Basic Pattern Matching
# import re
# pattern = r"cat"
# text = "The cat sat on the mat."
# match = re.search(pattern, text)
# if match:
#     print("Match found:", match.group())
# else:
#     print("No match found.")
    
# Example 2: 
# import re
# msg = "This is beautiful morning"
# match = re.search(r"is", msg)
# print("Match found:", match)  # match object gives the position of the first occurrence

# if match:
#     print(f"{match.start()} - {match.end()}")  # start and end positions of the match

# Example 3: 
# import re
# msg = "Morning is beautiful, Today is beautiful"
# match = re.search(r"\AMorning", msg)        # \A asserts position at start of the string
# print(match)

# msg1 = "This is Good Morning, Good Afternoon"
# match = re.search(r"\d+", "test 123 456")
# print(match)
# match = re.findall(r"\d+", "test 123 456")
# print(match)

# Example 4:
# import re
# msg = "This is IND, This is NZD"
# match = re.search(r"[D-Z]$", msg)       # [] is used for range of characters, $ asserts position at the end of the string
# print(match)
# match = re.search(r"NZD$", msg)
# print(match)

# Differentiate between re.match() and re.search():
# import re
# text = "Hello, welcome to the world of Python."
# match_result = re.match(r"welcome", text)
# print("re.match result:", match_result())  # Output: None, as 'welcome' is not at the start
# search_result = re.search(r"welcome", text)
# print("re.search result:", search_result())  # Output: 'welcome'

# Example 5: Find Total number of phone numbers in a text
# import re
# text = "Contact us at 1234567890 or 9876543210 for more information"
# phone_numbers = re.findall(r"\d{10}", text)
# print("Phone numbers found:", phone_numbers)
# print("Total phone numbers found:", len(phone_numbers))
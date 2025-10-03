# What is list?
# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
# Lists are used to store multiple items in a single variable.
# Collections is of data types that are used to store multiple data which can be string, integer, float, boolean etc.

# List functions and methods:
# list() function: It creates a list in Python.
# sum() function: It returns the sum of all items in an iterable.
# extend() method is used to add elements of one list to another list.
# clear() method is used to remove all items from the list.
# append() method is used to add an item to the end of the list.
# copy() method is used to create a shallow copy of the list.
# insert() method is used to add an item at a specified index in the list.
# remove() method is used to remove the first occurrence of a specified value from the list.
# pop() method is used to remove an item at a specified index and return it. If no index is specified, it removes and returns the last item.
# count() method is used to return the number of occurrences of a specified value in the list
# index() method is used to return the index of the first occurrence of a specified value in the list.
# reverse() method is used to reverse the order of the list.
# sort() method is used to sort the items of the list in ascending or descending order. Only if all elements are of same data type.
# set() function: It converts a list to a set, removing any duplicate values.
# del statement is used to delete an item at a specified index or delete the entire list.

# Why List is changeable?
# Lists are mutable, meaning their content can be changed after creation. You can add, remove, or modify elements in a list.

# Example 1: 
# my_list = [3, 25.78, "Hello", True]
# print(my_list)  # Output: [3, 25.78, 'Hello', True]
# for i in my_list:
#     print(i, type(i)) #type() function is used to know the data type of the variable.
    
# Example 2: Add all elements of the list
# num_list = [3,34,56,23,89]
# print(f"Sum of all elements in the List is: {sum(num_list)}")
# sum = 0
# for i in num_list:
#     sum += i
# print(f"Sum of all elements in the List is: {sum}")

# Example 3:
# lst = ['Ahmedabad', 'Surat', 'Vadodara', 'Rajkot', 'Bhavnagar']
# lst1 = ['Mumbai', 'Pune', 'Nagpur', 'Nashik', 'Thane']
# lst.extend(lst1) 
# print(lst)

# Example 4: 
# lst = [25.78, "Test", "Ahmedabad", 23]
# lst.clear() 
# print(lst)  # Output: []
# del lst     # This will delete the entire list.
# print(lst)  # This will raise an error because lst is deleted.
# del lst[2]  # This will delete the element at index 2.
# print(lst)  # Output: [25.78, 'Test', 23]
# lst1 = lst.copy()  # This will create a shallow copy of the list.
# print(lst1)  # Output: [25.78, 'Test', 'Ahmedabad', 23]
# lst1 = lst   # This will create a reference to the same list.

# Example 5:
# lst = [25.78, "Test", "Ahmedabad", 23]
# lst1 = [1 ,34, 45, 90, 23]
# print(lst.count("Test"))       # Output: 1
# print(lst.index("Ahmedabad"))  # Output: 2
# lst.insert(2, "Surat")         # This will insert "Surat" at index 2.
# print(lst)                     # Output: [25.78, 'Test', 'Surat', 'Ahmedabad', 23]
# lst.remove("Test")             # This will remove the first occurrence of "Test".
# lst.pop()                      # This will remove and return the last item.
# print(lst)                     # Output: [25.78, 'Surat', 'Ahmedabad']
# lst.reverse()                  # This will reverse the order of the list.
# print(lst)                     # Output: ['Ahmedabad', 'Surat', 25.78]
# lst1.sort()                    # This will sort the list in ascending order. Only if all elements are of same data type.
# print(lst1)                    # Output: [1, 23, 34, 45, 90]
# lst1.sort(reverse=True)        # This will sort the list in descending order. Only if all elements are of same data type.
# print(lst1)                    # Output: [90, 45, 34, 23, 1]
# lst1.sort(key=len)             # This will sort the list based on the length of the elements. Only if all elements are of same data type.
# print(lst1)                    # Output: [1, 23, 34, 45, 90]

# Example 6: All list methods
# lst1 = [34, "Test", "Ahmedabad", 23.78, "Surat", True]
# print(f"Original List: {lst1}")
# lst1.append("Rajkot")          # This will add "Rajkot" at the end of the list.
# print(f"List after append(): {lst1}")
# lst1.insert(2, "Mumbai")      # This will insert "Mumbai" at index 2.
# print(f"List after insert(): {lst1}")
# lst1.remove("Test")           # This will remove the first occurrence of "Test".
# print(f"List after remove(): {lst1}")
# lst1.pop()                    # This will remove and return the last item.
# print(f"List after pop(): {lst1}")
# lst1.pop(1)                   # This will remove and return the item at index
# print(f"List after pop(1): {lst1}")
# print(f"Count of 'Surat' in the List: {lst1.count('Surat')}")
# print(f"Index of 'Ahmedabad' in the List: {lst1.index('Ahmedabad')}") 
# lst1.reverse()                # This will reverse the order of the list.
# print(f"List after reverse(): {lst1}")

# lst_names = ['Romil', 'Abhijit', 'Dhruv']
# print(lst_names[2])  # Output: Dhruv
# print(lst_names[20]) # Output: IndexError: list index out of range
# for i in range(len(lst_names)):
#     print(lst_names[i])
# print(lst_names[-3]) # Output: Romil
# for i in range(len(lst_names)-1, -1, -1):
#     print(lst_names[i])

# Slicing in List
# lst = ['Romil', 'Abhijit', 'Dhruv', 'Dharmishta']
# print(lst[1:])    # ['Abhijit', 'Dhruv', 'Dharmishta']
# print(lst[1:3])   # ['Abhijit', 'Dhruv']
# print(lst[::-1])  # ['Dharmishta', 'Dhruv', 'Abhijit', 'Romil']

# Convert Names into uppercase from list
# name = ['Romil', 'Abhijit', 'Dhruv', 'Dharmishta']
# total_len = len(name)
# for i in range(total_len):
#     name[i] = name[i].upper()
# print(name)

# Find length of each string from list
# str_list = ['Romil', 'Abhijit', 'Dhruv', 'Dharmishta']
# for i in str_list:
#     print(f"Length of '{i}' is {len(i)}")

# Find the largest string from the list
# str_list = ['Romil', 'Abhijit', 'Dhruv', 'Dharmishta']
# temp = 0
# for i in str_list:
#     if len(i) > temp:
#         temp = len(i)
# print(f"Largest string length is {temp}")

# Create valid email id list from existing list
# lst = ['test@gmail.com', 'test.com', 'fdgregmail.com', 'romilraja@yahoo.com','rte@.boplk']
# valid_email = []
# for i in lst:
#     if '@' in i and '.' in i:
#         if 'gmail' in i or 'yahoo' in i:
#             valid_email.append(i)
# print(f"Valid email ids are: {valid_email}")

# Give the second heighest number from the list
# num_list = [23, 45, 67, 89, 12, 90, 34, 90, 67]
# num_list = list(set(num_list))
# num_list.sort()                
# print(f"Second highest number is: {num_list[-2]}")

# Find number of vowels in the string from list and add into a new list
# str_list = ['Romil', 'Abhijit', 'Dhruv', 'Dharmishta']
# vowels = 'aeiouAEIOU'
# vowel_count = []
# for i in str_list:
#     count = 0
#     for j in i:
#         if j in vowels:
#             count += 1
#     vowel_count.append(count)
# print(f"Number of vowels in each string: {vowel_count}")
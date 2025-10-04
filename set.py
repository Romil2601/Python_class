# What is set?
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
# Sets are used to store multiple items in a single variable.

# Set functions and methods:
# set() function: It creates a set in Python.
# add() method is used to add an item to the set.
# clear() method is used to remove all items from the set.
# copy() method is used to create a shallow copy of the set.
# remove() method is used to remove a specified item from the set. If the item is not found, it raises a KeyError.
# discard() method is used to remove a specified item from the set. If the item is not found, it does nothing.
# pop() method is used to remove and return an arbitrary item from the set. Raises KeyError if the set is empty.
# union() method is used to return a set that is the union of two sets.
# intersection() method is used to return a set that is the intersection of two sets.
# difference() method is used to return a set that is the difference of two sets.
# symmetric_difference() method is used to return a set that is the symmetric difference of two sets.
# isdisjoint() method is used to return True if two sets have no elements in common.
# issubset() method is used to return True if all elements of the set are present in another set.
# issuperset() method is used to return True if all elements of another set are present in the set.
# len() function: It returns the number of items in the set.

# Example 1:
# set_num = {1, 2, 3, 4, 5, 1, 2, 5} # Duplicate values will be removed
# set_str = {"Apple", "Banana", "Orange"}
# set_mixed = {1, "Hello", 3.14, True}
# print(set_num)    # Output: {1, 2, 3, 4, 5}
# print(set_str)    # Output: {'Apple', 'Banana', 'Orange'}
# print(set_mixed)  # Output: {1, 3.14, 'Hello'}
# set_num.add(6)  # Adding an item to the set
# print(set_num)  # Output: {1, 2, 3, 4, 5, 6}
# set_str.remove("Banana")  # Removing an item from the set
# print(set_str)  # Output: {'Apple', 'Orange'}   
# set_mixed.clear()  # Removing all items from the set
# print(set_mixed)  # Output: set()
# set_copy = set_num.copy()  # Creating a shallow copy of the set
# print(set_copy)  # Output: {1, 2, 3, 4, 5, 6}

# Example 2:
# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}
# print(set_a.union(set_b))  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
# print(set_a.intersection(set_b))  # Output: {4, 5}
# print(set_a.difference(set_b))  # Output: {1, 2, 3}
# print(set_a.symmetric_difference(set_b))  # Output: {1, 2, 3, 6, 7, 8}
# print(set_a.isdisjoint(set_b))  # Output: False
# print(set_a.issubset(set_b))  # Output: False
# print(set_a.issuperset(set_b))  # Output: False

# Example 3: but using operators
# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}
# # Union1
# print(set_a | set_b)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
# # Intersection
# print(set_a & set_b)  # Output: {4, 5}
# # Difference
# print(set_a - set_b)  # Output: {1, 2, 3}
# # Symmetric Difference
# print(set_a ^ set_b)  # Output: {1, 2, 3, 6, 7, 8}
# # Is Disjoint
# print(set_a.isdisjoint(set_b))  # Output: False
# # Is Subset
# print(set_a.issubset(set_b))  # Output: False
# # Is Superset
# print(set_a.issuperset(set_b))  # Output: False
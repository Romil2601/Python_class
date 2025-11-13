# map() - A built-in function that applies a given function to all items in an iterable (like a list) and returns a map object (which is an iterator).
# filter() - A built-in function that constructs an iterator from elements of an iterable for which a function returns true.
# reduce() - The reduce() function reduces the multiple arguments into a single value. This function returns an aggregated value by applying it to an iterable.

# Syntax for map(), filter(), and reduce():

# map(function, iterable, ...)   ----MAP
# filter(function, iterable)     ----FILTER

# from functools import reduce
# reduce(function, iterable[, initializer])  ----REDUCE



# ------- Map Function Examples -------


# def square(num):
#     return num * num
# lst = [1,2,3]
# anslst = []
# for val in lst:
#     anslst.append(square(val))
# print(anslst)
# anslst = map(square, lst)
# print(list(anslst))

# lst_str = ["1", "2", "33", "67", "59"]
# lst_int = list(map(int, lst_str))
# print(lst_int)

# lst_city = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
# lst_len = list(map(len, lst_city))
# print(lst_len)

# lst_upper = list(map(str.upper, lst_city))
# print(lst_upper)

# def add(num1, num2):
#     return num1 + num2
# lst_num = [1, 2, 3, 4, 5]
# lst_num1 = [8, 9, 10]
# lst_ans = list(map(add, lst_num, lst_num1))
# print(lst_ans)

# lst = [1, 2, 3, 4]
# power = [2, 3, 4, 1]
# ans = list(map(pow, lst, power))
# print(ans)


# ------- Filter Function Examples -------

# def is_even(num):
#     return num % 2 == 0
# lst_numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = filter(is_even, lst_numbers)
# print(list(even_numbers))

# def city_len(i):
#     if len(i) > 5:
#         return i
# lst_city = ["Ahmedabad", "Assam", "Mumbai", "Goa"]
# ans = list(filter(city_len, lst_city))
# print(ans)

# def fltr(i):
#     if i % 2 == 0:
#         return i
# def square(n):
#     return n * n
# lst = [ 1, 2, 4, 6, 9]  
# ans = list(map(square,list(filter(fltr, lst))))
# print(ans)     

# Convert Those city into upper case whose len is more than 5.
# def city_len(i):
#     if len(i) > 5:
#         return i
# lst_city = ["Ahmedabad", "Assam", "Mumbai", "Goa"]
# ans = list(filter(city_len, lst_city))
# lst1 = list(map(str.upper,ans))
# print(lst1)

# Convert Celsius to Fahrenite.
# def c_to_f(i):
#     ans = (i * 9/5) + 32
#     return ans

# lst = [ 0, 32, 45]
# lst_ans = list(map(c_to_f, lst))
# print(lst_ans)


# ------- Reduce Function Examples -------


# def add(x, y):
#     return x + y
# def multiply(x, y):
#     return x * y
# from functools import reduce
# lst = [1, 2, 3, 4, 5]
# result = reduce(add, lst)
# print(f"Sum: {result}")
# result = reduce(multiply, lst)
# print(f"Multiplication: {result}")

# Average of Age from dictionary data = {name: 'John', age: 25}.
# data = [{'name': 'Romil', 'age': 24}, 
#         {'name': 'Vhishwraj', 'age': 25}, 
#         {'name': 'Abhijit', 'age': 22}]
# def add(x, y):
#     return x + y
# def get_age(person):
#     return person['age']
# ages = []
# for i in data :
#    ages.append(i['ages'])
# from functools import reduce
# ages = list(map(get_age, data))
# average_age = reduce(add, ages) / len(ages)
# print(f"Average Age: {average_age}")
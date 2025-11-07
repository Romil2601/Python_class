def concatenate(lst, separator):
    return separator.join(lst)
str_input = input("Enter the list of strings: ")
str_lst = str_input.split(",")
sep = input("Enter a separator: ")
print("Concatenated string:", concatenate(str_lst, sep))
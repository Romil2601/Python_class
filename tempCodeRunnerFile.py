def add(i):
    return i + j
lst = [1, 2, 3, 4]
j = int(input("Enter the number you want to add to all : "))
ans = list(map(add, lst))
print(ans)
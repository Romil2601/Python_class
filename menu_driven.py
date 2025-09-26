# Menu driven program with functions like convert to uppercase, lowercase, find length, replace and exit using match case.
while True: 
    print("Menu:")
    print("1. Convert to Uppercase")
    print("2. Convert to Lowercase")
    print("3. Find Length")
    print("4. Replace Substring")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))
    match choice:
        case 1:
            s = input("Enter a string: ")
            print("Uppercase:", s.upper())
        case 2:
            s = input("Enter a string: ")
            print("Lowercase:", s.lower())
        case 3:
            s = input("Enter a string: ")
            print("Length of string:", len(s))
        case 4:
            s = input("Enter a string: ")
            old_substr = input("Enter the substring to be replaced: ")
            new_substr = input("Enter the new substring: ")
            print("Modified String:", s.replace(old_substr, new_substr))
        case 5:
            print("Exiting the program.")
            break
        case _:
            print("Invalid choice. Please try again.")


# Menu driven program with functions like convert to Reverse printing, find number of digits, count total even/odd digits of a number, 
# check if number is palindrome and exit using match case.

while True: 
    print("Menu:")
    print("1. Reverse Number")
    print("2. Find Number of Digits")
    print("3. Count Even and Odd Digits")
    print("4. Check Palindrome")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))
    match choice:
        case 1:
            num = int(input("Enter a number: "))
            reversed_num = 0
            temp = num
            while temp > 0:
                digit = temp % 10
                reversed_num = reversed_num * 10 + digit
                temp //= 10
            print("Reversed Number:", reversed_num)
        case 2:
            num = int(input("Enter a number: "))
            count = 0
            temp = num
            while temp > 0:
                count += 1
                temp //= 10
            print("Number of Digits:", count)
        case 3:
            start = int(input("Enter a number: "))
            end = int(input("Enter another number: "))
            print(f"Even and Odd digit counts between {start} and {end}:")
            even_count = 0
            odd_count = 0
            for num in range(start, end + 1):
                if num % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
            print("Even Digits:", even_count)
            print("Odd Digits:", odd_count)
        case 4:
            num = int(input("Enter a number: "))
            reversed_num = 0
            temp = num
            while temp > 0:
                digit = temp % 10
                reversed_num = reversed_num * 10 + digit
                temp //= 10
            if num == reversed_num:
                print(num, "is a Palindrome")
            else:
                print(num, "is not a Palindrome")
        case 5:
            print("Exiting the program.")
            break
        case _:
            print("Invalid choice. Please try again.")
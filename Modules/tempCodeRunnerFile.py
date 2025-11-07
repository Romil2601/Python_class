import Modules.number_check as number_check
num = int(input("Enter a number: "))
if number_check.checkPrime(num):
    print(f"{num} is Prime")
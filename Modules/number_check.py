def greet (name):
    return "Good Morning",name

def bye (name):
    return "Goodbye",name

def checkEven(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
def checkPositive(num):
    if num >= 0:
        return True
    else:
        return False
    
def checkPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
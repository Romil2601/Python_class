# Number Guessing Game
import random 

num = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1
    if guess < num:
        print("Too low! Try again.")
    elif guess > num:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {num} in {attempts} attempts.")
        break
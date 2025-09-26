# Number Guessing Game
import random # Importing random module to generate random numbers

num = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
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
    
# Functions in random module:
# randint() function generates a random integer between the given range.
# random() function generates a random float between 0 and 1.
# choice() function returns a randomly selected element from a non-empty sequence.
# shuffle() function shuffles the sequence in place.
# uniform() function returns a random float number between the given range.
# sample() function returns a list of unique elements chosen from the population sequence or set.
# seed() function initializes the random number generator.
# randrange() function returns a randomly selected element from the specified range.
# getrandbits() function returns an integer with the specified number of random bits.
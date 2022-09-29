import random
from art import logo

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty, type \"easy\" or \"hard\": ")
lives = 0
num_to_guess = random.randint(0, 100)

if difficulty == "easy":
    lives = 10
else:
    lives = 5

print(f"You have {lives} attempts remaining to guess the number.")

while lives > 0:
    guess = int(input("Make a guess: "))
    if guess < num_to_guess:
        print("Too low.")
        lives -= 1
        print(f"You have {lives} remaining to guess the numeber.")
    elif guess > num_to_guess:
        print("Too high.")
        lives -= 1
        print(f"You have {lives} remaining to guess the numeber.")
    else:
        print("You guessed it!")
        break
        
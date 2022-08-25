from art import logo
from random import randint

print(logo)


def get_difficulty(difficulty):
    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5
    return attempts


def get_number():
    return randint(1, 100)


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

lives = get_difficulty(input("Choose a difficulty. Type 'easy' or 'hard': "))
number = get_number()

while lives:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print("===============    CORRECT!    ===============")
        break
    elif guess > number:
        print("===============    TOO HIGH    ===============")
        lives -= 1
    else:
        print("===============    TOO LOW    ===============")
        lives -= 1

if lives == 0:
    print("You have run out of guesses, YOU LOSE!")
    print(f"The number was {number}")
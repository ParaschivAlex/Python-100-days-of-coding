import random
import string

alphabet = string.ascii_letters
letters = []
for letter in alphabet:
    letters.append(letter)
# print(letters)

numbers = [str(i) for i in range(10)]
# print(numbers)

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']

print("Welcome to the PyPassword Generator!")
letter = int(input("How many letters would you like in your password?"))
symbol = int(input("How many symbols would you like?"))
number = int(input("How many numbers would you like?"))

password = ''
nr_letters_used = 0
nr_symbols_used = 0
nr_numbers_used = 0
total_randomizes = letter + symbol + number

for i in range(total_randomizes):
    choice = random.randint(1, 3)  # get a random choice, to put letter for 1,
    # symbol for 2 and number for 3
    if choice == 1 and nr_letters_used == letter:  # have to choose something else
        choice = random.randint(2, 3)
        if choice == 2 and nr_symbols_used == symbol:
            choice = 3
        elif choice == 3 and nr_numbers_used == number:
            choice = 2

    if choice == 3 and nr_numbers_used == number:  # have to choose something else
        choice = random.randint(1, 2)
        if choice == 2 and nr_symbols_used == symbol:
            choice = 1
        elif choice == 1 and nr_letters_used == letter:
            choice = 2

    if choice == 2 and nr_symbols_used == symbol:  # have to choose something else
        choice = random.randint(1, 2)
        if choice == 2:
            choice = 3
        if choice == 3 and nr_numbers_used == number:
            choice = 1
        elif choice == 1 and nr_letters_used == letter:
            choice = 3

    # Now regarding the choice, I add to the password and I increment the digit used
    if choice == 1:
        password += random.choice(letters)
        nr_letters_used += 1
    elif choice == 2:
        password += random.choice(symbols)
        nr_symbols_used += 1
    else:
        password += random.choice(numbers)
        nr_numbers_used += 1

print("Your MEGA SECRET password is:", password)

from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal(card_list):
    user1, user2 = random.choice(card_list), random.choice(card_list)
    computer1, computer2 = random.choice(card_list), random.choice(card_list)
    return [user1, user2], [computer1, computer2]


def calculate_win(user_total_win, computer_total_win):
    if (computer_total_win < user_total_win <= 21) or (user_total_win <= 21 < computer_total_win):
        return 1  # win
    elif user_total_win > 21 or (user_total_win < computer_total_win <= 21):
        return 2  # lose
    else:
        return 0  # draw


def calculate_score_user(user):
    user_sum = sum(user)
    return user_sum


def calculate_score_computer(computer):
    computer_sum = sum(computer)
    return computer_sum


dealt_user, dealt_computer = [], []
choice_rematch = 'y'

while choice_rematch == 'y':
    if dealt_user == [] and dealt_computer == []:
        dealt_user, dealt_computer = deal(cards)
    print(f"Your cards: {dealt_user}")
    print(f"Computer's first card: {dealt_computer[0]}")
    choice = input("Type 'y' to get another card or 'n' to pass: ")
    if choice == 'n':
        print(f"Your final hand: {dealt_user}")
        user_total = calculate_score_user(dealt_user)

        computer_total = calculate_score_computer(dealt_computer)
        while computer_total < 17:
            dealt_computer.append(random.choice(cards))
            computer_total = calculate_score_computer(dealt_computer)

        print(f"Computer's final hand: {dealt_computer}")
        win = calculate_win(user_total, computer_total)
        if win == 1:
            print("You WIN!")
        elif win == 0:
            print("Draw!")
        else:
            print("You LOST!")
        choice_rematch = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        dealt_user, dealt_computer = [], []
    else:
        dealt_user.append(random.choice(cards))
        if calculate_score_user(dealt_user) > 21:
            print("OH NO!")
            print(f"Your final hand: {dealt_user}")
            print(f"Computer's final hand: {dealt_computer}")
            print("You LOST!")
            dealt_user, dealt_computer = [], []
            choice_rematch = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

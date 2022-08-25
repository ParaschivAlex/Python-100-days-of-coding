import random
from art import logo, vs
from game_data import data
# from replit import clear

print(logo)

score, game_on = 0, True
option_a, option_b = random.choice(data), random.choice(data)

while game_on:
    while option_a == option_b:
        option_b = random.choice(data)

    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
    print(vs)
    print(f"Compare B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")

    option = input("Who has more followers? 'A' or 'B': ").upper()
    if option == 'A' and option_a['follower_count'] >= option_b['follower_count']:
        score += 1
        option_a, option_b = option_b, random.choice(data)
        print("You are right, your score is:", score)
    elif option == 'B' and option_a['follower_count'] <= option_b['follower_count']:
        score += 1
        option_a, option_b = option_b, random.choice(data)
        print("You are right, your score is:", score)
    else:
        game_on = False
        print("NO, YOU LOST with a score of", score)

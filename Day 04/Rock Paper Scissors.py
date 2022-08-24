import random

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer = random.randint(0, 2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]
while player >= 0 and player <= 2:
    print("Your choice:", options[player])
    print("Computer's choice:", options[computer])
    if player == 0 and computer == 2:
        print("You win!")
    elif player == 2 and computer == 0:
        print("You lose!")
    elif player < computer:
        print("You lose!")
    elif computer < player:
        print("You win!")
    else:
        print("Draw!")
    player = int(input("Play again by choosing a number between 0 and 2. Anything else exits the game."))

print("Thank you for playing!")
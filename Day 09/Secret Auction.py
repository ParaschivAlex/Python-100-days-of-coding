from replit import clear
# HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)
print("Welcome to the secret auction program.")

auctioners = {}
inpt = 'yes'
while inpt != 'no':
    name = input("What is your name?:")
    bid = int(input("What is your bid?: $"))
    auctioners[name] = bid
    inpt = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    clear()

print("The winner is", max(auctioners), "with a bid of $", max(auctioners.values()))

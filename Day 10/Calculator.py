from art import logo

print(logo)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

go_on = True
number1 = float(input("What's your first number?: "))
print("+\n-\n*\n/")
while go_on:
    operation = input("Pick an operation: ")
    number2 = float(input("What's the next number?: "))
    result = operations[operation](number1, number2)
    print(f"{number1} {operation} {number2} = {result}")
    stop = input("Would you like to continue the operations? Type 'yes' or 'no'.")
    if stop == 'no':
        go_on = False
    else:
        number1 = result

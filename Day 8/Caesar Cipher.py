from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    new = ''
    for letter in text:
        check = alphabet.index(letter)
        if check + shift > length:
            check = shift - (length - check) - 1
            new += alphabet[check]
        else:
            new += alphabet[check + shift]
    print(new)


def decrypt(text, shift):
    new = ''
    for letter in text:
        check = alphabet.index(letter)
        if check - shift < 0:
            check = check - shift + length
            new += alphabet[check]
        else:
            new += alphabet[check - shift]
    print(new)


should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    length = len(alphabet) - 1

    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)
    else:
        print("Not a valid option!")
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")

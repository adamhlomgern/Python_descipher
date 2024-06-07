

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
from art import end_art
print(logo)




def caesar(text, shift, direction):
    result_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = (position + shift) % 26
            elif direction == "decode":
                new_position = (position - shift) % 26
            new_letter = alphabet[new_position]
            result_text += new_letter
        else:
            result_text += letter
    print(f"The {direction}d text is {result_text}")


def main():
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)

        re_play = input("Would you like to go again? Type 'yes' to go again, 'no' to exit:\n").lower()
        if re_play != "yes":
            print(end_art)
            break


main()
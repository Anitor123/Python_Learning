alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo

print(logo)


def ceaser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position + shift_amount) % 26
            end_text += alphabets[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")


again = "yes"
while again == "yes":
    direction = input("Type 'encode' to encrypt, and type 'decode' to decrypt: \n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)
    again = input("Type 'yes' to continue and 'no' to end the program:\n")

print("Goodbye ☺☺")

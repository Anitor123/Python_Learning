import random

print("THIS PROGRAM GENERATES A PASSWORD FOR THE USER (PASSWORD CAN'T BE LESS THAN 8 CHARACTERS)")
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbolic = ['!', '@', '#', '$', '%', '&', '*', '?', '+']

length = int(input("How long do you need your password? "))
while length < 8:
    print("Password length should be at least 8 characters.")
    length = int(input("How long do you need your password? "))

number = int(input("Enter the amount of numbers you need: "))
while number >= length:
    print("The password can't only contain numbers.")
    number = int(input("Enter the amount of numbers you need: "))

symbols = int(input("Enter the amount of symbols you need: "))
while symbols + number >= length:
    print("The password can't only contain symbols and numbers.")
    symbols = int(input("Enter the amount of symbols you need: "))

password = []
for n in range(number):
    password.append(random.choice(numbers))

for s in range(symbols):
    password.append(random.choice(symbolic))

for a in range(length - (number + symbols)):
    password.append(random.choice(alphabets))

random.shuffle(password)
generated_password = ''.join(password)
# This line of code above is used to join the items in the list into a single string
print("Generated password:", generated_password)

water_level = 50
if water_level > 80:
    print("Drain the water")
else:
    print("Continue")

print("Welcome to the rollercoater")
height = int(input("What is your height in cm: "))
bill = 0
if height >= 120:
    print("You can ride the rollercater!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5")
    elif age <= 18:
        bill = 7
        print("Please pay $7")
    else:
        bill = 12
        print("Please pay $12")

    wants_photo = input("Do you want a photo? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride")


number = int(input("Enter the number that you wanna check: "))
if number % 2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")


height = float(input("Enter the height in m: "))
weight = float(input("Enter the weight in kg: "))
bmi = round(weight / height**2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have noraml weight")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese")
else:
    print(f"Your BMI is {bmi}, you are clincally obese")


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_chesse = input("Do you want extra chesse? Y or N ")
bill = 0
if size == "S":
    bill = 15
    print("Small pizza is $15")
elif size == "M":
    bill = 20
    print("Medium pizza is $20")
elif size == "L":
    bill = 25
    print("Large pizza is $25")

if add_pepperoni == "Y" and size == "L" or size == "M":
    bill += 3
elif add_pepperoni == "Y" and size == "S":
    bill += 2

if extra_chesse == "Y":
    bill += 1

print(f"Your total bill is ${bill}")


# Love Calculator
# Get drawing form ascii.co.uk/art
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

print(love_score)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")



# Treasure Island
print("Welcome To Treasure Island")
print("""
 __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
ejm97  %%%%

       {}           {}
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
ejm 96     / HHH  \
          /  \_/   \
        {}          {}
      """)
print("Your Mission is to find the treasure")
cross_road = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' ")
if cross_road.lower() == "left":
    print(r"""
        _
             .''.' \    _  __
 ___         './    '. ' `'  `
    '._______.'       \
                       '.__________
                                   '-.____________
 _________________________________________________'.__________________
                                      ____________.'
                         __________.-'
      _______          .'                      
 ___.'       '.       /               '-._         
             .'\    .' ._,.__,        ____\____.o.
             '..'._/                 '-._______.-'
                                     .-'_______'-.
                                         _/    'o'
                                      .-'

        """)
    lake = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across ")
    if lake.lower() == "wait":
        print(r"""

                                                    ____
                                         v        _(    )
        _ ^ _                          v         (___(__)
       '_\V/ `
       ' oX`
          X                            v
          X             -HELP!
          X                                                 .
          X        \O/                                      |\
          X.a##a.   M                                       |_\
       .aa########a.>>                                    __|__
    .a################aa.                                 \   /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)
        island = input("You arrive at an island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ") 
        if island.lower() == "yellow":
            print(r"""
         _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
             '-._'-.|| |' `_.-'
                    '-.||_/.-'
          
            """)
            print("Congrats, You have found the Treasure")
        elif island.lower() == "blue":
            print("You entered a room of beasts. Game Over")
        elif island.lower() == "red":
            print("You entered a room of fire. Game Over")            

    elif lake.lower() == "swim":
        print("You got eaten by sharks. Game Over") 
elif cross_road.lower() == "right":
     print("You fell into a hole. Game Over")    


# Dr. Yu 2
import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.pi)
random_float = random.random()
random_float*5
# this mutliplication helps to make sure the floating point values remain between 0 - 5(5 is exclusive)
print(random_float)


def heads_tails():
    random_int = random.randint(1,2)
    if random_int == 1:
        print("Heads")
    else:
        print("Tails")  

heads_tails()



def banker_roulette():
    name = input("Enter the boys name seperated by a comma: ")
    names = name.split(",")
    random_name = random.choice(names)
    print(f"{random_name} is going to buy the meal today.")
    # OR!!!!!!!!!
    number = random.randint(1,len(names)-1)
    namess = names[number]
    print(f"{namess} is going to pay for today's meal")


banker_roulette()


#dirty_dozen = ["strawberries","spinach","kale","Nectarines","Apples","Grapes","Preaches",
#               "Cherries","Pears","Tomatoes","Celery","Potatoes" ]

fruits = ["strawberries","Nectarines","Apples","Grapes","Peaches","Cherries","Pears"]
vegetables = ["spinach","kale","Tomatoes","Celery","Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

row1 = ["😶","😶","😶"]
row2 = ["😶","😶","😶"]
row3 = ["😶","😶","😶"]
map = [row1,row2,row3]
print(f'{row1}\n{row2}\n{row3}')
position = input("Where'd you wanna put the treasure: ")
vertical = int(position[0])
horizontal = int(position[1])

selected_row = map[vertical -1]
selected_row[horizontal -1]= "😎"
# OR!!!!!!!!!1
# map[vertical -1][horizontal -1] ="😎"

print(f'{row1}\n{row2}\n{row3}')



print("This is a rock, paper, scissor game")
print("0 is for rock, 1 is for paper, 2 is for scissor")
choices = ["rock", "paper", "scissor"]
choice = int(input("Enter the number: "))
human_choice = choices[choice]
comp_choice = choices[(random.randint(1,3)) - 1]
if human_choice == comp_choice:
    print("It's a draw")
elif human_choice == "rock":
    if comp_choice == "papper":
        print("Computer Wins")
    else:
        print("You Win")
elif human_choice == "paper":
    if comp_choice == "scissor":
        print("Compter Wins")    
    else:
        print("You Win")
elif human_choice == "scissor":
    if comp_choice == "rock":
        print("Compter Wins")
    else:
        print("You Win")                        


print(f"Your choice is {human_choice}")
print(f"Computer choice is {comp_choice}")
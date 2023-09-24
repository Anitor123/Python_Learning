import random

move_list = ["rock","paper","scissors"]


continue_game = True
while continue_game:
    user_input = input("Enter rock, paper or scissors: " ).lower()
    comp_input = random.choice(move_list)
    if user_input == "rock":
        if comp_input == "scissors":
            print("You win")
        elif comp_input == "paper":
            print("You lose")
            continue_game = False    
        elif comp_input == "rock":
            print("It's a tie")
    elif user_input == "paper":
        if comp_input == "scissors":
            print("You lose")
            continue_game = False
        elif comp_input == "paper":
            print("It's a draw")    
        elif comp_input == "rock":
            print("You win")     
    elif user_input == "scissors":
        if comp_input == "scissors":
            print("It's a draw")
        elif comp_input == "paper":
            print("You win")    
        elif comp_input == "rock":
            print("You lose")   
            continue_game = False           

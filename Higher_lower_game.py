from Game_data import data
import random
from Arty import logo, vs

def format_account(account):
    """Format the account into printable format"""
    account_name = account["name"]
    account_descr = account["description"]  
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"

print(f"{logo} \n")
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_account(account_a)}")
    print(f"{vs} \n")
    print(f"Against B: {format_account(account_b)}")

    guess = input("Who has more followers 'A' or 'B': ").upper()

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"CORRECT!!, Current Score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, You're wrong, Final Score: {score}")    
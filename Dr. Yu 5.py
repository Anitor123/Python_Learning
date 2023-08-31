import random
from hangman_word import hangman_words 
from hangman_art import Logo


print(Logo)
chosen_word = random.choice(hangman_words)
print(chosen_word)

blank_list =[]
for alpha in chosen_word:
    blank_list += "_"
print(f"{' '.join(blank_list)}")

lives = 0
end_of_game = False
while not end_of_game:
    guess = input("Enter a chosen letter: ").lower()
    for n in range(len(chosen_word)):
        letter = chosen_word[n]
        #print(f"Current position: {n}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            blank_list[n] = letter

    if guess not in chosen_word:
        lives +=1
        from hangman_art import stages
        print(stages[lives])    
        if lives == 6:
            end_of_game = True
            print("You lose")

    print(f"{' '.join(blank_list)}")
    if "_" not in blank_list:
        end_of_game = True
        print("You win")


 
            
#OR!!!!!!!!
# for letter in chosen_word:
#      if letter == guess:
#        print("Right")
#      else:
#        print("Wrong")   


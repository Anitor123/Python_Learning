i = 1
while i <= 5:
    print("x" *i)
    i += 1
print("Done")

# GUESS GAME
number = 5
guess_count= 1
guess_limit = 3
while guess_count <= guess_limit:
    guess = int(input("Type in a single digit number: " ))
    guess_count+= 1
    if guess == number:
        print("Yayyyyyyyyy! you are gay ")
        break 
else:
    print("Atleast your not gay LOL!!!!!")


# CAR GAME
command=""
started = False
while True:
    command= input(">").lower()
    if command == "start":
        if started:
            print("The car has already started")
        else:
            started = True
            print("Car started.....") 
    elif command == "stop":
        if not started:
             print("The car has already stopped")
        else:
            started = False
            print("Car stopped")     
    elif command == "quit":
        break    
    elif command == "help":
        print("""
Start - To start the car
Stop - To stop the car
quit - To quit                           
            
 """)    
    else:
        print("Don't understand you")

        
for item in "Python":
    print(item)
    
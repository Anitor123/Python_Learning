# Kilometer Converter
def main():
    kilo = float(input("Enter the amount of kilometer(s): "))
    miles = mile_conv(kilo)
    print(f"{kilo} = {miles} miles")


def mile_conv(kilos):
    result = kilos * 0.6214
    return result
main()



# String Repeater
def maine():
    word = input("Enter the word and see the magic: ")
    number = int(input("Enter the multiplies: "))
    magic = string_mult(word, number)
    print(f"You entered {word} and it is now {magic} ")

def string_mult(alpha, numeric):
    result = alpha * numeric
    return result
maine()          



# How much Insurance
mini_percent = 0.8
def insurance():
    rep_cost = int(input("Enter the replacement cost of a builing: $"))
    mini_cost = calc_mini(rep_cost)
    print(f"This is the minimum amount of insurance to buy proprty: ${mini_cost}")

def calc_mini(cost_rep):
    result = cost_rep * mini_percent
    return result
insurance()



# Automobile Costs
def auto():
    lp = int(input("Enter the amount spent on loan payment: $"))
    ins = int(input("Enter the amount spent on insurance: $"))
    gas = int(input("Enter the amount spent on gas: $"))
    oil = int(input("Enter the amount spent on oil: $"))
    tires = int(input("Enter the amount spent on tires: $"))
    main = int(input("Enter the amount spent on maintenance: $"))
    total = lp+ins+gas+oil+tires+main
    annual_cost = total*12
    print(f"This is the monthly cost: ${total}")
    print(f"This is the annual cost: ${annual_cost}")
auto()    



# Property Tax
Ass_percent = 0.6
def prop_tax():
    value_prop = float(input("Enter the actual value of the property: $"))
    ass_value = value_prop * Ass_percent
    total = ass_value / 100
    property_tax = total * 0.72
    print(f"This is the assessment value of the property: ${ass_value}")
    print(f"This is the property tax: ${property_tax}")
prop_tax()



# Calories for Fat and Carbohydrates
def calories():
    fat = int(input("Enter the number of fat grams consumed per day: "))
    carbs = int(input("Enter the amount of carbs consumed per day: "))
    result1 = cal_from_fat(fat)
    result2 = cal_from_carbs(carbs)
    print(f"This is the amount of calories gotten from fats: {result1}g")
    print(f"This is the amount of calories gotten from carbs: {result2}g")

def cal_from_fat(fats):
    fatcal = fats * 9
    return fatcal

def cal_from_carbs(carbss):
    carbcal = carbss * 4
    return carbcal    

calories()



# Paint Job Estimator
def paint_job_estimator():
    # Get user input
    square_feet = float(input("Enter the square feet of wall space to be painted: "))
    paint_price = float(input("Enter the price of the paint per gallon: "))
    
    # Calculate the number of gallons of paint required
    gallons_required = square_feet / 112
    
    # Calculate the hours of labor required
    labor_hours = gallons_required * 8
    
    # Calculate the cost of the paint
    paint_cost = gallons_required * paint_price
    
    # Calculate the labor charges
    labor_charges = labor_hours * 35.00
    
    # Calculate the total cost of the paint job
    total_cost = paint_cost + labor_charges
    
    # Display the results
    print("Number of gallons of paint required:", gallons_required)
    print("Hours of labor required:", labor_hours)
    print("Cost of the paint: $",paint_cost)
    print("Labor charges: $",labor_charges)
    print("Total cost of the paint job: $",total_cost)

# Call the function to run the program
paint_job_estimator()



# Monthly Sales Tax
def monthly_sales_tax():
    total_sale = float(input("Enter the total sales for the month: $"))
    state_sale = 0.05 * total_sale
    county_sale = 0.025 * total_sale
    total = county_sale + state_sale
    print(f"The amount of county sales tax: ${county_sale}")
    print(f"The amount of state sales tax: ${state_sale}")
    print(f"The total sales tax: ${total}")

monthly_sales_tax()    



# Feet to Inches
def feet_to_inches(feet):
    return feet * 12

# Prompt the user for input
feet = float(input("Enter the number of feet: "))

# Convert feet to inches using the function
inches = feet_to_inches(feet)

# Display the result
print("The number of inches in", feet, "feet is", inches, "inches.")



# Addition Test
import random

def generate_addition_test():
    for question_number in range(1, 6):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        print("Question", question_number)
        print(num1, "+", num2, "= _____")
        print()

# Generate the addition test
generate_addition_test()



# Maximum of Two Values
def max():
    int1 = int(input("Enter first integer: "))
    int2 = int(input("Enter second integer: "))
    com_ints(int1, int2)

def com_ints(num1, num2):
    if num1 > num2:
        print(num1)
    elif num2 > num1:
        print(num2)
    else:
        print("They are thesame")
    return num1, num2
    
max()    



# Falling Distance
def falling_distance(time):
    g = 9.8  # acceleration due to gravity in m/s^2
    distance = 0.5 * g * (time ** 2)
    return distance

# Call the function in a loop for values 1 through 10
for time in range(1, 11):
    distance = falling_distance(time)
    print("Time:", time, "seconds | Distance:", distance, "meters")


# Mosh Tutorials
def square(number):
    return number * number

print(square(4))



# Kinetic Energy
def kinetic_energy(m, v):
    energy = 0.5 * m * v**2
    return energy

# Prompt the user for mass and velocity
mass = float(input("Enter the mass: "))
velocity = float(input("Enter the velocity: "))

# Calculate and display the kinetic energy
result = kinetic_energy(mass, velocity)
print("The kinetic energy is:", result)



# Test Average and Grade
def calc_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return average

def determine_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Prompt the user for five test scores
scores = []
for i in range(5):
    score = float(input("Enter the test score: "))
    scores.append(score)

# Calculate the average test score
average = calc_average(scores)

# Display the letter grade for each score
for i, score in enumerate(scores):
    grade = determine_grade(score)
    print("Test", i+1, "Score:", score, "| Grade:", grade)

# Display the average test score
print("Average Test Score:", average)



# Odd/Even Number
def odd():
    for count in range(101):
        number = random.randint(0, count)
        if number % 2== 0:
            print("It is even")
        else:
            print("It is odd")


odd()



# Tutorials
def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))



def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))




def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))

 


def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5)



def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')



def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 



def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(9))



def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))



def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(6))



def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(isPalindrome('aza')) 



def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")



def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")



def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")



def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


def myfunction():
  pass



def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    # It does the top block of code until it reaches 0 then, the addition starts from there
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)



# outer function
def outer_fun(a, b):
    square = a ** 2

    # inner function
    def addition(a, b):
        return a + b

    # call inner function from outer function
    add = addition(a, b)
    # add 5 to the result
    return add + 5

result = outer_fun(5, 10)
print(result)



def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)


import random

print("Generating 3 random integer number between 100 and 999 divisible by 5")
for num in range(3):
    print(random.randrange(100, 999, 5), end=', ')



import random

lottery_tickets_list = []
print("creating 100 random lottery tickets")
# to get 100 ticket
for i in range(100):
    # ticket number must be 10 digit (1000000000, 9999999999)
    lottery_tickets_list.append(random.randrange(1000000000, 9999999999))
# pick 2 luck tickets
winners = random.sample(lottery_tickets_list, 2)
# random.sample is used to ensure that the two winners are unique
print("Lucky 2 lottery tickets are", winners)



import random

name = 'pynative'
char = random.choice(name)
# random.choice randomly selects an element from a sequence, in this case a string
print("random char is ", char)



import random

num1  = random.random()
print("First Random float is ", num1)
num2 = random.uniform(9.5, 99.5)
print("Second Random float is ", num1)

num3 = num1 * num2
print("Multiplication is ", num3)



import random

def play_guessing_game():
    random_number = random.randint(1, 100)
    num_guesses = 0

    while True:
        user_guess = int(input("Guess the number (between 1 and 100): "))
        num_guesses += 1

        if user_guess > random_number:
            print("Too high, try again.")
        elif user_guess < random_number:
            print("Too low, try again.")
        else:
            print("Congratulations! You guessed the number.")
            print("Number of guesses:", num_guesses)
            break

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_guessing_game()
    else:
        print("Thank you for playing!")

# Start the game
print("Welcome to the Random Number Guessing Game!")
play_guessing_game()



# Rock, Paper, Scissor
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"

    if user_choice == "rock":
        if computer_choice == "scissors":
            return "User"
        else:
            return "Computer"
    elif user_choice == "scissors":
        if computer_choice == "paper":
            return "User"
        else:
            return "Computer"
    elif user_choice == "paper":
        if computer_choice == "rock":
            return "User"
        else:
            return "Computer"

def play_rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    while user_choice not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    print("Computer's choice:", computer_choice)

    winner = determine_winner(user_choice, computer_choice)

    if winner == "Tie":
        print("It's a tie! Let's play again.")
        play_rock_paper_scissors()
    else:
        print(winner, "wins!")

# Start the game
print("Welcome to Rock, Paper, Scissors Game!")
play_rock_paper_scissors()




import random

def shuffle_list(lst):
    random.shuffle(lst)
    # random.shuffle modifies the list, shuffles the list in place
    return lst

# Test the program
my_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(my_list)
print("Original List:", my_list)
print("Shuffled List:", shuffled_list)




import random

def simulate_dice():
    dice1 = [1,2,3,4,5,6]
    dice2 = [1,2,3,4,5,6]
    guess1= random.choice(dice1)
    guess2 = random.choice(dice2)
    sum = guess1 + guess2
    print(sum)

simulate_dice()    
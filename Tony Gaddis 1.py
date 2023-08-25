# Number Analyser
Number = int(input("Type in the number : "))
if Number > 0:
    print("Positive")
elif Number < 0:
    print("Negative")
else:
    print("Zero")
if Number % 2 == 0:
    print("Even")
elif Number % 2 != 0:
    print("Odd")
else:
    print("Zero")    


# Area of Rectangle
print("Enter values for Rectangle 1")
len1 = int(input("Enter the length for Rectangle 1: " ))
wid1 = int(input("Enter the width for Rectangle 1: " ))
print("Enter the value for Rectangle 2")
len2 = int(input("Enter the length for Recatangle 2: " ))
wid2 = int(input("Enter the width for Rectangle 2: " ))
Area1 = len1 * wid1
Area2 = len2 * wid2
if Area1 > Area2:
    print(format(f"Area of Rectangle 1, {Area1} is greater"))
elif Area2 > Area1:
    print(format(f"Area of Rectangle 2, {Area2} is greater")) 
else:
    print("Both area's are equal")


# Quarter of the year
print("We use number's 1-12 to signify the months of the year")
month = int(input("Enter the month number: " ))
if month == 1:
    print("January ")
elif month == 2:
    print("February ")
elif month == 3:
    print("March")        
elif month == 4:
    print("April")
elif month == 5:
    print("May ")
elif month == 6:
    print("June ")           
elif month == 7:
    print("July ")
elif month == 8:
    print("August ")
elif month == 9:
    print("September ")
elif month == 10:
    print("October ")
elif month == 11:
    print("November ")
elif month == 12:
    print("December ")   
else:
    print("Invalid month input")  
if month == 1 or month == 2 or month == 3:
    print("First quarter of the year")    
elif month == 4 or month ==5 or month == 6:
    print("Second quarter of the year")
elif month == 7 or month == 8 or month == 9:
    print("Third quarter of the year")
elif month == 10 or month == 11 or month == 12:
    print("Fourth quarter of the year") 
else:
    print("ERORR!!!!!!!!!!!!!!!!!!! ")     


# Roman Numerals
print("This program displays the Roman Numeral version of a number between 1-10")
num = int(input("Enter a number between 1-10: " ))
if num ==1:
    print("I")
elif num ==2:
    print("II")    
elif num ==3:
    print("III") 
elif num ==4:
    print("IV") 
elif num ==5:
    print("V") 
elif num ==6:
    print("VI") 
elif num ==7:
    print("VII") 
elif num ==8:
    print("VIII") 
elif num ==9:
    print("IX") 
elif num ==10:
    print("X") 
else: 
    ("Invalid number input")  


# Mass and Weight
print("This program helps to get the weight in Newtons")
gravity_const = 9.8
mass = int(input("Enter the mass of the object in kilograms: " ))
weight = mass * gravity_const
print(f"The weight of the object is {weight}", )
if weight > 500:
    print("It's too heavy")
elif weight < 100:
    print("It's too light") 


# Magic Date
print("THIS PROGRAM HELPS US ENJOY AND DETERMNE A MAGIC DATE") 
print("A MAGIC DATE IS A SITUATION WHEN THE DAY * MONTH(IN NUMERIC FORM) IS EQUAL TO THE TWO-DIGIT YEAR")
num_month = int(input("Enter the number of month: " ))
num_day = int(input("Enter the number of day: " ))
num_year = int(input("Enter the two-digit year: " ))
magic_date = num_month * num_day
if magic_date == num_year:
    print("Wowww, It's a magic date") 
else:
    print("It's not a magic date")


# Grade Calculator
print("THIS PROGRAM HELPS USER CALCULATE THEIR GRADES")
test1 = int(input("Enter the score for test 1: " ))
test2 = int(input("Enter the score for test 2: " ))
exams = int(input("Enter the score for exams: " ))
total = test1 + test2 + exams
if exams >= 25 and total >= 50:
    if total >= 80:
        print("Distinction!!")
    elif total >=60 and total < 80:
        print("Credit")
    elif total < 60:
        print("Pass")
else:
    print("Fail")       
              

# Hot Dog Calculator
import math
print("THIS PROGRAM PRINTS THE NUMBER OF HOT DOGS NEEDED FOR A PARTY")
hot_dog_package = 10
hot_buns_package = 8
people = int(input("Enter the number of people attending the party: " ))
dogs_per_people = int(input("Enter the number of hot dogs per person: " ))
total_hot_dogs = people * dogs_per_people
total_hot_doggies = math.ceil(total_hot_dogs/hot_dog_package)
total_hot_buns = math.ceil(total_hot_dogs/ hot_buns_package)
total_hot_doggies_leftover = (hot_dog_package*total_hot_doggies) - total_hot_dogs
total_hot_buns_leftover = (hot_buns_package*total_hot_buns) - total_hot_dogs
print(f"The minimum amount of hot dog packages is {total_hot_doggies}")
print(f"The minimum amount of hot buns packages is {total_hot_buns}")
print(f"The number of hot dog letover is {total_hot_doggies_leftover}")
print(f"The number of hot buns leftover is {total_hot_buns_leftover}")


# Roulette Wheel colors
print("ON A ROULETTE WHEEL, THE POCKETS ARE NUMBERERD 0-36")
wheel_no = int(input("Enter the desired Roulette Wheel Number: " ))
if wheel_no >= 1 and wheel_no < 11:
    if wheel_no % 2 == 0:
        print("The number falls in between 1 and 10 and it is also an even number")
        print("So the colour is 'RED' ")
    else:
        print("The number falls in between 1 and 10 and it is also an odd number")
        print("So the colour is 'BLACK' ")
elif wheel_no >= 11 and wheel_no < 19:
    if wheel_no % 2 == 0:
        print("The number falls in between 11 and 18 and it is also an even number")
        print("So the colour is 'BLACK' ")
    else:
        print("The number falls in between 11 and 18 and it is also an odd number")
        print("So the colour is 'RED' ")
elif wheel_no >= 19 and wheel_no < 29: 
    if wheel_no % 2 == 0:
        print("The number falls in between 19 and 28 and it is also an even number")
        print("So the colour is 'RED' ")
    else:
        print("The number falls in between 19 and 28 and it is also an odd number")
        print("So the colour is 'BLACK' ")       
elif wheel_no >= 29 and wheel_no < 37:
    if wheel_no % 2 == 0:
        print("The number falls in between 29 and 36 and it is also an even number")
        print("So the colour is 'BLACK' ")
    else:
        print("The number falls in between 29 and 36 and it is also an odd number")
        print("So the colour is 'RED' ")
else:
    print("ERORR, check your input") 


# Money Counting Game
print("THIS PROGRAM IS A GAME THAT ALLOWS USER TO INPUT THE NUMBER OF COINS IT TAKES TO GET A DOLLAR")
PENNY_TO_DOLLAR = 100
NICKEL_TO_DOLLAR = 20
DIME_TO_DOLLAR = 10
QUARTER_TO_DOLLAR = 4
penny_ques = int(input("Enter the number of pennies make a dollar: " ))
if penny_ques == PENNY_TO_DOLLAR:
    print("Congratulations you got the questions")
else:
    print(f"Wrong, it takes {PENNY_TO_DOLLAR}")    
nickel_ques = int(input("Enter the number of nickel is takes to get a dollar: " ))
if nickel_ques == NICKEL_TO_DOLLAR:
    print("Congratulations you got the questions")
else:
    print(f"Wrong, it takes {NICKEL_TO_DOLLAR}")    
dime_ques = int(input("Enter the number of dime it takes to get a dollar: " ))
if dime_ques == DIME_TO_DOLLAR:
    print("Congratulations you got the questions")
else:
    print(f"Wrong, it takes {DIME_TO_DOLLAR}")    
quarter_ques = int(input("Enter the number of quarters is takes to get a dollar: " ))
if quarter_ques == QUARTER_TO_DOLLAR:
    print("Congratulations you got the questions")
else:
    print(f"Wrong, it takes {QUARTER_TO_DOLLAR}")   


# Book Club Points
print("THIS PROGRAM CALCULATES THE AMOUNT OF POINTS GOTTEN FROM A BOOK CLUB")
books = int(input("Enter the amount of books purchased: " ))
if books == 0:
    print("Number of points is 0")
elif books == 2:
    print("Number of points is 5")
elif books == 4:
    print("Number of points is 15")
elif books == 6:
    print("Number of points is 30")
elif books >= 8:
    print("Number of points is 60")


# Software Sales
print("THIS PROGRAMS CALCULATES THE DISOUNT PRICES OF SOFTWARES")
RETAIL = 99
print(f"Retail price of Software is ${RETAIL}")
quantity = int(input("Enter the amount of software packages to be purchased: " ))
if quantity >= 10 and quantity < 20 :
    discount = 0.1
    print("Your discount will be 10 percent off")
elif quantity >= 20 and quantity < 50:
    discount = 0.2
    print("Your discount will be 20 percent off ")
elif quantity >= 50 and quantity < 100:
    discount = 0.3
    print("Your discount will be 30 percent off ")
elif quantity >= 100:
    discount = 0.4
    print("Your discount will be 40 percent off ")
else:
    print("There's no discount for that quantity")
    discount = 0
discount_amt = RETAIL * discount
total_amt = RETAIL - discount_amt    
print(f"The price after discount will be ${total_amt}")    


# Shipping Charges
print("THIS PROGRAMS DISPLAYS THE CHARGES FOR CERTAIN AMOUNT OF WEIGHTS ")
goods_weight= float(input("Enter the weight of goods(In pounds): " ))
if goods_weight <= 2:
    rate = 1.50
    print("The charge is $1.50")
elif goods_weight > 2 and goods_weight <= 6:
    rate = 3.00
    print("The charge rate is $3.00") 
elif goods_weight > 6 and goods_weight <= 10:
    rate = 4.00
    print("The charge rate is $4.00") 
elif goods_weight > 10:
    rate = 4.75
    print("The charge rate is $4.75")  


# Body Mass Index
print("THIS PROGRAM HELPS DETERMINE WHETHER THE USER IS UNDERWEIGHT OR OVERWEIGHT")
bmi_weight = float(input("Enter the weight in pounds: " ))
bmi_height = float(input("Enter the height in inches " ))
BMI= bmi_weight * 703/(bmi_height ** 2)
print(f"Your BMI is {BMI}")
if BMI < 18.5:
    print("You are Underweight")
elif BMI > 25:
    print("You are Overweight")
else:
    print("You seem very well")


# Time Calculator
print("THIS IS A TIME CALCULATOR THAT CONVERTS SECONDS TO MINUTES, HOUR OR DAYS")
seconds = int(input("Enter the number of seconds: " ))
if seconds >= 60 and seconds < 3600:
    Minutes = seconds//60
    Seconds = seconds%60
    print(f"{Minutes}min:{Seconds}sec")
elif seconds >= 3600 and seconds < 86400:
    Hour = seconds//3600
    Minutes = (seconds//60)%60
    Seconds = seconds%60
    print(f"{Hour}hr:{Minutes}min:{Seconds}sec")   
elif seconds >= 86400:
    Days = seconds//86400
    Hour = (seconds//3600)%24
    Minutes = (seconds//60)%60
    Seconds = seconds%60
    print(f"Day{Days}, {Hour}hr:{Minutes}min:{Seconds}sec")



# February Days
print("THIS PROGRAM HELPS DETERMINE THE NUMBER OF FEBRUARY DAYS IN THE YEAR")
feb_year = int(input("Enter the year: " ))
if feb_year % 100 ==0:
    if feb_year % 400 ==0:
        print("There are 29 days in February this year")
    else:
        print("There are 28 days in February this year")    
elif feb_year % 100 !=0:
    if feb_year % 4 == 0:
        print("There are 29 days in February this year ")  
    else:
        print("There are 28 days in February this year")
else:
    print("ERORR!, check the input")                  


# Wi-Fi Diagnostic Tree
print("THIS IS A Wi-Fi DIAGNOSIS PROGRAM")
print("Reboot the computer and try to connect")
wifi_dia = input("Did that fix the problem? Answer with yes or no: " )
if wifi_dia == "yes":
    print("")
if wifi_dia == "no":
    print("Reboot the router and try to connect")
    wifi_dia = input("Did that fix the problem? Answer with yes or no: " )
    if wifi_dia == "no":
        print("Make sure the cables between the router and modem are plugged in firmly")    
        wifi_dia = input("Did that fix the problem? Answer with yes or no: " ) 
        if wifi_dia == "no":
            print("Move the router to a new loaction and try to connect")
            wifi_dia = input("Did that fix the problem? Answer with yes or no: " )  
            if wifi_dia == "no":
                print("Get a new router")
            


# Restaurant Selector
print("THIS PROGRAM HELPS SELECT THE PREFECT RESTAURANT FOR A GROUP OF FRIENDS")
veg = input("Is anyone in party a vegetarian? Answer with yes or no: " ) 
vegan = input("Is anyone in your party vegan? Answer with yes or no: " ) 
glut = input("Is anyone in your party gluten-free? Answer with yes or no: " )
if veg == "yes" and vegan == "yes" and glut == "yes":
    print("Here are your restaurant choice(s):")
    print("The Chef's Kitchen \n Corner Cafe")  
elif veg == "yes" and vegan == "no" and glut == "no":
    print("Here are your restaurant choice(s):")
    print("Mama's Fire Italian")
elif veg == "yes" and vegan == "no" and glut =="yes":
    print("Here are your restaurant choice(s):")
    print("Main Street Pizza Comapny") 
elif veg == "no" and vegan == "no" and glut == "no":
    print("Here are your restaurant choice(s)):")
    print("Joe's Gourment Burgers")
else:
    ("We don't have such restaurant or invalid answer inputs")
           
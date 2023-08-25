# Bug Collector
print("THIS PROGRAM DISPLAYS THE TOTAL OF BUGS COLLECTED WITHIN FIVE DAYS")
bug = 1
total_bug = 0
while bug < 6:
    bugs = int(input(f"Day {bug},Enter the number of bugs collected today: " ))
    bug += 1
    total_bug += bugs
print(f"This is the total bug for the five days {total_bug}")


# Calories Bruned
print("THIS PROGRAM DISPLAYS THE CALORIES BURNED AFTER SOME MINUTES")
burning = 10
while burning <= 30:
    burnt = burning * 4.2
    print(f"{burning}mins, This is the amount of calories burnt after this minute, {burnt}")
    burning += 5


# Lap Times
print("THIS PROGRAM HELPS DISPLAY THE MIN, MAX, AND AVERAGE OF LAP TIMES INPUTED")
lap = int(input("Enter the number of laps ran around the racetrack: " ))
lapping = []
total = 0
for laps in range(lap):
    lappie= float(input(f"Lap {laps+1},Enter the lap time for the lap: " ))
    lapping.append(float(lappie))
# for max
max = lapping[0] 
for lappings in lapping:
    if lappings > max:
        max = lappings
# for min
min = lapping[0]
for lappingss in lapping:
    if lappingss < min:
        min = lappingss
# for average
for lappingsss in lapping:
    total += lappingsss
    average = total / lap
# print values
print(f"The fastest lap time is {min}") 
print(f"The slowest lap time is  {max}")
print(f"The average lap time is {average}")        


# Distance Travelled
print("THIS PROGRAM HELPS DISPLAY THE DISTANCE TRAVELLED IN EACH HOUR")
speed = float(input("Enter the speed of the car(in miles per hour): " ))
hour = int(input("Enter the number of hours: " ))
print("HOUR \t DISTANCE TRAVELLED")
print("__________________________")
for hours in range(hour):
    distance = speed * (hours +1)
    print(f"{hours+1} \t {distance}")


# Average Rainfall
print("THIS PROGRAM DISPLAYS THE NO. OF MONTHS AND THE AVERAGE RAINFALL")
inches_list = []
year = int(input("Enter the number of years: " ))
for years in range(year):
    print(f"YEAR {years +1}")
    for month in range(12):
        inches = float(input(f"Month {month+1}, Enter the amount of rainfall in inches: "))
        inches_list.append(float(inches))
# for total month
total_month = year *12        
# for average
total =0
for inchess in inches_list:
    total += inchess
    av_rain = total/total_month
# Display values
print(f"This is the total number of months, {total_month}")           
print(f"This is the total amount of rainfall {total}")
print(f"This is the average rainfall per month {av_rain}")  



# Miles To Kilometer Table
print("THIS PROGRAM DISPLAYS THE MILES AND KILOMETERS")
miles = 10.0
print("MILES \t KILOMETERS")
print("__________________")
while miles <= 80:
    conv_kilo = miles * 1.60934
    print(f"{miles} \t {conv_kilo}")
    miles += 10    


# Pennies for Pay
total = 0
pennies = 1
print("THIS PROGRAM DISPLAYS THE SALARY IN DOLLARS FOR A PERIOD OF DAYS")
day = int(input("Enter the number of days worked: " ))
print("DAYS \t SALARY")
print("______________")
for days in range(day):
    pennies *= 2
    total += pennies
    dollar = pennies /100
    print(f"DAY {days + 1} \t ${dollar}")
dollar_total = total / 100
print(f"Total amount will be ${dollar_total}")    


# Average Word Length
print("THIS PROGRAM DISPLAYS THE TOTAL WORD LENGTH OF THE WORDS INPUTED")
total = 0
length = 0
word_list = ""
print("Enter the word or;")
print("Enter the <enter> button to end ")
word = input("Word: " )
while word != "":
    word_list = word
    length += len(word_list)
    print("Enter the word")
    print("Enter the <enter> button to end ")
    word = input("Word: " )
total += length
print(f"This is the total word length: {total}")


# Ocean Levels
print("DISPLAYS THE OCEAN RISING LEVEL")
print("YEAR \t OCEAN RISE")
rise_rate = 1.6
for rise in range(25):
    ocean_rise = (rise+1)* rise_rate
    print(f"YEAR {rise + 1} \t {ocean_rise}")


# Tuition Increase
import math
print("THIS PROGRAM DISPLAYS THE INCREASE IN TUITION FEES OVER FIVE YEARS")
print("YEAR \t TUITION INCREASE")
print("____________________________")
year = 1
rate = 0.03
total = 0
tuition = 8000
while year <= 5:
    per_increase = rate * tuition
    tuition = tuition + per_increase
    print(f"{year} \t ${tuition}")
    year += 1


# Sleep Debt
print("THIS PROGRAM CHECKS WHETHER AN INDIVIDUAL HAS SLEEP DEBT")
desire_sleep_amt = 8
total = 0
week =7
for day in range(week):
    sleep_hrs = int(input(f"DAY {day+1} Enter the amount of hour: "))
    total += sleep_hrs
normal_amount = week * desire_sleep_amt
determine = total - normal_amount
if determine < 0:
    print("Your not getting enough sleep")
else:
    print("Mehnnnnn I wish I were you")   


# Calculating The Factorial of a Number
print("THIS PROGRAM DISPLAYS THE FACTORIAL OF A NUMBER")
total = 1
number = int(input("Enter the number: "))
for numbers in range(1,number+1):
    if number == 0:
        total = 1
        print(f"Factorial of {number} is {total}")
    else:
        total = total * numbers
        print(f"Factorial of {number} is {total}")


# Population
print("THIS PROGRAM DISPLAYS THE POPULATION INCREASE OVER CERATIN DAYS")
org_no = int(input("Enter the starting number of organisms: "))
pop_rate = int(input("Enter the average daily population increase(as percentage): "))
no_days = int(input("Enter the number of days organisms will multiply: "))
print("Day Approximate \t Population")
print(f"1 \t\t\t {org_no}")
integer = 0
for integer in range(no_days):
    pop_dec = pop_rate / 100
    pop_increase = org_no * pop_dec
    org_no = org_no + pop_increase
    print(f"{integer + 2} \t\t\t {org_no}")
    
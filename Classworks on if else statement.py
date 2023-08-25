# Divisibility by 7
number = int(input("Type in the number: " ))
if number % 7 == 0:
    print("The number is divisible by 7")
else:
    print("The number is not divisible by 7")


#Odd and Even Numbers
number = int(input("Type in the digit: " ))
if number %2 == 0:
    print("The number is even")
else:
    print("The number is odd")    

# Shows the last digit of a nummber
# number % will return last digit
number= int(input("Type in any number: " ))
last_digit = number % 10
print(last_digit)    


# School Grading System
grade=int(input("Type in the score: " ))
if grade > 90 and grade <=100 :
    print("A")
elif grade > 80 and grade <= 90:
    print("B")
elif grade >= 60 and grade <= 80:
    print("C")
elif grade >= 0 and grade <= 60:
    print("D")           
else:
    print("Invalid  input")


# Tax rate
income=int(input("Type in the income: " ))
if income > 100000:
    print("Your tax rate is 15%")
    Tax_one = 0.15*income
    print(f"Tax to be paid is ${Tax_one}")
elif income > 50000 and income <= 100000:
    print("Your tax rate is 10%")
    Tax_two = 0.1 * income
    print(f"Tax to be paid is ${Tax_two}")    
elif income <= 50000:
    print("Your tax rate is 5%") 
    Tax_three = 0.05*income
    print(f"Tax to be paid is ${Tax_three}")

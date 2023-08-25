# Multiplication table of 5
i = 0
while i <= 12:
    print(5 * i)
    i += 1


#Factorial of numbers
number=int(input("Enter number: " ))
factorial = 1
if number== 0:
    print(1)
else:
    while number>=1:
        factorial =factorial*number
        number= number - 1
        print(factorial)


#Factorial of numbers (Another approach)
number =int(input("Enter the number"))
fact=1
i =1
while i<=number:
    fact = fact*i
    i = i+1 
print(f"The factorial of {number} is {fact}")    



#H.C.F
num1=int(input("Enter fisrt number: " ))
num2=int(input("Enter second number: " ))
# x,y = 10,20 means x=10 and y=20
while  num2 != 0:
    num1,num2 = num2, num1%num2
    print(F"This is your HCF: {num1}")

# Another approach to HCF
num1=int(input("Enter fisrt number: " ))
num2=int(input("Enter second number: " ))
smaller =0
hcf=0
if num1 < num2:
    smaller = num1
else:
    smaller = num2 
while smaller >= 1:
    if num1 % smaller ==0 and num2 % smaller==0:
        hcf = smaller
        break
    smaller = smaller-1
print(F"HCF of {num1} and {num2} = {hcf}")

# Button q to quit
#stop_going = "q"
#while stop_going == "q":
#    int(input("Enter another digit"))       

#Show Numbers and Squares
i = 0
print("Numbers \t\t squares ")
while i <= 10:
    print(i, "\t\t\t", i**2)
    i= i+1


# Showing a series of number incrementing by 10
i = 10
while i<= 300:
    print(i, end = ",")
    i = i+10

# Prints the sum of the first 10 Numbers
i = 10
j = 0
while i >= 1:
    j =j + i
    i = i -1
    print(j)

# Even numbers in between numbers
starting_no = int(input("Enter the starting value: " ))
Limit = int(input("Enter the last number: " ))
if starting_no < Limit:
    while starting_no < Limit:
        if starting_no % 2== 0:
            print(starting_no, end=",")
        starting_no+=1    
else:
    print("Your starting number is bigger than the last number, Fat Dummy")            

# Prime Numbers
num = int(input("Type in the number: " ))
is_prime = True #To set the boolean variable for prime number
i = 2 # because 0 and 1 are not prime numbers
while i <= num/2: # To check for prime numbers, if the value of cannot be divided even up half of the num, it is a prime number
    if num%i == 0:
        is_prime =False
        break
    i = i+1
if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")    


# Program that finds the sum of user inputs
number =int(input("Enter your digits"))
i=0 # holds the value of the last digits of the user input
j=0 # holds the value of the sum
while number !=0:
    i =number % 10
    j=j+i
    number=number//10 # this takes the integer value of the number, this helps to get all the digits of the number
print("Sum of the digits are: " ,j)     


import math

problem = math.fabs(-874)
print(problem)
problem = math.copysign(78, -94)
print(str(problem) * 45)
name = "Kelly"
name += " "
name += "Evan"
name += " "
name += "Nehe"
print(name)
course = "Python For Beginners"
print(course[0:-1])


is_hot = False
is_cold = False

if is_hot:
    print("Drink water bitch")
elif is_cold:
    print("Wear a shitty jacket")
else:
    print("It's a freaking good day")

credit = False

if credit:
    money = 0.1 * 1000000
    print(f"Down payment: ${money}")
else:
    money = 0.2 * 1000000
    print(f"Down Payment: ${money}")

name = input("Write your name: ")
if len(name) < 3:
    print("Name must not be less than three characters")
elif len(name) > 50:
    print(" Name must not be above 50 characters")
else:
    print("Name looks good")

weight = int(input("Enter your weight: "))
choice = input("(L)bs or (K)g :")
if choice.upper() == "L":
    weight_pound = weight * 0.45
    print(f"You are {weight_pound} pounds")
elif choice.upper() == "K":
    print(f"You are {weight} kilograms")

# I am making a change here.

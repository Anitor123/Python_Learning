# Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

num1 = int(input("What's the first number? "))

for signs in operations:
    print(signs)
should_continue = True

while should_continue:
    operation_signs = input("Pick an operation form the line above: ")
    num2 = int(input("What's the next number? "))
    calculation_function = operations[operation_signs]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_signs} {num2} = {answer}")  

    if input(f"Type 'y' to continue calculating with {answer} or Type 'n' to exit: ") == "y":
        num1 = answer
    else:
        should_continue = False    
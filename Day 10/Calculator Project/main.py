import art

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def calculate(sign, n1, n2):
    if sign == "+":
        return float(add(n1, n2))
    elif sign == "-":
        return float(subtract(n1, n2))
    elif sign == "*":
        return float(multiply(n1, n2))
    elif sign == "/":
        return float(divide(n1, n2))
    else:
        return 0

calculator_directory = {"+", "-", "*", "/"}

should_continue = True
output = 0

while should_continue:
    print(art.logo)
    number1 = float(input("What's the first number?: "))

    continue_calculation = 'y'
    while continue_calculation == 'y':
        for calci in calculator_directory:
            print(calci)
        operation = input("Pick an operation: ")
        number2 = float(input("What's the next number?: "))
        output = calculate(operation, number1, number2)
        print(f"{number1} {operation} {number2} = {output}")
        continue_calculation = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")
        if continue_calculation == 'y':
            number1 = output
        else:
            output = 0
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def mod(num1, num2):
    return num1 % num2

operations = {
    "+": add, 
    "-": sub, 
    "*": mult, 
    "/": div,
    "%": mod,
}

def calculator():
    first_num = float(input("Type your first number\n"))
    for symbol in operations:
        print(symbol)
    num_operation = input("Pick a sign. Type ONLY the operating sign.\n")
    second_num = float(input("Type your second number\n"))

    result = operations[num_operation](first_num, second_num)
    print(f"{first_num} {num_operation} {second_num} = {result}")

    keep_result = input(f"Do you want to continue calculating with {result}? If so, type 'yes', otherwise type 'no'.\n")

    while keep_result == 'yes' or keep_result == 'y':
        first_num = result
        for symbol in operations:
            print(symbol)
        num_operation = input("Pick a sign. Type ONLY the operating sign.\n")
        second_num = float(input("Type your second number\n"))

        result = operations[num_operation](first_num, second_num)
        print(f"{first_num} {num_operation} {second_num} = {result}")

        keep_result = input(f"Do you want to continue calculating with {result}? If so, type 'yes', otherwise type 'no'.\n")
    
    if keep_result == 'no' or keep_result == 'n':
        calculator()

calculator()
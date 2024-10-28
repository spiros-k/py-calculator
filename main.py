def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

operations = {
    "+": add, 
    "-": sub, 
    "*": mult, 
    "/": div
}

y = operations["*"](4, 8)

x = mult(4, 8)
print(x, y)
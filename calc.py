'''tthis file is use for 
the module '''





# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is undefined"
    return a / b

# Function to check if a number is even or odd
def evenodd(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"

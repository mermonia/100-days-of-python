from art import logo
from replit import clear

print(logo)


def sum(a, b):
  print(f"{a} + {b} = {a+b}")
  return a + b


def subtract(a, b):
  print(f"{a} - {b} = {a-b}")
  return a - b


def multiply(a, b):
  print(f"{a} * {b} = {a*b}")
  return a * b


def divide(a, b):
  print(f"{a} / {b} = {a/b}")
  return a / b


operations = {"+": sum, "-": subtract, "*": multiply, "/": divide}

continue_program = True
while continue_program:
  first_number = float(input("What's the fist number? "))

  continue_input = True
  while continue_input:
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    
    second_number = float(input("What's the next number? "))
    first_number = operations[operation](first_number, second_number)
    
    continue_query = input(f"Type 'y' to continue calculating with {first_number}, or type 'n' to start a new calculation: ")
    continue_input = continue_query.lower() == 'y'

  clear()
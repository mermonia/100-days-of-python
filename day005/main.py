#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
letter_amount = len(letters)

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
number_amount = len(numbers)

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
symbol_amount = len(symbols)

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []

for letter in range(0, nr_letters):
    random_letter = letters[random.randint(0, letter_amount - 1)]
    password.append(random_letter)

for symbol in range(0, nr_symbols):
    random_symbol = symbols[random.randint(0, symbol_amount - 1)]
    random_position = random.randint(0, len(password))
    password.insert(random_position, random_symbol)

for number in range(0, nr_numbers):
    random_number = numbers[random.randint(0, number_amount - 1)]
    random_position = random.randint(0, len(password))
    password.insert(random_position, random_number)

password = "".join(password)

print(f"Here's you new password:\n{password}")

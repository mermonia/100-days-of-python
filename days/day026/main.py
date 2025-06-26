import pandas as pd

phonetic_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
letters = {entry.letter: entry.code
           for _, entry in phonetic_alphabet.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the
# user inputs.
user_input = input("Enter a valid string: ")

code_list = [letters[letter.upper()] for letter in user_input]
print(code_list)

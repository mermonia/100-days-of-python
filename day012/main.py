# Import some basic libraries.
from art import logo
print(logo)

from replit import clear
import random


# Displays the number of attempts the player has left.
def display_attempts():
    print(f"You have {lives} attempts left!")


# Prints whether the guessed number is above or below the target number. Does
# nothing if the numbers are equal.
def check_number_difference():
    if guessed_number > random_number:
        print("Too high!")
    elif guessed_number < random_number:
        print("Too low!")


# Called at the end of each game. Checks the game state, and prints some information
# about its result.
def check_end_game_state():
    if lives < 1:
        display_attempts()
        print("You are terrible at this game. Please don't come back.")
    elif game_difficulty.lower() != "hard":
        print("You won! What about trying not to be a pussy next time?")
    else:
        print(
            "You won! Against all odds, you finally did something worth of praise. Well done!"
        )


# Main loop of the code.
continue_playing = True
while continue_playing:
    print(
        "Welcome to the Russian Number Guesser!\nI just thought of a number between 1 and 100."
    )

    random_number = random.randint(1, 100)
    game_difficulty = input("Choose a difficulty (hard / pussy): ")

    if game_difficulty.lower() == "hard":
        lives = 6
    else:
        lives = 11

    guessed_number = -1
    while guessed_number != random_number and lives > 1:
        lives -= 1
        display_attempts()
        guessed_number = int(input("Make a guess: "))
        check_number_difference()

    check_end_game_state()

    continue_playing = input(
        "Do you want to play again? (Y/N): ").lower() == "y"

    clear()
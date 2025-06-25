rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

plays = [rock, paper, scissors]
plays_strings = ["rock", "paper", "scissors"]

player_choice = input("No game no life simulator fr fr. What path will you choose, chosen one? (Rock, Paper, Scissors)\n").lower()
computer_number = random.randint(0,2)

player_number = plays_strings.index(player_choice)
computer_choice = plays_strings[computer_number]

print(f"You drew {player_choice}!")
print(plays[player_number])

print(f"The computer drew {computer_choice}!")
print(plays[computer_number])

if player_choice == computer_choice:
  print("The game ends in a draw! Nice show, pussy.")
elif player_choice == "rock":
  if computer_choice == "paper":
    print("You lost. You are a disgrace to humanity.")
  elif computer_choice == "scissors":
    print("You won! A season 2 might be airing soon thanks to you!")
elif player_choice == "paper":
  if computer_choice == "scissors":
    print("You lost. You are a disgrace to humanity.")
  elif computer_choice == "rock":
    print("You won! A season 2 might be airing soon thanks to you!")
else:
  if computer_choice == "rock":
    print("You lost. You are a disgrace to humanity.")
  elif computer_choice == "paper":
    print("You won! A season 2 might be airing soon thanks to you!")
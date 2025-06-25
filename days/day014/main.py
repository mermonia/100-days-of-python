# Some basic imports
from art import logo, vs
print(logo)

from game_data import data
from replit import clear
import random

# Returns a formatted entry given its list index.
def get_entry(index):
  entry = data[index]
  return f"{entry['name']}, a {entry['description']}, from {entry['country']}."

# Prints information about two entries given their indexes.
def print_versus_entries(first_index, second_index):
  print("Compare A: " + get_entry(first_index))
  print(vs)
  print("Against B: " + get_entry(second_index))

# Returns "a" or "b", depending on the entries' follower count
def compare_entries(first_index, second_index):
  first_count = data[first_index]["follower_count"]
  second_count = data[second_index]["follower_count"]

  if first_count > second_count:
    return "a"
  return "b"

# Definition of the length of the list, to further clarify other functionalities.
LIST_LENGTH = len(data)

# Returns a random index from the entry list.
def get_random_index():
  return random.randint(0, LIST_LENGTH-1)

# Main loop of the program.
continue_playing = True
while continue_playing:
  current_score = 0
  first_index = get_random_index()
  second_index = get_random_index()
  player_is_right = True
  
  while player_is_right:
    second_index = get_random_index()
    print_versus_entries(first_index, second_index)

    player_answer = input("Who has more followers? (A/B): ").lower()
    clear()
    
    if player_answer == compare_entries(first_index, second_index):
      current_score += 1
      print(f"You're right! Current score: {current_score}.")
      
      if compare_entries(first_index, second_index) == "b":
        first_index = second_index
    else:
      print(f"Sorry, that's wrong. Final score: {current_score}")
      player_is_right = False
      continue_playing = input("Do you want to play again? (Y/N): ").lower() == "y"
      clear()
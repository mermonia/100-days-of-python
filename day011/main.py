############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##############################################################

from replit import clear
import random

from art import logo

print(logo)

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Draws a card, adds it to the selected hand and properly updates the score. Returns the score.
def draw_card(hand, score):
  card = random.randint(0, 12)
  hand.append(deck[card])
  score += deck[card]

  if score > 21:
    score = check_for_aces(hand, score)

  return score


# Checks for aces in the selected hand, and properly updates the score. Returns the score.
def check_for_aces(hand, score):
  for i in range(len(hand)):
    if hand[i] == 11:
      hand.pop(i)
      hand.insert(i, 1)
      score -= 10
      return score
  return score


# Prints the result of the game given two scores.
def check_winner(player, computer):
  if player == computer:
    print("The game ends in a draw!")
  elif player > 21:
    print("You went over! You lose :(")
  elif computer > 21:
    print("The computer went over! You win! :D")
  elif player > computer:
    print("Your final score is over the computer's! You win! :D")
  else:
    print("Your final score is under the computer's... You lose :(")


# Displays information about the game that must be known while playing.
def display_mid_game_info(player_hand, player_score, computer_hand):
  print(f"  Your cards: {player_hand}, current score: {player_score}")
  print(f"  Computer's first card: {computer_hand[0]}")


# Displays a final report about the game.
def display_end_game_info(player_hand, player_score, computer_hand,
                          computer_score):
  print(f"  Your cards: {player_hand}, final score: {player_score}")
  print(f"  Computer's cards: {computer_hand}, final score: {computer_score}")


start_new_game = input("Do you wanna play a game? (Y/N): ").lower() == 'y'
while start_new_game:
  # Declarations of the players' hands.
  player_hand = []
  computer_hand = []

  # Declarations of the players' scores.
  player_score = 0
  computer_score = 0

  # First two draws are forced.
  for i in range(2):
    player_score = draw_card(player_hand, player_score)
    computer_score = draw_card(computer_hand, computer_score)

  display_mid_game_info(player_hand, player_score, computer_hand)

  # Asking the player for new cards.
  player_draws_card = input("Do you want another card? (Y/N): ").lower() == 'y'
  while player_draws_card and player_score <= 21:
    player_score = draw_card(player_hand, player_score)

    if player_score <= 21:
      display_mid_game_info(player_hand, player_score, computer_hand)
      player_draws_card = input(
          "Do you want another card? (Y/N): ").lower() == 'y'

  while player_score <= 21 and player_score > computer_score and computer_score < 17:
    computer_score = draw_card(computer_hand, computer_score)

  display_end_game_info(player_hand, player_score, computer_hand,
                        computer_score)
  check_winner(player_score, computer_score)
  start_new_game = input(
      "Do you wanna start a new game? (Y/N): ").lower() == 'y'
  clear()

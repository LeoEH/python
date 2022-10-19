from logo import logo
import random
import os
#from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
  card = random.choice(cards)
  return card


def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):

  # if user_score > 21 and computer_score > 21:
  #   return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"


def play():

  print(logo)
  my_cards = []
  cpu = []

  is_game_over = False

  for _ in range(2):
    my_cards.append(deal_card())
    cpu.append(deal_card())
  
  while not is_game_over:
    os.system("cls")
    user_score = calculate_score(my_cards)
    computer_score = calculate_score(cpu)

    print(f"   Your cards: {cpu}, current score: {user_score}")
    print(f"   Computer's first card: {cpu[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        my_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    cpu.append(deal_card())
    computer_score = calculate_score(cpu)

  print(f"   Your final hand: {my_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {cpu}, final score: {computer_score}")
  print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  #clear()
  play()



print("HAVE A NICE DAY AND SEE U SOON   ")
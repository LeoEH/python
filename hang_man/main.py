import random
from hangman_art import stages, logo
from hangman_words import word_list


#print(logo)
# game_is_finished = False
# lives = len(stages) - 1



word = random.choice(word_list)

print(word)

word_dash = []
for _ in range(len(word)):
  word_dash.append("_")
print(word_dash)

game_over = False
lives = 6
while not game_over:
  guess = input("guess a letter: ")
  
  for position in range(len(word)):
    letter = word[position]
    
    if letter in guess:
      word_dash[position]= letter
  else:
    lives -= 1
    print(f"U have {lives} lefft")
    if lives == 0:
      print("GAME OVER")
      game_over = True
  
  
  print(word_dash)
import random
import re

word_list = ["home", "pub", "hotel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def check_word(guess):
  known_letters.extend(guess)
  regex = f"[^{'|'.join(known_letters)}]"
  tmp_chosen_word = chosen_word

  return re.sub(regex, '_', tmp_chosen_word)

def print_display():
  print(guess_word)
  print(stages[lives])

chosen_word = random.choice(word_list)
known_letters = []
guess_word = check_word(" ")
lives = 6

while (chosen_word != guess_word) & (lives > 0):
  print_display()

  guess = input("Guess a letter: ").lower()
  right_answer = (chosen_word.find(guess) != -1) | (guess in known_letters)

  if right_answer:
    guess_word = check_word(guess)
  else:
    lives -= 1

print_display()
if lives == 0:
  print("You lose!")
elif chosen_word == guess_word:
  print("You win!")


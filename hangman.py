import random
from words import words

def get_valid_word(words):
  #take one word from the list
  words = random.choices(words)
  #if the word has - or space
  while '-' in word or ' ' in word: 
  word = random.choices(words)
return word

def hangman():
  word = get_valid_word(words)
  word_latters = set(word)
  alphabet = set(string.ascii_uppercase)
  user_letters = set()
  user_letter = input('Guess a letter: ').upper()

user_input = input('Type something: ')

print(user_input)

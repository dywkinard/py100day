import random
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
lives = 6
game_end = False
word_list = ["aardvark", "baboon", "camel"]
word = word_list[random.randint(0, 2)]
display = list()
for letter in word:
    display.append("_")
  
while not game_end:

  if lives == 0:
    print("\n*** Game Over ***\n")
    break

  print(stages[lives])
  print(f"{' '.join(display)}\n")
  
  guess = input("Guess a letter: ").lower()
  
  for letter in range(0, len(display)):
    if guess not in word:
      print("\nWrong guess!!!")
      lives -= 1
      break
    if guess == word[letter]:
      display[letter] = guess
      
  if "".join(display) == word:
    game_end = True
    print(f"{' '.join(display)}\n")
    print("You win!")
  
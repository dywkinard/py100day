from art import *
import random

#Write your code below this line 👇
rps = [rock, paper, scissors]
comp_choice = random.randint(0, 2)
player_choice = None
while True: 
  player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
  if player_choice == "0" or player_choice == "1" or player_choice == "2":
    break
choices = str(comp_choice) + str(player_choice)
print(rps[int(player_choice)])
print("Compuer chose:")
print(rps[comp_choice])

if choices == "00" or choices == "11" or choices == "22":
  print("Tie")
elif choices == "01" or choices == "12" or choices == "02":
  print("You win")
else:
  print("You lose")

  
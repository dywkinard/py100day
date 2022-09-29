import random
import os
current_answer = None
from art import logo, vs
from game_data import data

print(logo)

def game():
  score = 0
  while True:
    if score == 0:
      comp_a = obtain_comp()
    else:
      comp_a = current_answer
    print(f"Compare A: {comp_a['name']}, a {comp_a['description']}, from {comp_a['country']}.")
    
    print(vs)
    
    comp_b = obtain_comp()
    print(f"Compare A: {comp_b['name']}, a {comp_b['description']}, from {comp_b['country']}.")

    if comp_a['follower_count'] > comp_b['follower_count']:
      print("PSST A IS THE ANSWER")

    elif comp_a['follower_count'] < comp_b ['follower_count']:
      print("PSST B IS THE ANSWER")
    
    answer = input("who has more followers? Type 'A' or 'B': ").upper()
    
    if check_answer(answer, comp_a, comp_b):
      os.system('cls' if os.name == 'nt' else 'clear')
      if comp_a['follower_count'] > comp_b['follower_count']:
        current_answer = comp_a
      else:
        current_answer = comp_b
      print(logo)
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      os.system('cls' if os.name == 'nt' else 'clear')
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      break
    
      
def obtain_comp():
  return data[random.randint(0, len(data) - 1)]

def check_answer(string, a, b):
    
  if a['follower_count'] > b['follower_count'] and string == "A":
    return True
  elif a['follower_count'] < b['follower_count'] and string == "B":
    return True
  else:
    return False

game()
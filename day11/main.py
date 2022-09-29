from art import logo
import random
import os
print(logo)
game_end = False
user_cards = []
user_score = 0
computer_cards = []
computer_score = 0

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return cards[random.randint(0, 12)]

def calculate_score(cards):
    if sum(cards) == 21:
        return 0
    elif sum(cards) > 21:
        if 11 in cards:
            cards.remove(11)
            cards.append(1)
            return sum(cards)
        else:
            return sum(cards)
    else:
        return sum(cards)

def compare_score(user, computer):
    if user == computer:
        print("Tied")
    elif computer > user:
        print("Dealers Hand")
    elif user > computer:
        print("Player wins!")
    elif compter == 0:
        print("Computer wins!")
    elif user == 0: 
        print("Player wins!")

while True:

    for deal in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_end:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            break
        else:
            print("Dealers Cards: ")
            for card in range(0, len(computer_cards) - 1):
                print(f"{computer_cards[card]} ", end="")
            print("\nPlayer Cards: ")
            for card in user_cards:
                print(f"{card} ", end="")
                
            if computer_score < 17:
                computer_cards.append(deal_card())
   
            draw_card = input("\nDo you wish to draw another card? (y / n): ")

            if draw_card.lower() == "y" or draw_card.lower() == "yes":
                user_cards.append(deal_card())
            else:
                game_end = True

    compare_score(user_score, computer_score)

    restart = input("Do you wish to play again? (y/n): ")

    if restart.lower() == "n":
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    else:
        user_cards = list()
        computer_cards = list()
        game_end = False
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

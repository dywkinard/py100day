from art import logo


print(logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
found = False
while not found:
    print("You arrive at a cross roads")
    choice = input("Which way would you like to got? (Left / Right): ")
    if choice.lower() == "right":
        print("You found the not so hidden treasure!")
        found = True
    else:
        print("You get the feeling you chose the wrong path\nYou trip and end up back where you started")
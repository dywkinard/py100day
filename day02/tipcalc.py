print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = float(input("What would you like to tip? (10/12/15)? "))
split = int(input("How many people are splitting the bill? "))
total = ((bill * (tip / 100)) + bill) / split
print("Each person will pay {:.2f}".format(total))
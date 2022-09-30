import turtle as t
from random import randint

turtle_list = []
y = -100
x = -225


def create_turtle(color, xpos, ypos):
    new_turtle = t.Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(xpos, ypos + 30.00)
    turtle_list.append(new_turtle)


is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for turtle in colors:
    create_turtle(turtle, x, y)
    y += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} is the winner!")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()

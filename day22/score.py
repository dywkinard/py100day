from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.speed(0)
        self.penup()
        self.color('white')
        self.hideturtle()

    def display(self, score):
        self.goto(self.position)
        self.write(f"{score}", True, align="center", font=("Courier", 50, 'normal'))

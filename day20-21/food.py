from snake import Turtle
from random import randrange


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(randrange(-280, 280, 20), randrange(-280, 280, 20))

from turtle import Turtle


class Panel(Turtle):
    def __init__(self, x):
        super().__init__()
        self.score = 0
        self.penup()
        self.shape('square')
        self.color('white')
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(x, 0)

    def go_up(self):
        if self.ycor() > 200:
            pass
        else:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() < -200:
            pass
        else:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.get_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", True, align="center", font=('Ubuntu', 16, 'normal'))

    def get_score(self):
        self.goto(0, 260)
        self.write(f"Score:   {self.score}", True, align="center", font=('Ubuntu', 16, 'normal'))

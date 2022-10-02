from panel import Panel
from turtle import Screen, pendown
from ball import Ball
from score import Scoreboard
import time

game_on = True

left_panel = Panel(-350, 0)
right_panel = Panel(350, 0)
ball = Ball()
score = Scoreboard()
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.listen()
screen.onkey(left_panel.go_up, 'w')
screen.onkey(left_panel.go_down, 's')
screen.onkey(right_panel.go_up, 'Up')
screen.onkey(right_panel.go_down, 'Down')

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.movement()

    # Detect ball collisions
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ybounce()
    if ball.distance(right_panel) < 50 and ball.xcor() > 320 or ball.distance(left_panel) < 50 and ball.xcor() < -320:
        ball.xbounce()
    # Detect if panel misses  
    if ball.xcor() > 380: 
        ball.reset()
        score.l_point()
    elif ball.xcor() < -380:
        ball.reset()
        score.r_point()

screen.exitonclick()

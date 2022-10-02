from panel import Panel
from turtle import Screen, pendown
from ball import Ball
from score import Scoreboard
import time

game_on = True

left_panel = Panel(-350, 0)
lscore = Scoreboard((-50, 240))
lscore.display(left_panel.score)
right_panel = Panel(350, 0)
rscore = Scoreboard((50, 240))
rscore.display(right_panel.score)
ball = Ball()
y_pos = -280
lines = []
for line in range(20):
    line = Panel(0, y_pos)
    line.speed(0)
    line.turtlesize(stretch_wid=.8, stretch_len=0.1)
    lines.append(line)
    y_pos += 30
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
    time.sleep(0.1)
    screen.update()
    ball.movement()

    # Detect ball collisions
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ybounce()
    if ball.distance(right_panel) < 50 and ball.xcor() > 320 or ball.distance(left_panel) < 50 and ball.xcor() < -320:
        ball.xbounce()
    # Detect if panel misses  
    if ball.xcor() > 380: 
        left_panel.score += 1
        lscore.clear()
        lscore.display(left_panel.score)
        ball.reset()
    elif ball.xcor() < -380:
        right_panel.score += 1
        rscore.clear()
        rscore.display(right_panel.score)
        ball.reset()
        

screen.exitonclick()

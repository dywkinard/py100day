from panel import Panel
from turtle import Screen
from ball import Ball
import time

game_on = True

left_panel = Panel(-350)
right_panel = Panel(350)
ball = Ball()
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
        ball.reset()
        print(f"Lefts Score: {left_panel.score}\n Rights Score: {right_panel.score}")
    elif ball.xcor() < -380:
        right_panel.score += 1
        ball.reset()
        print(f"Lefts Score: {left_panel.score}\n Rights Score: {right_panel.score}")
        

screen.exitonclick()

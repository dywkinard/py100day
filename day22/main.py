from turtle import Screen
from panel import Panel

game_on = True

left_panel = Panel(-350)
right_panel = Panel(350)
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
    screen.update()

screen.exitonclick()

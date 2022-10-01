from snake import Snake
from food import Food
from scoreboard import Score
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_over = False
while not game_over:
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.score += 1
        score.clear()
        score.get_score()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_over = True
        score.game_over()

    for seg in snake.body[1:]:
        if snake.head.distance(seg) < 10:
            game_over = True
            score.game_over()

screen.exitonclick()

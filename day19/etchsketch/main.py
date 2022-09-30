from turtle import Screen, Turtle


def move_forward():
    em.forward(10)


def move_left():
    em.left(10)


def move_back():
    em.back(10)


def move_right():
    em.right(10)


def clear():
    em.penup()
    em.clear()
    em.home()
    em.pendown()


em = Turtle()
em.speed(0)
screen = Screen()
screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='a', fun=move_left)
screen.onkey(key='s', fun=move_back)
screen.onkey(key='d', fun=move_right)
screen.onkey(key='r', fun=clear)
screen.exitonclick()

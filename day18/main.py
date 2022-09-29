import turtle as t
import colorgram as cg
import random as rand

t.colormode(255)
color_list = cg.extract("imgs/hirst.jpg", 10)
color_palette = []

for count in range(len(color_list)):
    rgb = color_list[count]
    color = rgb.rgb
    color_palette.append(color)

x = -300.00
y = -240.00
em = t.Turtle()
em.hideturtle()
em.speed(0)
em.up()
em.goto(x, y)

for row in range(10):
    for dots in range(10):
        em.pencolor(color_palette[rand.randint(0, len(color_list) - 1)])
        em.dot(30)
        em.forward(60)
    y += 60
    em.goto(x, y)


screen = t.Screen()
screen.exitonclick()

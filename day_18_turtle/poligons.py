from turtle import Turtle, Screen
from random import randint

chiquinha = Turtle()
screen = Screen()
screen.colormode(255)

for x in range(3, 11):
    y = x
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    chiquinha.pencolor(r, g, b)
    while y > 0:
        chiquinha.forward(100)
        chiquinha.right(360 / x)
        y -= 1

screen.exitonclick()
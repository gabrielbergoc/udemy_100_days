from turtle import Turtle, Screen
from random import randint, choice

chiquinha = Turtle()
chiquinha.hideturtle()
chiquinha.speed(0)

screen = Screen()
screen.screensize(1920, 1080)
screen.colormode(255)

for x in range(100):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    chiquinha.color(r, g, b)
    chiquinha.circle(100)
    chiquinha.right(3.6)



screen.exitonclick()
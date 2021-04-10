from turtle import Turtle, Screen
from random import randint, choice

WIDTH = 800
HEIGHT = 600

chiquinha = Turtle()
chiquinha.width(5)
# chiquinha.hideturtle()
chiquinha.speed(0)

screen = Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)
screen.screensize(WIDTH, HEIGHT)
screen.colormode(255)

for x in range(10000):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    chiquinha.color(r, g, b)

    if chiquinha.xcor() > WIDTH//2:
        chiquinha.penup()
        chiquinha.setposition(x=-WIDTH//2,y=chiquinha.ycor())
        chiquinha.pendown()

    elif chiquinha.xcor() < -WIDTH//2:
        chiquinha.penup()
        chiquinha.setposition(x=WIDTH//2, y=chiquinha.ycor())
        chiquinha.pendown()

    elif chiquinha.ycor() > HEIGHT//2:
        chiquinha.penup()
        chiquinha.setposition(x=chiquinha.xcor(), y=-HEIGHT//2)
        chiquinha.pendown()

    elif chiquinha.ycor() < -HEIGHT//2:
        chiquinha.penup()
        chiquinha.setposition(x=chiquinha.xcor(), y=HEIGHT//2)
        chiquinha.pendown()

    chiquinha.forward(20)
    turn = choice([0, 90, 180, 270])
    chiquinha.right(turn)

screen.exitonclick()
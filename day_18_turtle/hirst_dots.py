from turtle import Turtle, Screen
from random import randint, choice
import colorgram

dots_colors = colorgram.extract('Damien_Hirst_Dot_Painting_1992.jpg', 50)

pallete = [dots_colors[i].rgb for i in range(len(dots_colors)) if dots_colors[i].proportion < 0.70]

# for color in pallete:
#     print(color)

screen = Screen()
screen.screensize(800, 600)
screen.colormode(255)
screen.setworldcoordinates(-20,-20,780,580)

chiquinha = Turtle()
chiquinha.hideturtle()
chiquinha.speed(0)
chiquinha.penup()

for i in range(13):
    for j in range(13):
        color = choice(pallete)
        chiquinha.color(color)
        chiquinha.dot(30)
        chiquinha.forward(60)
    chiquinha.goto(0, (i + 1) * 60)


screen.exitonclick()
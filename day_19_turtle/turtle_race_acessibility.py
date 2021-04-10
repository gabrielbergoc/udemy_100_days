from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.title('Turtle Race (Different Shapes) 1.0')
screen.setup(width=500, height=400)
screen.setworldcoordinates(llx=0, lly=-200, urx=500, ury=200)
user_bet = screen.textinput(title='Place your bet', prompt='Which turtle do you bet on? (turtle, arrow, circle, square, triangle or classic)')

line = Turtle()
line.hideturtle()
line.penup()
line.goto(x=450, y=150)
line.right(90)
line.pendown()
line.forward(300)
del line

colors = ['purple', 'blue', 'cyan', 'green', 'orange', 'red']
shapes = ['turtle', 'arrow', 'circle', 'square', 'triangle', 'classic']
positions = [125, 75, 25, -25, -75, -125]
turtles = []

for i in range(6):
    tim = Turtle()
    tim.color(colors[i])
    tim.shape(shapes[i])
    tim.penup()
    tim.goto(0, positions[i])
    turtles.append(tim)


is_race_on = True

while is_race_on:

    for turtle in turtles:
        turtle.forward(randint(0, 10))

        if turtle.xcor() > 450:
            winner_shape = turtle.shape()
            is_race_on = False

screen.bye()

if user_bet == winner_shape:
    res = 'win'
else:
    res = 'lose'

print(f'You {res}. The winner was {winner_shape}.')
input()
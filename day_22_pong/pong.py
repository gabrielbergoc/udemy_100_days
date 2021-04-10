from turtle import Screen
from paddleClass import Paddle
from ballClass import Ball
from scoreboardClass import ScoreBoard
import time

# constants
WIDTH = 800
HEIGHT = 600
DIFFICULTIES = {"easy": 2, "medium": 3, "hard": 4, "impossible": 5}

# initialize screen
screen = Screen()
screen.title("Pong")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.tracer(n=0) # disable screen tracer to set custom refresh rates

# asks if there's 1 or 2 players
user_input = screen.textinput("Welcome to Pong!", "1P or 2P?")

if user_input == "1P" or user_input == "1p":
    difficulty = screen.textinput("Welcome to Pong!", "Which difficulty? (easy/medium/hard/impossible)")
    r_paddle = Paddle(x=WIDTH // 2 - 50, window_height=HEIGHT, velocity=20)
    l_paddle = Paddle(x=-WIDTH // 2 + 50, window_height=HEIGHT, velocity=DIFFICULTIES[difficulty])
    cpu = True
else:
    cpu = False
    r_paddle = Paddle(x=WIDTH // 2 - 50, window_height=HEIGHT, velocity=20)
    l_paddle = Paddle(x=-WIDTH // 2 + 50, window_height=HEIGHT, velocity=20)

# initialize paddles and ball

ball = Ball(window_width=WIDTH, window_height=HEIGHT)

# initialize scoreboard
scoreboard = ScoreBoard(window_height=HEIGHT)

# main loop
while True:
    # listen to key presses
    screen.listen()
    screen.onkeypress(fun=screen.bye, key="Escape")
    screen.onkeypress(fun=r_paddle.moveUp, key="Up")
    screen.onkeypress(fun=r_paddle.moveDown, key="Down")

    # 1 player mode
    if cpu:
        if ball.ycor() > l_paddle.ycor():
            l_paddle.moveUp()
        if ball.ycor() < l_paddle.ycor():
            l_paddle.moveDown()

    # 2 players mode
    else:
        screen.onkeypress(fun=l_paddle.moveUp, key="w")
        screen.onkeypress(fun=l_paddle.moveDown, key="s")

    # checks for scores
    if ball.r_score():
        scoreboard.r_score += 1
    if ball.l_score():
        scoreboard.l_score += 1

    # ball, scoreboard and screen update
    ball.update(l_paddle, r_paddle)
    scoreboard.update()
    screen.update()
    time.sleep(0.01)

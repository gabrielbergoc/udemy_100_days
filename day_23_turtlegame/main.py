import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

GRID = {
        "y": [0 + i for i in range(-240, 260, 20)],
        "x": [-300 + i for i in range(0, 620, 20)],
        }

DIFFICULTIES = {"easy": 10, "medium": 15, "hard": 20, "impossible": 40}

# initialize screen
screen = Screen()
screen.title("Turtle")
screen.setup(width=600, height=600)
screen.tracer(0)
player_choice = screen.textinput("Welcome to Turtle!", "Which difficulty? (easy/medium/hard/impossible")

#initialize player, scoreboard and car manager
player = Player()
scoreboard = Scoreboard(player=player)
car_manager = CarManager(number=DIFFICULTIES[player_choice], grid=GRID, player=player)

# main loop
while player.is_alive:

    # listen to key presses
    screen.listen()
    screen.onkeypress(fun=player.move, key="Up")
    screen.onkey(fun=screen.bye, key="Escape")

    # updates
    player.update()
    car_manager.update()
    scoreboard.update()
    time.sleep(0.1)
    screen.update()

scoreboard.game_over()
screen.exitonclick()
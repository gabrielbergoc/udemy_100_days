from turtle import Screen
from snakeClass import Snake
from foodClass import Food
from scoreboardClass import ScoreBoard, InsaneMode
import time

# dictionary with window sizes, grids for food placement and score multipliers
grids = {
"small": {"grid": [-220 + i for i in range(20, 440, 20)], "size": 440, "multiplier": 3},
"medium": {"grid": [-260 + i for i in range(20, 520, 20)], "size": 520, "multiplier": 2},
"big": {"grid": [-300 + i for i in range(20, 600, 20)], "size": 600, "multiplier": 1},
}

# list of sleep times between each loop
speeds = [0.3, 0.2, 0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01]

# dictionary relating an user input with each "speed"
speeds_dict = {i + 1: speeds[i] for i in range(len(speeds))}

def main():
    # initialize screen
    screen = Screen()
    screen.title("Snake")
    screen.tracer(0)

    # ask for user inputs for window size and snake speed
    chosen_grid = screen.textinput("Welcome to Snake!","Choose a window size (small/medium/big): ")
    insane_choice = screen.textinput("Welcome to Snake!", "Insane mode? (yes/no)")

    if insane_choice == "yes":
        speed = 1
        insane_mode = True
    else:
        speed = screen.numinput("Welcome to Snake!", f"Choose a speed (1-{len(speeds)}): ")
        insane_mode = False

    # initialize food, snake and scoreboard
    chosen_size = grids[chosen_grid]["size"]
    food = Food(grids[chosen_grid]["grid"])
    snake = Snake(chosen_size)
    scoreboard = ScoreBoard(chosen_size)

    if insane_mode:
        insane_writer = InsaneMode(chosen_size)

    # setup screen of the chosen size, color, title
    width = height = grids[chosen_grid]["size"]
    screen.setup(width=width, height=height)
    screen.bgcolor("black")
    screen.title("Snake")

    # updates screen to show snake, first food piece and scoreboard
    screen.update()

    # main loop
    # stops when snake collides with itself or obstacles
    while snake.is_alive():

        # checks for collision with food and updates food position if necessary
        # also increments scoreboard score according to difficulty
        if snake.head.distance(food) < 15:
            snake.lenght += 1
            food.update()
            scoreboard.score += int(grids[chosen_grid]["multiplier"] * speed)

            # increments difficulty on insane mode
            if insane_mode and speed < 12:
                speed += 1
                insane_writer.level += 1

        # listen to user key presses
        screen.listen()
        screen.onkey(fun=snake.turnUp, key="Up")
        screen.onkey(fun=snake.turnDown, key="Down")
        screen.onkey(fun=snake.turnLeft, key="Left")
        screen.onkey(fun=snake.turnRight, key="Right")
        screen.onkey(fun=screen.bye, key="Escape")

        # update snake, scoreboard, insane lvl and screen
        snake.update()
        scoreboard.update()
        screen.update()
        if insane_mode:
            insane_writer.update()

        # loop delay / speed control
        time.sleep(speeds_dict[speed])

    # game over screen
    scoreboard.game_over()
    screen.textinput("Game Over", "Press any key to play again")
    snake.reset()
    scoreboard.reset()
    screen.clear()
    main()

if __name__ == '__main__':
    main()
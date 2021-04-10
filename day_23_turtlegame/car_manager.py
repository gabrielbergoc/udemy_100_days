COLORS = ["red", "orange", "cyan", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
from random import choice

class CarManager():

    def __init__(self, number, grid, player):
        self.grid = grid
        self.cars = []
        self.player = player

        for i in range(number):
            self.create_car()

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(choice(COLORS))
        car.penup()
        car.setposition(choice(self.grid["x"]), choice(self.grid["y"]))
        self.cars.append(car)

    def update(self):
        for car in self.cars:

            # move cars
            car.backward(STARTING_MOVE_DISTANCE * self.player.level)

            # checks for out of screen cars
            # and moves them to the other side of the screen if yes (random ycor and color)
            if car.xcor() < -320:
                car.setposition(320, choice(self.grid["y"]))
                car.color(choice(COLORS))

            if car.distance(self.player) < 25:
                self.player.is_alive = False
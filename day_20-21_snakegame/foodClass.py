from turtle import Turtle
from random import choice



class Food(Turtle):

    def __init__(self, grid: list):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.grid = grid
        self.setposition(x=choice(self.grid), y=choice(self.grid))

    def update(self):
        self.setposition(x=choice(self.grid), y=choice(self.grid))
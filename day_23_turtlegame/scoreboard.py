FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, player):
        super(Scoreboard, self).__init__()
        self.penup()
        self.hideturtle()
        self.setposition(-280, 260)
        self.player = player

    def update(self):
        self.clear()
        self.write(arg=f"Level: {self.player.level}", move=False, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write(arg="GAME OVER", move=False, font=FONT)
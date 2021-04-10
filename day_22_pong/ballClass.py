from turtle import Turtle
from random import randint

class Ball(Turtle):

    def __init__(self, window_width, window_height):
        super(Ball, self).__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_velocity = randint(2, 6)
        self.y_velocity = randint(2, 6)
        self.window_width = window_width
        self.window_height = window_height

    # moves ball
    def move(self):
        self.setposition(x=self.x_velocity + self.xcor(), y=self.y_velocity + self.ycor())

    # checks for collisions with horizontal walls
    def wall_bounce(self):
        if self.ycor() > self.window_height // 2 - 15 or self.ycor() < -self.window_height // 2 + 20:
            self.y_velocity = -self.y_velocity

    # checks for collisions with paddles and randomly changes velocities
    def paddle_bounce(self, l_paddle, r_paddle):

        # right paddle
        if self.xcor() > self.window_width // 2 - 70 and self.distance(r_paddle) < 50:
            self.x_velocity = -randint(2, 6)
            self.y_velocity = randint(2, 6)

        #left paddle
        if self.xcor() < -self.window_width // 2 + 70 and self.distance(l_paddle) < 50:
            self.x_velocity = randint(2, 6)
            self.y_velocity = randint(2, 6)

    # checks for scores, resets ball position at the center of the screen and returns True if yes
    def l_score(self):
        if self.xcor() > self.window_width // 2:
            self.setposition(x=0, y=0)
            self.x_velocity = randint(2, 6)
            self.y_velocity = randint(2, 6)
            return True

    def r_score(self):
        if self.xcor() < -self.window_width // 2:
            self.setposition(x=0, y=0)
            self.x_velocity = -randint(2, 6)
            self.y_velocity = randint(2, 6)
            return True

    def update(self, l_paddle, r_paddle):
        self.wall_bounce()
        self.paddle_bounce(l_paddle, r_paddle)
        self.move()



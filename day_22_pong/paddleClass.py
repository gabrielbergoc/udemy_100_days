from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x, window_height, velocity):
        super(Paddle, self).__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.setposition(x=x, y=0)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.window_height = window_height
        self.velocity = velocity

    def moveUp(self):
        self.forward(self.velocity)

        if self.ycor() > self.window_height // 2 - 50:
            self.setposition(x=self.xcor(), y=self.window_height // 2 - 50)

    def moveDown(self):
        self.backward(self.velocity)

        if self.ycor() < -self.window_height // 2 + 50:
            self.setposition(x=self.xcor(), y=-self.window_height // 2 + 50)
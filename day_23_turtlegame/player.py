STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.setposition(STARTING_POSITION)
        self.velocity = MOVE_DISTANCE
        self.is_alive = True
        self.level = 1

    def move(self):
        self.forward(self.velocity)

    def update(self):
        if self.ycor() > FINISH_LINE_Y:
            self.setposition(STARTING_POSITION)
            self.level += 1
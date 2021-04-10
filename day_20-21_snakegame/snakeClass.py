from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

LENGHT = 3

class Snake:

    def __init__(self, window_size, lenght=LENGHT):
        self.lenght = lenght
        self.segments = []
        self.create()
        self.head = self.segments[0]
        self.direction = RIGHT
        self.window_size = window_size

    def create(self):
        for i in range(self.lenght):
            x_position = i * -20
            self.add_segment((x_position, 0))

    def reset(self):
        for segment in self.segments:
            del segment
        self.create()
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def move(self):
        # moves each snake segment, from the last to the second (head is moved below)
        for i in range(len(self.segments) - 1, 0, -1):
            new_position = self.segments[i - 1].position()
            self.segments[i].setposition(new_position)

        # moves head of the snake
        self.head.setheading(self.direction)
        self.head.forward(20)

        # checks if snake is outside of the screen
        # if it is, moves it to the opposite side of the screen
        current_position = self.head.position()
        if current_position[0] > self.window_size // 2:
            self.head.setposition(x=-self.window_size // 2, y=current_position[1])
        if current_position[0] < -self.window_size // 2:
            self.head.setposition(x=self.window_size // 2, y=current_position[1])
        if current_position[1] > self.window_size // 2:
            self.head.setposition(x=current_position[0], y=-self.window_size // 2)
        if current_position[1] < -self.window_size // 2:
            self.head.setposition(x=current_position[0], y=self.window_size // 2)

    # checks for collisions with itself
    def is_alive(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return False

        return True

    def turnUp(self):
        if self.direction != DOWN:
            self.direction = UP

    def turnDown(self):
        if self.direction != UP:
            self.direction = DOWN

    def turnRight(self):
        if self.direction != LEFT:
            self.direction = RIGHT

    def turnLeft(self):
        if self.direction != RIGHT:
            self.direction = LEFT

    def update(self):
        if self.lenght > len(self.segments):
            self.add_segment(self.segments[-1].position())

        self.move()
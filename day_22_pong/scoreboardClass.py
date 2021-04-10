from turtle import Turtle

ALIGNMENT = "center"
FONT = "Small Fonts"

class ScoreBoard(Turtle):
    
    def __init__(self, window_height):
        super(ScoreBoard, self).__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.r_score = 0
        self.l_score = 0
        self.window_top = window_height // 2
        self.setposition(0, self.window_top - 60)

    def update(self):
        self.clear()
        self.write(arg=f"Score:\n  {self.l_score} : {self.r_score}", move=False, align=ALIGNMENT,
                   font=(FONT, 18, "normal"))

    def game_over(self):
        self.setposition(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT,
                   font=(FONT, 18, "normal"))


class InsaneMode(ScoreBoard):

    def __init__(self, window_size, level=1):
        super(InsaneMode, self).__init__(window_size)
        self.level = level
        self.setposition(0, -self.window_top + 10)

    def update(self):
        self.clear()
        self.write(arg=f"INSANE MODE LVL: {self.level}", move=False, align=ALIGNMENT,
                   font=("Reprise Title STD", 18, "normal"))

from turtle import Turtle

ALIGNMENT = "center"
FONT = "Small Fonts"


class ScoreBoard(Turtle):
    
    def __init__(self, window_size):
        super(ScoreBoard, self).__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.highscore = self.get_highscore()
        self.window_top = window_size // 2
        self.setposition(0, self.window_top - 28)

    def update(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", move=False, align=ALIGNMENT,
                   font=(FONT, 18, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0

    def get_highscore(self):
        with open("highscore.txt", mode="r") as file:
            highscore = file.read()
            return int(highscore) if len(highscore) > 0 else 0

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

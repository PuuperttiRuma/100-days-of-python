from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score} ",False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()



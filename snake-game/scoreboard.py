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
        self.highscore = self.get_highscore()
        self.update_scoreboard()

    def get_highscore(self):
        with open("highscore.txt") as file:
            try:
                highscore = int(file.read())
            except ValueError:
                print("Error reading highscore file!")
                return 0
        return highscore

    def write_highscore(self):
        with open("highscore.txt", "w") as file:
            file.write(f"{self.highscore}")

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} ",False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_highscore()
        self.goto(0,0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)
        self.goto(0,-30)
        self.write(f"High score: {self.highscore}", False, ALIGNMENT, FONT)
        # self.goto(0, -120)
        # self.write("(Press 'Enter' to play again, 'q' to quit)", False, ALIGNMENT, FONT)



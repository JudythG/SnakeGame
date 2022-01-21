from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Helvetica", "12")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 295)
        self.color("white")
        self.display()

    def increment_score(self):
        self.score += 1
        self.display()

    def display(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
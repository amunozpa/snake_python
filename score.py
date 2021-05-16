from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.write(f"Score : {self.score}", move=False, align="center", font=("Arial", 14, "normal"))

    def score_up(self):
        self.score += 1
        self.write(f"Score : {self.score}", move=False, align="center", font=("Arial", 14, "normal"))

    def final_score(self):
        self.home()
        self.write(f"Your Score was : {self.score}", move=False, align="center", font=("Arial", 14, "normal"))

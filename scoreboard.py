from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.write(f"Score: {self.score}", move=False, align='center', font=('Verdana', 12, 'normal'))
        self.penup()
        self.goto(-25, 280)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='left', font=('Verdana', 12, 'normal'))

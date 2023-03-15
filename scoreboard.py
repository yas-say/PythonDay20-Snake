from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape()
        self.penup()
        self.score = 0
        self.goto(-25,280)
        self.hideturtle()

    def print_score(self):
        self.write(f"Score: {self.score}", move=False, align='left', font=('Verdana', 12, 'normal'))

    def increment_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='left', font=('Verdana', 12, 'normal'))

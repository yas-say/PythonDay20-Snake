from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Verdana', 12, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.highscore = self.read_hiscore()
        print(self.highscore)
        self.write(f"Score: {self.score} and HI Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("hiscore.txt", mode = 'w') as file:
                file.write(str(self.highscore))
        self.write(f"Score: {self.score} and HI Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def read_hiscore(self):
        with open("hiscore.txt") as file:
            return file.read()




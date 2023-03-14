from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()


    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            xcord = self.segments[seg - 1].xcor()
            ycord = self.segments[seg - 1].ycor()
            self.segments[seg].goto(xcord, ycord)
        self.segments[0].forward(20)
        self.segments[0].left(90)

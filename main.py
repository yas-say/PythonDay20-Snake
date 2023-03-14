from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("Black")
screen.tracer(0)

# t1 = Turtle(shape="square")
# t1.color("white")
# t2 = Turtle(shape="square")
# t2.color("white")
# t3 = Turtle(shape="square")
# t3.color("white")
# t2.setpos(x=t1.xcor()-20, y=0)
# t3.setpos(x=t2.xcor()-20, y=0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

game_on = True
while game_on:
    time.sleep(0.1)
    # for _ in segments:
    #     _.forward(20)
    screen.update()

    for seg in range(len(segments)-1,0,-1):
        xcord = segments[seg-1].xcor()
        ycord = segments[seg - 1].ycor()
        segments[seg].goto(xcord, ycord)
    segments[0].forward(20)
    segments[0].left(90)
screen.exitonclick()

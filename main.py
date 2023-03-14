from turtle import Turtle, Screen




screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("Black")
# t1 = Turtle(shape="square")
# t1.color("white")
# t2 = Turtle(shape="square")
# t2.color("white")
# t3 = Turtle(shape="square")
# t3.color("white")
# t2.setpos(x=t1.xcor()-20, y=0)
# t3.setpos(x=t2.xcor()-20, y=0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)





screen.exitonclick()

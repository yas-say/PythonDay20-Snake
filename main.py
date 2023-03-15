from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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
snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
score.print_score()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increment_score()

screen.exitonclick()

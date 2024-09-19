from turtle import Turtle, Screen
from snake import Snake
import time


# create a snake body
# move the snake
# control the snake
# detect collision with food
# create a scoreboard
# detect collision with wall to end
# detect collision with tail to end

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()

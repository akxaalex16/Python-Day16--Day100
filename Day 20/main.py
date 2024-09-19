from turtle import Turtle, Screen
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
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for positions in starting_positions:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(positions)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)


screen.exitonclick()

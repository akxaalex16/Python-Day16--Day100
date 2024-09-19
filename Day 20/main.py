from turtle import Turtle, Screen

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

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for positions in starting_positions:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.goto(positions)


screen.exitonclick()

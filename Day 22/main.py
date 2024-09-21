from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# create the screen
# create and move a paddle
# create another paddle
# create the ball and make it move
# detect collision with wall and bounce back
# detect collision with paddle
# detect when paddle misses
# keep score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()

    # detect when l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()


screen.exitonclick()

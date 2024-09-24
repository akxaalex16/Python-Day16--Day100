import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move_across, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    # detect collision with car
    for cars in car.all_cars:
        if cars.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect successful crossing
    if turtle.is_at_finish_line():
        turtle.go_to_start()
        car.level_up()
        scoreboard.increase_level()


screen.exitonclick()

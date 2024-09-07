from turtle import Turtle, Screen
import random

bean = Turtle()

directions = [0, 90, 180, 270]
colors = ["maroon", "floral white", "violet", "sandy brown", "pale green", "pale turquoise", "light slate gray", "gold"]
# speed = random.randint(0, 10)
# bean.speed(speed)
bean.pensize(16)
bean.speed('fastest')

for _ in range(200):
    bean.color(random.choice(colors))
    bean.forward(30)
    bean.setheading(random.choice(directions))


screen = Screen()
screen. exitonclick()

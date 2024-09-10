import turtle as t
import random

bean = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


bean.speed('fastest')


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        bean.color(random_color())
        bean.circle(100)
        bean.setheading(bean.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen. exitonclick()

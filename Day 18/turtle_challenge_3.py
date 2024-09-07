from turtle import Turtle, Screen
import random

bean = Turtle()
bean.shape('turtle')
bean.color('pink')

# one solution
# draw a triangle
for _ in range(3):
    bean.forward(100)
    bean.right(120)

# draw a square
for _ in range(4):
    bean.forward(100)
    bean.right(90)

# draw a pentagon
for _ in range(5):
    bean.forward(100)
    bean.right(72)

# draw a hexagon
for _ in range(6):
    bean.forward(100)
    bean.right(60)

# draw a heptagon
for _ in range(7):
    bean.forward(100)
    bean.right(51.4)

# draw an octagon
for _ in range(8):
    bean.forward(100)
    bean.right(45)

# draw a nonagon
for _ in range(9):
    bean.forward(100)
    bean.right(40)

# draw a decagon
for _ in range(10):
    bean.forward(100)
    bean.right(36)


# preferred solution
colors = ["maroon", "floral white", "violet", "sandy brown", "pale green", "pale turquoise", "light slate gray", "gold"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        bean.forward(100)
        bean.right(angle)


for shape_side_n in range(3, 11):
    bean.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = Screen()
screen. exitonclick()

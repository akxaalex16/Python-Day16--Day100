import random
import turtle as t

# you cant change the values of tuples
# immutable
# but if you decide that you do want to change certain items then you can turn it into a list
# list(my_tuple)

# creating tuples
my_tuple = (1, 3, 8)

# to access the items inside the tuple: add square brackets with the index value inside it.
print(my_tuple[0])

bean = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


directions = [0, 90, 180, 270]
bean.pensize(16)
bean.speed('fastest')

for _ in range(200):
    bean.color(random_color())
    bean.forward(30)
    bean.setheading(random.choice(directions))

screen = t.Screen()
screen. exitonclick()

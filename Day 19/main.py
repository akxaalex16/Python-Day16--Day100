from turtle import Turtle, Screen


bean = Turtle()
screen = Screen()


# etch-a-sketch
def move_forwards():
    bean.forward(10)


def move_backwards():
    bean.backward(10)


def move_cc():
    # bean.left(10)
    new_heading = bean.heading() + 10
    bean.setheading(new_heading)


def move_c():
    # bean.right(10)
    new_heading = bean.heading() - 10
    bean.setheading(new_heading)


def clear():
    bean.clear()
    bean.penup()
    bean.home()
    bean.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key='a', fun=move_cc)
screen.onkey(key='d', fun=move_c)
screen.onkey(key='c', fun=clear)
screen.exitonclick()


# Functions as Inputs
# def function_a(something):
    # do this with something
    # then do this
    # finally do this

# def function_b():
    # do this

# function_a(function_b)

# example
# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# def calculator(n1, n2, func):
#     return func(n1, n2)
#
#
# result = calculator(16, 3, add)
# print(result)


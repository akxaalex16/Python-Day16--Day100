from turtle import Turtle, Screen

beanie_the_turtle = Turtle()
beanie_the_turtle.shape('turtle')
beanie_the_turtle.color('red')

# easy way of creating a square
# beanie_the_turtle.forward(100)
# beanie_the_turtle.right(90)
# beanie_the_turtle.forward(100)
# beanie_the_turtle.right(90)
# beanie_the_turtle.forward(100)
# beanie_the_turtle.right(90)
# beanie_the_turtle.forward(100)
# beanie_the_turtle.right(90)

# preferred way of creating a square
for _ in range(4):
    beanie_the_turtle.forward(100)
    beanie_the_turtle.right(90)

screen = Screen()
screen.exitonclick()

# if you did this to import: import turtle
# then you have to do this to create a new turtle: beanie_the_turtle = turtle.Turtle()

# from turtle import Turtle
# keyword Module_name keyword Thing_in_module
# then you can do this to create a new turtle: beanie_the_turtle = Turtle()
# use this method if you are going to use Turtle() a lot to create many objects

# from turtle import *
# keyword Module_name keyword everything
# this imports everything

# aliasing modules
# import turtle as t
# keyword Module_name keyword alias_name

# installing modules
# import heroes
# print(heroes.gen())

# object-oriented programming
# object = Class
# car = CarBlueprint()
# the car object has attributes, example speed = 0 fuel = 50
# accessing attributes of an object, example car.speed
# the car does methods, functions, example def move():
#                                               speed = 60
#                                           def stop():
#                                               speed = 0
# accessing methods of an object, example car.stop()

import another_module
from turtle import Turtle, Screen
from prettytable import PrettyTable

# import turtle
# bean = turtle.Turtle()

print(another_module.another_variable)

bean = Turtle()
print(bean)
bean.shape('turtle')
bean.color('plum1')
bean.forward(100)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Type", ['Electric', 'Water', 'Fire'])
print(table)
# change object attributes
table.align = 'l'
print(table)

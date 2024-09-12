# import colorgram
import random
import turtle as t
from turtle import Screen

# # how to get color in rgb tuple
# colors = colorgram.extract('hirst-image.jpeg', 20)
#
# rgb_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_list.append(new_color)
#
# print(rgb_list)

bean = t.Turtle()
t.colormode(255)
bean.speed('fastest')
color_list = [(203, 34, 66), (71, 116, 151), (228, 161, 193), (150, 184, 70), (151, 160, 164), (242, 235, 46), (37, 161, 80), (35, 31, 32), (137, 205, 187), (240, 99, 54), (75, 65, 40), (33, 162, 165), (240, 246, 249), (221, 49, 65), (142, 210, 191), (145, 69, 64), (38, 155, 73)]


# # My solution
# def drawing_line_of_dots():
#     for _ in range(10):
#         bean.dot(20, random.choice(color_list))
#         bean.penup()
#         bean.forward(50)
#
#
# drawing_line_of_dots()
# bean.home()
#
# bean.goto(0, 50)
# drawing_line_of_dots()
# bean.goto(0, 100)
# drawing_line_of_dots()
# bean.goto(0, 150)
# drawing_line_of_dots()
# bean.goto(0, 200)
# drawing_line_of_dots()
# bean.goto(0, 250)
# drawing_line_of_dots()
# bean.goto(0, 300)
# drawing_line_of_dots()
# bean.goto(0, 350)
# drawing_line_of_dots()
# bean.goto(0, 400)
# drawing_line_of_dots()
# bean.goto(0, 450)
# drawing_line_of_dots()

# #another solution
bean.penup()
bean.hideturtle()
bean.setheading(225)
bean.forward(300)
bean.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    bean.dot(20, random.choice(color_list))
    bean.forward(50)

    if dot_count % 10 == 0:
        bean.setheading(90)
        bean.forward(50)
        bean.setheading(180)
        bean.forward(500)
        bean.setheading(0)

screen = Screen()
screen. exitonclick()
from turtle import Turtle, Screen


bean = Turtle()
bean.shape('turtle')
bean.color('pink')

# one solution
# for _ in range(15):
#     bean.forward(10)
#     bean.color('white')
#     bean.forward(10)
#     bean.color('black')

# another solution
for _ in range(15):
    bean.forward(10)
    bean.penup()
    bean.forward(10)
    bean.pendown()

screen = Screen()
screen. exitonclick()
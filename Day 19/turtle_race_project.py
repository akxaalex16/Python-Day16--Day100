from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = []


for turtle_index in range(0, 6):
    bean = Turtle(shape='turtle')
    bean.color('blue')
    bean.penup()
    bean.goto(-200, -150)


baby = Turtle(shape='turtle')
baby.color('pink')
baby.penup()
baby.goto(-200, -100)
jovi = Turtle(shape='turtle')
jovi.color('grey')
jovi.penup()
jovi.goto(-200, 100)
beanie = Turtle(shape='turtle')
beanie.color('purple')
beanie.penup()
beanie.goto(-200, 150)


screen.exitonclick()

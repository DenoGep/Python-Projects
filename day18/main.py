from turtle import Turtle, Screen

screen = Screen()
screen.exitonclick()

timmy = Turtle
timmy.shape("turtle")
timmy.color("DarkOliveGreen1")

for n in range(50):
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()

"""
for n in range(4):
    tim.forward(100)
    tim.right(90)
"""
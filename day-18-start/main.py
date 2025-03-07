import turtle as t
from turtle import Screen
import random


pati = t.Turtle()
pati.shape("turtle")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spirograph(circle_count):
    pati.speed("fastest")
    for n in range(circle_count):
        heading = (360 / circle_count) * n
        pati.setheading(heading)
        pati.color(random_color())
        pati.circle(50)


# Random Heading
def random_heading():
    angle = [0, 90, 180, 270]
    pati.pensize(12)
    pati.speed(9)

    for n in range(200):
        pati.setheading(random.choice(angle))
        pati.color(random_color())
        pati.forward(30)


# Dashed Lines
def dashed_lines():
    for n in range(15):
        pati.forward(10)
        pati.penup()
        pati.forward(10)
        pati.pendown()


# Shapes
def draw_shapes():
    pati.teleport(-50, 70)
    for side in range(3, 11):
        angle = int(360 / side)
        pati.color(random_color())
        for n in range(side):
            pati.forward(100)
            pati.right(angle)


screen = Screen()
screen.exitonclick()

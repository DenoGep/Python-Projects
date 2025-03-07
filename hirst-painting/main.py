"""
import colorgram

colors = colorgram.extract('image.jpg', 45)

rgb_colors = []
for item in colors:
    r = item.rgb.r
    g = item.rgb.g
    b = item.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
"""

color_list = [(1, 9, 30), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21),
 (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28),
 (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164),
 (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165), (70, 70, 45), (185, 190, 201),
 (126, 225, 231), (88, 49, 45), (61, 65, 66)]


import turtle as t
from turtle import Screen
import random


pati = t.Turtle()
pati.shape("turtle")
t.colormode(255)

pati.teleport(-250, -300)
pati.speed("fastest")


def random_color():
    return random.choice(color_list)


pati_x = -230
pati_y = -270
for row in range(10):
    pati_y += 50
    pati.teleport(pati_x, pati_y)
    for column in range(10):
        pati.dot(20, random_color())
        pati.penup()
        pati.forward(50)


screen = Screen()
screen.exitonclick()
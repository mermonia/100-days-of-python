from turtle import Turtle, Screen
from random import randint

# import colorgram
#
# color_raw_list = colorgram.extract('painting.jpg', 20)
#
# color_list = []
# for color_raw in color_raw_list:
#     rgb_color = (color_raw.rgb.r, color_raw.rgb.g, color_raw.rgb.b)
#     color_list.append(rgb_color)

color_list = [(236, 35, 108), (221, 231, 238), (145, 28, 66), (239, 75, 36), (7, 148, 95), (222, 170, 45),
              (183, 158, 47), (44, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 92),
              (244, 219, 53), (178, 40, 98), (40, 168, 117), (208, 131, 165), (205, 56, 35)]

myTurtle = Turtle()
myScreen = Screen()

myTurtle.speed("fastest")
myScreen.colormode(255)
myTurtle.penup()
myTurtle.hideturtle()


def draw_filled_circle(x, y):
    myTurtle.setpos(x * 70 - 350, y * 70 - 350)
    color = color_list[randint(0, len(color_list) - 1)]
    myTurtle.dot(30, color)


for i in range(10):
    for j in range(10):
        draw_filled_circle(j, i)

myScreen.exitonclick()
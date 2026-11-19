# import colorgram
#
# colors = colorgram.extract('img.png', 30)
#
# color_rgb = []
# for color in colors:
#     color_rgb.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(color_rgb)

import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(250, 244, 248), (240, 245, 250), (234, 225, 84), (195, 8, 69), (231, 54, 132), (197, 77, 17), (113, 177, 213), (194, 164, 14), (216, 162, 102), (29, 104, 167), (34, 187, 113), (14, 24, 64), (20, 29, 169), (231, 224, 7), (215, 134, 177), (201, 32, 132), (14, 182, 210), (231, 167, 197), (127, 188, 161), (10, 48, 28), (54, 20, 10), (40, 132, 75), (140, 218, 203), (108, 92, 210), (235, 64, 34), (131, 217, 231), (183, 17, 8), (11, 96, 53)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

def draw_dots(no_of_dots):
    for dots in range(1, no_of_dots+1):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

        if dots % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)

draw_dots(100)
screen.exitonclick()
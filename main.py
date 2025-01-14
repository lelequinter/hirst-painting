from turtle import Turtle, Screen
from random import choice
# import colorgram
# # list of tuples with color rgb
#
# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors = []
#
# for color in colors:
#     r, g, b = color.rgb
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

tim = Turtle()
screen = Screen()
screen.colormode(255)

color_list = [(133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209)]

for y in range(0, 700, 70):
    for x in range(0, 700, 70):
        pos = (x, y)
        tim.teleport(x - 350, y - 350)
        tim.dot(20, choice(color_list))

screen.exitonclick()

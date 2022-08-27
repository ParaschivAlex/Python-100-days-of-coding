import turtle as trt
import colorgram
import random
from turtle import Screen

colors = colorgram.extract('dots.jpg', 25)
# print(colors)

# rgb_colors = []
# for color in colors:
#     rgb_colors.append(color.rgb)
# # print(rgb_colors)

rgb_color = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_color.append(new_color)
# print(rgb_color)

t = trt.Turtle()
t.shape("circle")
trt.colormode(255)
t.speed("fastest")
for i in range(10):
    for j in range(10):
        t.pu()
        t.setposition(j * 50 - 225, i * 50 - 200)
        t.color(random.choice(rgb_color))
        t.pd()
        t.stamp()

screen = Screen()
screen.exitonclick()

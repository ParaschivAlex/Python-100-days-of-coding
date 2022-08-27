import turtle as trt
from turtle import Screen
import random

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'black', 'purple', 'pink', 'brown']
angle = [0, 90, 180, 270]
t = trt.Turtle()
t.shape("turtle")
t.color("green")
trt.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# Challenge 1 - Draw a Square
# timmy_the_turtle = trt.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("green")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)


# Challenge 2 - Draw a Dashed Line
# t = trt.Turtle()
# t.shape("turtle")
# t.color("green")
# for i in range(100):
#     t.pd()
#     t.forward(2)
#     t.pu()
#     t.forward(2)


# Challenge 3 - Drawing Different Shapes
# t = trt.Turtle()
# t.shape("turtle")
# t.color("green")
# k = 3
# for i in range(3, 10):
#     for j in range(k, 0, -1):
#         t.forward(100)
#         t.right(360 // i)
#     k += 1
#     t.color(random.choice(colors))


# Challenge 4 - Generate a Random Walk
# t = trt.Turtle()
# t.shape("turtle")
# t.color("green")
# t.speed("fastest")
# for i in range(1000):
#     t.forward(25)
#     t.left(random.choice(angle))
#     t.color(random.choice(colors))


# Challenge 5 - Draw a Spirograph
# t = trt.Turtle()
# t.shape("turtle")
# t.color("green")
t.speed("fastest")
for i in range(250):
    t.color(random_color())
    t.circle(100)
    # t.left(1)
    t.setheading(t.heading() + 5)

screen = Screen()
screen.exitonclick()

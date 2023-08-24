import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
turtle.colormode(255)


# colours = ["lime green", "dark orange", "green yellow"   , "gold", "dark violet", "red"]
def color_mode():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

directions = [0, 90, 180, 270]

t.pensize(10)

for _ in range(200):

    t.forward(30)
    t.color(color_mode())
    t.setheading(random.choice(directions))

    t.speed("fastest")

screen = Screen()
screen.exitonclick()

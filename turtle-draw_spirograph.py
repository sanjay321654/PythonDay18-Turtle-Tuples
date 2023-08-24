
import turtle
from turtle import Turtle, Screen
import random

jim = Turtle()
turtle.colormode(255)

def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)

    return random_color

jim.speed(90)

def draw_spirograph(size_of_gap):

    for i in range(int(360/size_of_gap)):
        jim.circle(100)
        current_heading = jim.heading()
        jim.color(color())
        jim.setheading(current_heading + size_of_gap)
draw_spirograph(5)

screen = Screen()
screen.exitonclick()
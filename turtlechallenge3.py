from turtle import Turtle, Screen
import random
jim = Turtle()

colours = ["royal blue", "pale green", "spring green",
           "blue", "yellow", "green", "red", "orange", "black", "pink"]
def sides(sides):
    angle = 360 / no_of_sides
    for _ in range(no_of_sides):
        jim.forward(100)
        jim.right(angle)


for no_of_sides in range(3, 11):
    jim.color(random.choice(colours))
    sides(no_of_sides)

screen = Screen()
screen.exitonclick()

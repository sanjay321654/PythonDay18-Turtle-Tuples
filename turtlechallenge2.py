from turtle import Turtle, Screen

sanjay = Turtle()
for _ in range(15):
    sanjay.forward(10)
    sanjay.penup()
    sanjay.forward(10)
    sanjay.pendown()

screen = Screen()
screen.exitonclick()

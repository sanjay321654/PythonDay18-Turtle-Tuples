from turtle import Turtle, Screen

jimmy = Turtle()
jimmy.shape("turtle")


# jimmy.forward(100)
# jimmy.right(90)
# jimmy.forward(100)
# jimmy.right(90)
# jimmy.forward(100)
# jimmy.right(90)
# jimmy.forward(100)

for _ in range(4):
    jimmy.forward(100)
    jimmy.right(90)



screen = Screen()
screen.exitonclick()
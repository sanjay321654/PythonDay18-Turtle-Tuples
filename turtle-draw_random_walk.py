from turtle import Turtle
import random
t = Turtle()

colours = ["lime green", "dark orange", "green yellow"   , "gold", "dark violet", "red"]

directions = [0, 90, 180, 270]

for _ in range(200):
    t.pensize(8)
    t.forward(30)
    t.color(random.choice(colours))
    t.setheading(random.choice(directions))

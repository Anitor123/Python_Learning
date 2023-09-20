import turtle as t
import random

zomp = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color





directions = [0, 90, 180, 270]
zomp.pensize(15)
zomp.speed("slow")

for _ in range(200):
    zomp.color(random_color())
    zomp.forward(30)
    zomp.setheading(random.choice(directions))













screen = t.Screen()
screen.exitonclick()
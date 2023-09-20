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


zomp.speed("fastest")

def draw_spirogragh(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        zomp.color(random_color())
        zomp.circle(100)
        zomp.setheading(zomp.heading() + size_of_gap)



draw_spirogragh(5)



screen = t.Screen()
screen.exitonclick()
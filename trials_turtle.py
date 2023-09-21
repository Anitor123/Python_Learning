import turtle as t 
import random

zomp = t.Turtle()
zomp.speed("fastest")
directions = [0, 90, 180, 270]
zomp.pensize(2)
        
color_list = ["black","blue","cyan","green","yellow","orange","purple","maroon","lime","gray"]



for _ in range(100):
    zomp.color(random.choice(color_list))
    zomp.forward(30)
    zomp.circle(100)
    zomp.setheading(random.choice(directions))
    






screen = t.Screen()
screen.exitonclick()    
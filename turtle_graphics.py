from turtle import Turtle, Screen


def draw_square():
    for turn in range(4):
        timmy.forward(100)
        timmy.right(90)
        


def draw_dashed_lines():
    for move in range(15):    
        timmy.forward(10)
        timmy.up()
        timmy.forward(10)
        timmy.down()    





#from turtle import * - this imports everthing in the module
# import turtle as t 

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
#draw_square()
draw_dashed_lines()



















screen = Screen()
screen.exitonclick()
import turtle
from prettytable import PrettyTable

def make_triangle():
    zomp.forward(100)
    zomp.left(120)
    zomp.forward(100)


zomp = turtle.Turtle()
print(zomp)
zomp.shape("turtle")
zomp.color("blue2")
make_triangle()
zomp.home()
zomp.pos()
turtle.clearscreen()

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        zomp.color(c)
        zomp.forward(steps)
        zomp.right(30)

my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

table = PrettyTable()
print(table)
import turtle


zomp = turtle.Turtle()
print(zomp)
zomp.shape("turtle")
zomp.color("blue2")
zomp.forward(100)
zomp.left(120)
zomp.forward(100)
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
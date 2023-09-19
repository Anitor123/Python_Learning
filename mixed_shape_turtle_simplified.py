from turtle import Turtle, Screen

zomp = Turtle()



n = 3
angle = 360
list_color_no = 0
list_color = ["black","blue","cyan","green","yellow","orange","purple","maroon","lime","gray"]
while not n == 11:
    zomp.shape("classic")
    zomp.color(list_color[list_color_no])
    for tri in range(n):
        zomp.right(angle/n)
        zomp.forward(100)
    n += 1
    list_color_no += 1



screen = Screen()
screen.exitonclick()    
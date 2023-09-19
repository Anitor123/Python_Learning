from turtle import Turtle, Screen

zomp = Turtle()



shape_no = 3
angle = 360
list_color_no = 0
list_color = ["black","blue","cyan","green","yellow","orange","purple","maroon","lime","gray"]
while not shape_no == 11:
    zomp.shape("classic")
    zomp.color(list_color[list_color_no])
    for tri in range(shape_no):
        zomp.right(angle/shape_no)
        zomp.forward(100)
    shape_no += 1
    list_color_no += 1



screen = Screen()
screen.exitonclick()    
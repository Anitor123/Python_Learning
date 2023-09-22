from turtle import Turtle, Screen

zomp = Turtle()
screen = Screen()


def move_forwards():
    zomp.forward(30)

def move_backward():
    zomp.backward(30)

def move_clockwise():
    zomp.right(10)  
    # Or new_heading = zomp.heading() - 10
    # zomp.setheading(new_heading)  

def move_anticlockwise():
    zomp.left(10)
    # Or new_heading = zomp.heading() + 10
    # zomp.setheading(new_heading)    

def clear():
    zomp.clear()
    zomp.penup()
    zomp.home()
    zomp.pendown()    

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(move_backward, "s")
screen.onkey(move_clockwise, "a")
screen.onkey(move_anticlockwise,"d")
screen.onkey(clear, "c")
screen.exitonclick()
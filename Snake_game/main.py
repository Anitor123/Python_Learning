from turtle import Turtle, Screen

screen = Screen()
screen.setup(width= 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
starting_positions = [(0,0), (-20,0), (-40,0)]
segments = []

for positons in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(positons)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(20)









screen.exitonclick()
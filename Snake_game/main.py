from turtle import Turtle, Screen
from snake import Snake 
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width= 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(snake.snake_speed)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 13.5:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    # Detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        scoreboard.game_over()


    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 12:
            game_is_on = False
            scoreboard.game_over()
        
        
        



screen.exitonclick()
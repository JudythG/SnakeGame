from turtle import Screen

import food
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

SLEEP_TIME = 0.5

screen = Screen()
screen.screensize(canvwidth=600, canvheight=600, bg="black")
screen.title("Snake Game")
screen.listen()
screen.tracer(0)

snake = Snake()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

food = Food()
scoreboard = Scoreboard()
scoreboard.display()

game_is_on = True
while game_is_on:
    time.sleep(SLEEP_TIME)
    screen.update()
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increment_score()

    # Detect collision with wall
    x_coord = snake.head.xcor()
    y_coord = snake.head.ycor()
    if x_coord > 280 or x_coord < -280 or y_coord > 280 or y_coord < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()


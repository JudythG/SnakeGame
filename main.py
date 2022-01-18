from turtle import Screen
from snake import Snake
import time

SLEEP_TIME = 0.1

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

game_is_on = True
while game_is_on:
    time.sleep(SLEEP_TIME)
    screen.update()
    snake.move()

screen.exitonclick()


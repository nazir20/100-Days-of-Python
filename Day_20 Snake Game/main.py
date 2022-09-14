from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# ********* step_1: screen setup & creating the snake body *********
# -screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game Python')
screen.tracer(0)

# *****************************
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
# ************** step_3: control the snake with a key press

screen.listen()
screen.onkey(key='Up', fun=snake.Up)
screen.onkey(key='Down', fun=snake.Down)
screen.onkey(key='Right', fun=snake.Right)
screen.onkey(key='Left', fun=snake.Left)

# **************  step_2: move & animate the snake  *************
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # ************** step_4: detect the collision of snake and food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # ************** step_5: detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # ************** step_6: detect collision with snake's own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

######
screen.exitonclick()

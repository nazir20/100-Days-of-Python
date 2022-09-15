# -@imports
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

# *************** @screen setup *****************
screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing Game')
screen.tracer(0)
# ************* @creating an instance of player class *************
player = Player()
screen.listen()
screen.onkey(key='Up', fun=player.go_up)

# ************** @create the car behavior ************
car_manager = CarManager()
# ************* @add the scoreboard **************
scoreboard = ScoreBoard()
# ************** @run the game *************
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # *********** @detect collision with car *********
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # ************ @detect successful crossing ************
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
# ************* @end of the game ************
screen.exitonclick()

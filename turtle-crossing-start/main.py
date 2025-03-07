"""
1) Make some of the cars longer
2) Make the car speed up a little balanced (maybe increase 5 speed every level or increase 10 every 3 lvl)
"""



import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Crossing Road Game")
screen.bgcolor("thistle")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Check if level is finished
    if player.check_level_up():
        car_manager.increase_speed()
        scoreboard.increase_level()


screen.exitonclick()
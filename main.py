import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    car_manager.moving_cars()

    if player.ycor() > 280:
        scoreboard.track_level()
        player.reset_position()

    if player.distance(car_manager) < 20:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

loop = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

car = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move, key="Up")

speed = 0.1

game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    loop += 1
    car.move()

    for car.car_num in car.cars:
        if player.distance(car.car_num) < 25:
            game_is_on = False
            scoreboard.game_over()

    if loop % 6 == 0:
        # print("This is working")
        car.spawn_car()

    if player.ycor() > 280:
        player.refresh()
        scoreboard.level_up()
        # car.increase_speed()
        speed *= 0.9


screen.exitonclick()
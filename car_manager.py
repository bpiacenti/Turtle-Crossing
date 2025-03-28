from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        # self.spawn_car()

    def spawn_car(self):
        car = Turtle("square")
        car.pu()
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.goto(300, random.randint(a=-200, b=200))
        self.cars.append(car)
        # self.move()

    def move(self):
        for car_num in range(len(self.cars)):
            new_x = self.cars[car_num].xcor() - STARTING_MOVE_DISTANCE
            self.cars[car_num].goto(new_x, self.cars[car_num].ycor())

    # def increase_speed(self):
    #     global STARTING_MOVE_DISTANCE
    #     STARTING_MOVE_DISTANCE += MOVE_INCREMENT
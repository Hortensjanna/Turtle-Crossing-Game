from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(280, random.randint(-250, 250))
        self.color(random.choice(COLORS))

    def moving_cars(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())
        self.forward(STARTING_MOVE_DISTANCE)



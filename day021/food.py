from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.color('red')
        self.speed('fastest')

        self.setpos(self.get_random_position())

    @staticmethod
    def get_random_position():
        xcor = random.randint(-14, 14) * 40
        ycor = random.randint(-14, 14) * 40
        print(xcor, ycor)
        return xcor, ycor

    def move_to_random_location(self):
        self.setpos(self.get_random_position())

from turtle import Turtle

STARTING_POSITION = (0, -560)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.setpos(STARTING_POSITION)
        self.setheading(90)
        self.shape('turtle')
        self.shapesize(stretch_wid=2, stretch_len=2)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.setpos(STARTING_POSITION)

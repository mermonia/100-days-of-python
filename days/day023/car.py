from turtle import Turtle


class Car(Turtle):
    def __init__(self, color, move_speed, y):
        super().__init__()

        self.penup()
        self.color(color)
        self.move_speed = move_speed
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=3)
        self.setheading(180)
        self.setpos(600, y)

    def set_speed(self, new_speed):
        self.move_speed = new_speed

    def move(self):
        self.forward(self.move_speed)

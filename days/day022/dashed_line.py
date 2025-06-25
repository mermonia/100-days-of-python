from turtle import Turtle


class DashedLine(Turtle):

    def __init__(self):
        super().__init__()
        self.setheading(270)
        self.color("white")
        self.teleport(0, 590)
        self.width(10)

    def draw_dashed_line(self):
        while self.ycor() >= -600:
            self.forward(25)
            self.penup()
            self.forward(25)
            self.pendown()



from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=2)

        self.y_direction = 1
        self.x_direction = -1

    def move(self):
        if self.ycor() >= 560:
            self.y_direction = -1
        elif self.ycor() <= -560:
            self.y_direction = 1

        self.setpos(self.xcor() + 20 * self.x_direction, self.ycor() + 20 * self.y_direction)

    def bounce_from_paddle(self):
        if self.x_direction == 1:
            self.x_direction = -1
        else:
            self.x_direction = 1

    def reset_position(self):
        self.x_direction = -1
        self.y_direction = 1
        self.setpos(0, 0)
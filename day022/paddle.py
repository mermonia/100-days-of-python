from turtle import Turtle


class Paddle:

    def __init__(self, x):
        self.paddle_body = []
        for i in range(4):
            new_segment = Turtle()
            new_segment.penup()
            new_segment.color("white")
            new_segment.shape("square")
            new_segment.shapesize(stretch_wid=2, stretch_len=2)
            new_segment.setpos(x, -60 + 40 * i)
            self.paddle_body.append(new_segment)

        self.upper_segment = self.paddle_body[3]
        self.lower_segment = self.paddle_body[0]

    def move_up(self):
        if self.upper_segment.ycor() >= 560:
            return

        for segment in self.paddle_body:
            segment.setpos(segment.xcor(), segment.ycor() + 40)

    def move_down(self):
        if self.lower_segment.ycor() <= -560:
            return

        for segment in self.paddle_body:
            segment.setpos(segment.xcor(), segment.ycor() - 40)


from paddle import Paddle


class CpuPaddle(Paddle):

    def __init__(self, x):
        super().__init__(x)
        self.move_direction = "Up"

    def move(self):
        if self.move_direction == "Up":
            if self.upper_segment.ycor() >= 560:
                self.move_direction = "Down"
                self.move_down()
            else:
                self.move_up()
        else:
            if self.lower_segment.ycor() <= -560:
                self.move_direction = "Up"
                self.move_up()
            else:
                self.move_down()
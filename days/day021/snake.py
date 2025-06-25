import turtle

MOVE_DISTANCE = 40


class Snake:
    def __init__(self):
        self.snake = []

        for i in range(3):
            new_turtle = self.get_new_segment()
            new_turtle.setx(-40 * i)
            self.snake.append(new_turtle)

        self.head = self.snake[0]

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].setposition(self.snake[i - 1].position())

        self.snake[0].forward(MOVE_DISTANCE)

    def face_right(self):
        if self.head.heading() == 180:
            return
        self.head.setheading(0)

    def face_up(self):
        if self.head.heading() == 270:
            return
        self.head.setheading(90)

    def face_left(self):
        if self.head.heading() == 0:
            return
        self.head.setheading(180)

    def face_down(self):
        if self.head.heading() == 90:
            return
        self.head.setheading(270)

    def is_out_of_bounds(self):
        if self.head.xcor() > 620 or self.head.xcor() < -620:
            return True
        if self.head.ycor() > 620 or self.head.ycor() < -620:
            return True
        return False

    def extend_snake(self):
        new_segment = self.get_new_segment()
        new_segment.setpos(self.snake[-1].pos())
        self.snake.append(new_segment)

    @staticmethod
    def get_new_segment():
        new_segment = turtle.Turtle(shape='square')
        new_segment.color('white')
        new_segment.shapesize(stretch_wid=2, stretch_len=2)
        new_segment.penup()

        return new_segment

    def is_head_colliding_with_body(self):
        for segment in self.snake[1:-1]:
            if self.head.distance(segment) < 15:
                return True
        return False

    def get_head_position(self):
        return self.head.position()

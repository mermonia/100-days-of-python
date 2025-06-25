import turtle

MOVE_DISTANCE = 40


class Snake:
    def __init__(self):
        self.snake = []

        for i in range(3):
            new_turtle = turtle.Turtle(shape='square')

            new_turtle.color('white')
            new_turtle.penup()
            new_turtle.setx(-40 * i)
            new_turtle.shapesize(stretch_wid=2, stretch_len=2)

            self.snake.append(new_turtle)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].setposition(self.snake[i - 1].position())

        self.snake[0].forward(MOVE_DISTANCE)

    def face_right(self):
        if self.snake[0].heading() == 180:
            return
        self.snake[0].setheading(0)

    def face_up(self):
        if self.snake[0].heading() == 270:
            return
        self.snake[0].setheading(90)

    def face_left(self):
        if self.snake[0].heading() == 0:
            return
        self.snake[0].setheading(180)

    def face_down(self):
        if self.snake[0].heading() == 90:
            return
        self.snake[0].setheading(270)

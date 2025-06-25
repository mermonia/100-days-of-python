import turtle
import time
from snake import Snake


def main():
    screen = turtle.Screen()

    screen.setup(width=1180, height=1180)
    screen.bgcolor('black')
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()

    screen.update()
    screen.listen()
    screen.onkey(key="w", fun=snake.face_up)
    screen.onkey(key="a", fun=snake.face_left)
    screen.onkey(key="s", fun=snake.face_down)
    screen.onkey(key="d", fun=snake.face_right)

    while True:
        snake.move()
        time.sleep(.1)
        screen.update()


if __name__ == "__main__":
    main()

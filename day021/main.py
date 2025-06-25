import turtle
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food


def main():
    screen = turtle.Screen()

    screen.setup(width=1240, height=1240)
    screen.bgcolor('black')
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.update()
    screen.listen()
    screen.onkey(key="w", fun=snake.face_up)
    screen.onkey(key="a", fun=snake.face_left)
    screen.onkey(key="s", fun=snake.face_down)
    screen.onkey(key="d", fun=snake.face_right)

    is_game_on = True
    while is_game_on:
        snake.move()
        time.sleep(.05)

        if snake.head.distance(food) < 15:
            food.move_to_random_location()
            scoreboard.increase_score()
            snake.extend_snake()

        if snake.is_out_of_bounds() or snake.is_head_colliding_with_body():
            is_game_on = False
            scoreboard.show_game_over()
        else:
            screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    main()

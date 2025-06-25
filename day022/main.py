from turtle import Screen

import score_counter
from dashed_line import DashedLine
from paddle import Paddle
from cpu_paddle import CpuPaddle
from ball import Ball
from score_counter import ScoreCounter
import time


def main():

    def ball_has_collided_with_paddle():
        for segment in player_paddle.paddle_body:
            if ball.distance(segment) <= 40:
                return True
        for segment in computer_paddle.paddle_body:
            if ball.distance(segment) <= 40:
                return True

    def check_ball_out_of_bounds():
        if ball.xcor() >= 790:
            player_score.increase_score()
            ball.reset_position()
            screen.update()
            time.sleep(1)
        elif ball.xcor() <= -790:
            computer_score.increase_score()
            ball.reset_position()
            screen.update()
            time.sleep(1)

    screen = Screen()
    screen.setup(width=1600, height=1200)

    screen.bgcolor('black')
    screen.title("Pong Game")
    screen.tracer(0)

    center_line = DashedLine()
    center_line.draw_dashed_line()

    player_paddle = Paddle(-750)
    computer_paddle = CpuPaddle(750)

    player_score = ScoreCounter(-100, 500)
    computer_score = ScoreCounter(100, 500)

    ball = Ball()

    screen.listen()
    screen.onkeypress(key="w", fun=player_paddle.move_up)
    screen.onkeypress(key="s", fun=player_paddle.move_down)

    game_is_on = True
    while game_is_on:
        computer_paddle.move()
        ball.move()

        if ball_has_collided_with_paddle():
            ball.bounce_from_paddle()

        check_ball_out_of_bounds()

        screen.update()
        time.sleep(0.05)

    screen.exitonclick()


if __name__ == '__main__':
    main()

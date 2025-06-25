import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from car import Car
import random


def main():

    def handle_car_spawning():
        if random.random() < 0.1 * level_number.level:
            car_manager.spawn_car()

    def is_player_on_goal():
        if player.ycor() >= 550:
            return True
        return False

    def has_player_crashed():
        for car in car_manager.car_list:
            if player.distance(car) <= 40:
                return True
        return False

    screen = Screen()
    screen.setup(width=1200, height=1200)
    screen.colormode(255)
    screen.tracer(0)

    car_manager = CarManager()
    player = Player()
    level_number = Scoreboard()

    screen.listen()
    screen.onkeypress(key="Up", fun=player.move_up)

    game_is_on = True
    while game_is_on:
        handle_car_spawning()
        car_manager.move_cars()

        if is_player_on_goal():
            player.reset_position()
            level_number.increase_level()
            car_manager.increase_cars_speed()

        if has_player_crashed():
            game_is_on = False
            level_number.show_game_over()

        time.sleep(0.07)
        screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    main()

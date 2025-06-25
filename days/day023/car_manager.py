import random

from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_move_speed = STARTING_MOVE_DISTANCE

    def increase_cars_speed(self):
        self.car_move_speed += MOVE_INCREMENT
        for car in self.car_list:
            car.set_speed(self.car_move_speed)

    def spawn_car(self, color=None, y=None):
        if color is None:
            car_color = random.choice(COLORS)
        else:
            car_color = color

        if y is None:
            car_y_pos = random.randint(-12, 12) * 40
        else:
            car_y_pos = y

        # print(f"Spawning car with color {car_color} and y_pos {car_y_pos} and move speed {self.car_move_speed}")
        self.car_list.append(Car(car_color, self.car_move_speed, car_y_pos))

        if self.car_list[0].xcor() >= 620:
            self.car_list.pop(0)

    def move_cars(self):
        for car in self.car_list:
            car.move()

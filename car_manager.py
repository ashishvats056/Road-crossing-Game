from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.num = -1
        self.no = 8

    def generate_car(self):
        self.num += 1
        if self.num % self.no == 0:
            y_pos = random.randint(-230, 230)
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.left(180)
            car.color(random.choice(COLORS))
            car.goto(310, y_pos)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)

    def remove_extra(self):
        for car in self.cars:
            if car.xcor() > 320:
                self.cars.remove(car)

    def increase_car_speed(self):
        self.speed += MOVE_INCREMENT
        self.no -= 1

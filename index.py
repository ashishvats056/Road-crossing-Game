import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

if __name__ == "__main__":
    # Game setup
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    car_manager = CarManager()
    player = Player()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkeypress(fun=player.move_turtle, key="Up")

    game_on = True

    while game_on:
        time.sleep(0.1)
        screen.update()
        # generate car and move them and remove any extra car that has gone off-screen
        car_manager.generate_car()
        car_manager.move_cars()
        car_manager.remove_extra()
        # check turtle collision with car (game over)
        for car in car_manager.cars:
            if player.distance(car) < 20:
                scoreboard.game_over()
                game_on = False
        # check if turtle has crossed the finish line
        if player.level_finish():
            scoreboard.increase_level()
            car_manager.increase_car_speed()

    screen.exitonclick()

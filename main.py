import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import Cars

screen = Screen()
screen.title('Turtle crossing game')
screen.bgpic('road.png')
screen.setup(width=600, height=600)
screen.tracer(0)
screen.cv._rootwindow.resizable(False, False)

car = Cars()

player = Player()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, 'w')
screen.onkey(player.move_down, 's')

n = scoreboard.level
game_is_on = True
while game_is_on:
    time.sleep(scoreboard.difficulty)
    screen.update()
    if len(car.cars) ==50:
        m = 0
        while m != 10:
            car.cars.remove(car.cars[0])
            m += 1
    for i in range(0, len(car.cars)):
        if player.distance(car.cars[i].xcor(), car.cars[i].ycor()) <= 20:
            scoreboard.game_over()
            game_is_on = False
    if n == 10:
        car.create_car()
        n = scoreboard.level
    else:
        n += 1
    car.move_car()
    if player.ycor() == 270:
        scoreboard.increase_level()
        player.reset_turtle()


screen.exitonclick()

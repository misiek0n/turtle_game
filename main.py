import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import Cars

screen = Screen()
screen.title('Turtle crossing game')
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

scoreboard = Scoreboard()

car = Cars()

screen.listen()
screen.onkey(player.move_up, 'w')
screen.onkey(player.move_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() == 270:
        scoreboard.inrease_level()
        player.reset_turtle()



screen.exitonclick()

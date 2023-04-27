from turtle import Turtle
import random as r


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.colors = ['purple', 'blue', 'pink', 'red', 'green', 'brown']
        self.color(r.choice(self.colors))
        self.cars = []

    def create_car(self):
        new_car = Turtle()
        new_car.pu()
        new_car.setheading(180)
        new_car.shape('square')
        new_car.shapesize(1, 2)
        new_car.color(r.choice(self.colors))
        new_car.sety(r.randint(-200, 200))
        new_car.setx(310)
        new_car.speed(0.95)
        self.cars.append(new_car)

    def move_car(self):
        for i in range(0, len(self.cars)):
            self.cars[i].forward(5)

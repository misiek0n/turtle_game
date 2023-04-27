from turtle import Turtle
import random as r


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape('square')
        self.shapesize(1, 2)
        self.colors = ['purple', 'blue', 'pink', 'red', 'green', 'brown']
        self.color(r.choice(self.colors))
        self.sety(r.randint(-250, 250))
        self.setx(0)

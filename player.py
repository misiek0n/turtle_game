from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.setpos(x=0, y=-270)
        self.setheading(90)
        self.shape('turtle')

    def move_up(self):
        new_y = self.ycor() + 10
        self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - 10
        self.sety(new_y)

    def reset_turtle(self):
        self.ht()
        self.goto(x=0, y=-270)
        self.st()

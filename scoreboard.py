from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.pu()
        self.ht()
        self.level = 1
        self.difficulty = 0.1
        self.setpos(x=-240, y=260)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level {self.level}", align="center", font=('Arial', 14, 'normal'))

    def increase_level(self):
        self.level += 1
        if self.difficulty > 0.005:
            self.difficulty -= 0.005
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over.", False, align="center", font=('Arial', 14, 'normal'))

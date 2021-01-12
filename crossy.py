from turtle import Turtle


class Crossy(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(0, -330)
        self.left(90)
        self.shape("turtle")

    def move(self):
        self.restart()
        self.forward(10)

    def restart(self):
        if self.ycor() > 320:
            self.goto(0, -330)
            self.level += 1
from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.right(180)
        self.penup()
        self.goto(random.randint(-320, 320), random.randint(-320, 320))

    def restart(self):
        if self.xcor() < -400:
            self.goto(400, random.randint(-320, 320))


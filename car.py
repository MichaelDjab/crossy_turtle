from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color('#%06X' % random.randint(0, 0xFFFFFF))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.right(180)
        self.penup()
        self.goto(random.randint(-310, 1000), random.randint(-280, 300))

    def restart(self):
        if self.xcor() < -400:
            self.goto(random.randint(400, 600), random.randint(-280, 300))


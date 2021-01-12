from turtle import Turtle
FONT = ("Arial", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-300, 300)
        self.write("Level: 1", align="left", font=FONT)

    def display_level(self, level):
        self.clear()
        self.write(f"Level: {level}", align="left", font=FONT)
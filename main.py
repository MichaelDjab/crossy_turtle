from turtle import Turtle, Screen
from crossy import Crossy

# Setup screen
screen = Screen()
screen.title("Crossy-Turtle")
screen.setup(700, 700)
screen.tracer(0)
screen.listen()

# setup crossy turtle
mike = Crossy()

# Setup scoreboard


game_over = False
while not game_over:
    screen.onkeypress(mike.move, "space")
    screen.update()





screen.exitonclick()
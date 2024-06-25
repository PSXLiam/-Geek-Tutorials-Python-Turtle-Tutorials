from turtle import *

#Screen Setup
setup(800, 500)
speed(0)
bgcolor("midnight blue")

#Make Star Function
def make_star():
    color("yellow")
    begin_fill()
    for i in range(5):
        forward(5)
        left(72)
        forward(5)
        right(144)
    end_fill()

#Draw Star
make_star()

exitonclick()

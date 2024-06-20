from turtle import *

#Initialise turtle
speed(5)
bgcolor("black")
color("greenyellow")
pensize(5)

#Draw Octagon
for i in range (8):
    forward(100)
    left(45)

#Hide turtle
hideturtle()

exitonclick()

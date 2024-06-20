from turtle import *

#Initialise turtle
speed(5)
bgcolor("black")
color("greenyellow")
pensize(5)

sides = 8

for i in range(sides):
    left(360/sides)
    #Draw Octagon
    for i in range (sides):
        forward(100)
        left(360/sides)

#Hide turtle
hideturtle()

exitonclick()

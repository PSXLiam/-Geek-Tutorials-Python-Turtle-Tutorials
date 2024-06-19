from turtle import *

#Initialise turtle
speed(0)
penup()
goto(-350, 100)
pensize(5)
color("magenta")
pendown()

#Draw outlined square
for i in range(4):
    forward(150)
    left(90)

#Hide turtle
hideturtle()

exitonclick()

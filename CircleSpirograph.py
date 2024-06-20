from turtle import *

#Initialise turtle
speed(0)
bgcolor("black")
pensize(2)

#for each set of circles
for i in range(6):
    #for each colour
    for colours in ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]:
        #draw circle of current color then rotate 10° to left
        color(colours)
        circle(100)
        left(10)

#Hide turtle
hideturtle()

exitonclick()

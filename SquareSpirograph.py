from turtle import *

#Initialise turtle
speed(0)
bgcolor("black")
pensize(2)

#Define variables for code
colourRange = ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]
angle = 10
fullrotation = 0

#while the pattern has not made a full rotation
while fullrotation <= 360:
    #for each colour
    for colours in colourRange:
        #draw circle of current colour then rotate 10° to left
        color(colours)
        circle(100)
        left(10)
        fullrotation = fullrotation + angle # increase value of 'fullrotation' by angle moved

#Hide turtle
hideturtle()

exitonclick()

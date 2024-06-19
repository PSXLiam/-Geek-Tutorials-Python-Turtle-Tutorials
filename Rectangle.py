from turtle import *

#Initialise turtle
speed(0)
fillcolor("red")
begin_fill()

#Draw rectangle
for i in range(2):
    forward(300)
    right(90)
    forward(150)
    right(90)

#Fill shape then hide turtle
end_fill()
hideturtle()

exitonclick()

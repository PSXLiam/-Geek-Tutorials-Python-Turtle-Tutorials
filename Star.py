from turtle import *

#Initialise turtle
speed(0)
penup()
goto(-150, 0)
bgcolor("black")
fillcolor("yellow")
begin_fill()
pendown()

points = 1

#Draw star
while points < 5:
    forward(250)
    right(144)
    points = points + 1
end_fill()

#Fill shape then hide turtle
hideturtle()

exitonclick()

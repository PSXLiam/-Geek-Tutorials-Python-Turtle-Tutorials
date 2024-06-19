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
while points <= 5:
    left(72)
    forward(50)
    right(144)
    forward(50)
    points = points + 1
end_fill()

#Hide turtle
hideturtle()

exitonclick()

from turtle import *

#Initialise turtle
speed(0)
bgcolor("blue")
penup()
goto(-150, -150)
fillcolor("yellow")
begin_fill()
pendown()

#Draw triangle
for i in range(3):
    forward(300)
    left(120)

#Fill shape then hide turtle
end_fill()
hideturtle()

exitonclick()

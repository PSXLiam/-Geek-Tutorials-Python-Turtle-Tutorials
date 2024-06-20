from turtle import *

#Initialise turtle
speed(0)
bgcolor("gold")

#Black Circle
penup()
goto(0, -225)
pendown()
color("black")
begin_fill()
circle(225)
end_fill()

#Hide turtle
hideturtle()

exitonclick()

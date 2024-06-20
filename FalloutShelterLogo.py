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

#Triangle part
penup()
goto(0, 0)
pendown()
color("gold")
begin_fill()
for i in range(3):
    left(120)
    for i in range(3):
        forward(200)
        left(120)
end_fill()

#Hide turtle
hideturtle()

exitonclick()

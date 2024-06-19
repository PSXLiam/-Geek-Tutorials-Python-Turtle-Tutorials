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

#move to next area
penup()
goto (-175, 100)
pendown()

#Draw outlined multicolour square
for i in ["yellow", "red", "blue", "purple"]:
    color(i)
    forward(150)
    left(90)

#move to next area
penup()
goto (0, 100)
pendown()

#Draw filled square
color("orange", "yellow")
begin_fill()
for i in range(4):
    forward(150)
    left(90)
end_fill()

#Hide turtle
hideturtle()

exitonclick()

from turtle import *

#Initialise turtle
speed(0)
penup()
goto(0, -100)
bgcolor("yellow")
color("magenta", "cyan")
pensize(10)
begin_fill()
pendown()

#Draw circle
circle(120)

#Fill shape then hide turtle
end_fill()
hideturtle()

exitonclick()

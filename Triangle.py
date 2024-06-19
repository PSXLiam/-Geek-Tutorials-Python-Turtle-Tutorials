from turtle import *

#Initialise turtle
speed(1)
bgcolor("blue")
penup()
goto(-150, -150)
fillcolor("yellow")
begin_fill()
pendown()

#Draw triangle
forward(300)
left(120)
forward(300)
left(120)
forward(300)
left(120)

#Fill shape then hide turtle
end_fill()
hideturtle()

done()

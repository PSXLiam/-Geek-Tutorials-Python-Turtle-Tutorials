from turtle import *
from random import *

#Screen Setup
setup(800, 500)
title("Turtle Race")
bgcolor("forestgreen")
speed(0)

#Heading
penup()
goto(-100, 205)
color("white")
write("TURTLE RACE", font=("Arial", 20, "bold"))

#Dirt Track
goto(-350, 200)
pendown()
color("chocolate")
begin_fill()
for i in range(2):
    forward(700)
    right(90)
    forward(400)
    right(90)
end_fill()

#Finish Line
gap_size = 20
shape("square")
penup()

#White Squares Row 1
color("white")
for i in range(10):
    goto(250, (170 - (i * gap_size * 2)))
    stamp()

#Black Squares Row 1
color("black")
for i in range(10):
    goto(250, (210 - gap_size) - (i * gap_size * 2))
    stamp()

#White Squares Row 2
color("white")
for i in range(10):
    goto(250 + gap_size, (210 - gap_size) - (i * gap_size * 2))
    stamp()

#Black Squares Row 2
color("black")
for i in range(10):
    goto(250 + gap_size, (170 - (i * gap_size * 2)))
    stamp()

#Initialize race turtle
def race_turtle(turtle_colour, turtle_ycor):
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-300, turtle_ycor)
    turtle.backward(125)
    turtle.showturtle()
    turtle.speed(1)
    turtle.color(turtle_colour)
    turtle.shape("turtle")
    turtle.shapesize(1.5)
    turtle.goto(-300, turtle_ycor)
    turtle.pendown()

#Turtle 1 - Blue
blue_turtle = race_turtle("cyan", 150)

exitonclick()

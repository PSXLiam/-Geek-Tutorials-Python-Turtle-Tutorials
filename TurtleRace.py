from turtle import *
from random import *
import time

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
    return turtle

#Turtle 1 - Blue
blue_turtle = race_turtle("cyan", 150)

#Turtle 2 - Pink
pink_turtle = race_turtle("magenta", 50)

#Turtle 3 - Yellow
yellow_turtle = race_turtle("yellow", -50)

#Turtle 4 - Green
green_turtle = race_turtle("lime", -150)

#Pause 1 second before race
time.sleep(1)

#Move the turtles
while blue_turtle.xcor() <= 230 and pink_turtle.xcor() <= 230 and yellow_turtle.xcor() <= 230 and green_turtle.xcor() <= 230:
    blue_turtle.forward(randint(1, 10))
    pink_turtle.forward(randint(1, 10))
    yellow_turtle.forward(randint(1, 10))
    green_turtle.forward(randint(1, 10))

#Find winner
if blue_turtle.xcor() >= 230:
    print("Blue Wins!")
elif pink_turtle.xcor() >= 230:
    print("Pink Wins!")
elif yellow_turtle.xcor() >= 230:
    print("Yellow Wins!")
else:
    print("Green Wins!")

exitonclick()

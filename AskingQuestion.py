from turtle import *

#Ask user for favorite colour
favoriteColour = input ("What is your favorite colour?: ")
color(favoriteColour)

#Initialise turtle
speed(0)

#Draw box thta is favorite colour
begin_fill()
for i in range (4):
    forward(200)
    right(90)
end_fill()

#Hide turtle
hideturtle()

exitonclick()

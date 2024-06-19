from turtle import *

#Intialise turtle
pensize(5)
color("green")

penup()
goto(-250, 100)

#The Letter 'L'
pendown()
right(90)
forward(200)
left(90)
forward(140)

#Move to next letter
penup()
forward(20)

#The letter 'I'
pendown()
left(90)
forward(200)

#Move to next letter
penup()
back(200)
right(90)
forward(20)

#The letter 'A'
pendown()
left(75)
forward(210)
right(155)
forward(210)
back(105)
right(100)
forward(46)

#Move to next letter
penup()
back (46)
left(100)
forward(105)
left(80)
forward(20)

#The letter 'M'
pendown()
left(90)
forward(200)
right(150)
forward(150)
left(120)
forward(150)
right(150)
forward(200)

done()

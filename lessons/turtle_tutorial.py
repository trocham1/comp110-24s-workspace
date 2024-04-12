from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

#  Enable RGB mode.
colormode(255)

#  Using while statements for square.
"""i: int = 0
while(i < 4):
    leo.forward(300)
    leo.left(90)
    i += 1"""

#  Pen color, changing the color.
"""leo.color(255, 51, 243)"""


#  Position the trianlge in a different spot.
leo.penup()
leo.goto(-150, -120)
leo.pendown()

#  Other useful color commands.
leo.pencolor("pink") #  Only pen color
leo.fillcolor(32, 67, 93) #  Only fill color
"""leo.color("green", "yellow")""" #  Set fill and pen color.

#  Speed, Visbility.
leo.speed(3) #  determine the speed of the drawing.
leo.hideturtle()  # this hide the turtle.


#  Fill color.
"""leo.begin_fill()
leo.end_fill()"""
leo.begin_fill()

#  This is for a triangle.
i: int = 0
while(i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1

leo.end_fill()

# Bob
bob: Turtle = Turtle()
bob.penup()
bob.goto(-150, -120)
bob.pendown()
bob.pencolor(255, 255, 50)
bob.speed(5)

side_length: int = 300
side_length = side_length * 0.97
 
i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(123)
    i = i + 1



done()
"""Townhouses in copenhagen."""


__author__ = "730711485"

from turtle import Turtle, colormode, done, tracer, update
colormode(255)


def main() -> None:
    """The entry point of my scence."""
    tracer(0, 0)
    bridge: Turtle = Turtle()
    #  First house.
    draw_rectanlge(bridge, -250, 100, 100, 125)
    draw_rooft(bridge, -250, 100, 100)
    draw_window(bridge, -230, 75, 20)
    draw_window(bridge, -190, 75, 20)
    draw_window(bridge, -230, 30, 20)
    draw_door(bridge, -190, -25, 20, 40)
    #  Second house.
    draw_rectanlge(bridge, -150, 100, 100, 125)
    draw_rooft(bridge, -150, 100, 100)
    draw_window(bridge, -130, 75, 20)
    draw_window(bridge, -90, 75, 20)
    draw_window(bridge, -130, 30, 20)
    draw_door(bridge, -90, -25, 20, 40)
    #  Third house.
    draw_rectanlge(bridge, -50, 100, 100, 125)
    draw_rooft(bridge, -50, 100, 100)
    draw_window(bridge, -30, 75, 20)
    draw_window(bridge, 10, 75, 20)
    draw_window(bridge, -30, 30, 20)
    draw_door(bridge, 10, -25, 20, 40)
    #  Fourth house.
    draw_rectanlge(bridge, 50, 100, 100, 125)
    draw_rooft(bridge, 50, 100, 100)
    draw_window(bridge, 70, 75, 20)
    draw_window(bridge, 110, 75, 20)
    draw_window(bridge, 70, 30, 20)
    draw_door(bridge, 110, -25, 20, 40)
    #  fifth house.
    draw_rectanlge(bridge, 150, 100, 100, 125)
    draw_rooft(bridge, 150, 100, 100)
    draw_window(bridge, 170, 75, 20)
    draw_window(bridge, 210, 75, 20)
    draw_window(bridge, 170, 30, 20)
    draw_door(bridge, 210, -25, 20, 40)
    #  Road.
    draw_road(bridge, 325, -26, 650, 100)

    update()
    done()


def draw_window(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a winow for the house."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.pencolor("black")
    a_turtle.begin_fill()
    a_turtle.fillcolor(34, 5, 5)
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1
    a_turtle.end_fill()


def draw_road(a_turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draw a line that is a path."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.pencolor("black")
    a_turtle.begin_fill()
    a_turtle.fillcolor(133, 117, 117)
    a_turtle.right(90)
    a_turtle.forward(height)
    a_turtle.right(90)
    a_turtle.forward(width)
    a_turtle.right(90)
    a_turtle.forward(height)
    a_turtle.right(90)
    a_turtle.end_fill()


def draw_rectanlge(a_turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draw a the houses."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.pencolor("black")
    a_turtle.fillcolor(165, 64, 64)
    a_turtle.begin_fill()
    a_turtle.forward(width)
    a_turtle.right(90)
    a_turtle.forward(height)
    a_turtle.right(90)
    a_turtle.forward(width)
    a_turtle.right(90)
    a_turtle.forward(height)
    a_turtle.right(90)
    a_turtle.end_fill()


def draw_rooft(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw the rooftop of houses."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.pencolor("black")
    a_turtle.fillcolor(68, 6, 6)
    a_turtle.begin_fill()
    i: int = 0
    while i < 3:
        a_turtle.forward(width)
        a_turtle.left(120)
        i = i + 1
    a_turtle.end_fill()


def draw_door(a_turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """This draw door for the houses."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.pencolor("black")
    a_turtle.fillcolor(70, 25, 25)
    a_turtle.begin_fill()
    a_turtle.forward(width)
    a_turtle.left(90)
    a_turtle.forward(height)
    a_turtle.left(90)
    a_turtle.forward(width)
    a_turtle.left(90)
    a_turtle.forward(height)
    a_turtle.left(90)
    a_turtle.end_fill()


if __name__ == "__main__":
    main()
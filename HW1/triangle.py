"""
Youssef Naguib - HW01 - This program creates a star shape by drawing triangles.
"""


import turtle


def init():
    """
    This function rotates the turtle's initial direction and makes sure the turtle will draw a trail behind itself
    """
    turtle.left(35)
    turtle.down()


def draw_triangle():
    """
    This function tells the turtle to draw a triangle with three equal side lengths of 100
    """
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
    turtle.up()
    turtle.forward(100)
    turtle.left(72)
    turtle.down()


init()
draw_triangle()
draw_triangle()
draw_triangle()
draw_triangle()
draw_triangle()
turtle.done()




'''
Youssef Naguib Lab 01 (tetris)
-this code draws an empty tetris board and proceeds to draw multiple instancesof 4 different tetris shapes.
Each shape is drawn atleast twice.
The docstrings under each function describe the order in which the shapes are drawn, assuming the turtle's starting
orientation is north. The shape will be drawn differently depending on the turtle's starting
orientation. (For example if the turtle starts facing south, the shape will be drawn upside down)
'''

import turtle
'''
Imports turtle library
'''

def DrawBoard():
    '''
    This function draws an empty 400x200 long rectangular tetris board
    Pre: Turtle is facing east, and in exact middle of canvas
    Post:Turle is facing north, and at the middle right border of the tetris board.
    '''
    turtle.up()
    turtle.forward(100)
    turtle.left(90)
    turtle.down()
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)

def Init():
    '''
    This function moves the turtle from the middle right section of the board, facing north, to the bottom left corner
    of the board, facing north, without drawing over the already visible lines.
    Pre: turtle is facing north and is at middle of the right border of the tetris board.
    Post: turtle is at the bottom left corner of the tetris board and faces north.
    '''
    turtle.up()
    turtle.right(180)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.down()

def ColorBlock():
    '''
    This function draws a 20x20 square, and contains a turtle.begin_fill and turtle.end_fill that allows the square to
    be filled in with a color. The color is determined by turtle.fillcolor, a command implemented in the
    different shapes.
    Pre: turtle starts at bottom left corner of the square and faces the top left corner of the square. The left side
    of the square will always be drawn first, followed by the top side, right side, and bottom side. This is assuming
    the turtle faces north at the begining.
    Post: turtle returns to starting corner and returns to the orientation at which it started.
    '''
    turtle.begin_fill()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.end_fill()

def DrawSquare():
    '''
    This function draws a red 40x40 square tetris shape, composed of four 20x20 smaller squares.
    Pre: The turtle will begin at the bottom left corner, facing top left corner.
    Post: The turtle will finish facing east, at the middle of it's left side. Red square is drawn.
    '''
    turtle.fillcolor('red')
    ColorBlock()
    turtle.forward(20)
    turtle.fillcolor('red')
    ColorBlock()
    turtle.right(90)
    turtle.forward(20)
    turtle.fillcolor('red')
    ColorBlock()
    turtle.left(90)
    turtle.fillcolor('red')
    ColorBlock()
    turtle.right(90)
    turtle.forward(20)

def DrawStick():
    '''
    This function draws four 20x20 blocks atop one another, resembling a stick shape. The shape is green.
    Pre: turtle will begin at bottom left corner, facing top left corner of shape.
    Post: turtle will finish at top left corner, facing north. Green stick is drawn.
    '''
    turtle.fillcolor('green')
    ColorBlock()
    turtle.forward(20)
    turtle.fillcolor('green')
    ColorBlock()
    turtle.forward(20)
    turtle.fillcolor('green')
    ColorBlock()
    turtle.forward(20)
    turtle.fillcolor('green')
    ColorBlock()
    turtle.forward(20)

def DrawZigzag():
    '''
    This function draws a zig zag tetris shape by using four 20x20 blocks. The shape is yellow.
    Pre: the turtle starts at the bottom left corner of the bottom square facing north.
    Post: the turtle finishes at the top left corner of the top square facing north. The zigzag is drawn.
    '''
    turtle.fillcolor('yellow')
    ColorBlock()
    turtle.forward(20)
    turtle.fillcolor('yellow')
    ColorBlock()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.fillcolor('yellow')
    ColorBlock()
    turtle.left(90)
    turtle.fillcolor('yellow')
    ColorBlock()
    turtle.forward(20)

def DrawMountain():
    '''
    This function draws a mountain shape (upside down T shape) using four 20x20 blocks. The shape is blue.
    Pre: the turtle begins at bottom left corner of bottom left square facing north.
    Post: the turtle ends at the bottom left corner of the top middle square, facing north. The mountain is drawn.
    '''
    turtle.fillcolor('blue')
    ColorBlock()
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.fillcolor('blue')
    ColorBlock()
    turtle.forward(20)
    turtle.fillcolor('blue')
    ColorBlock()
    turtle.left(180)
    turtle.forward(20)
    turtle.right(90)
    turtle.fillcolor('blue')
    ColorBlock()


DrawBoard()                     #draws tetris board
Init()                          #moves turtle to bottom left corner facing north
DrawSquare()                    #square is drawn
turtle.right(90)
turtle.forward(20)
turtle.right(180)
DrawStick()                     #stick is drawn
turtle.right(180)
turtle.forward(80)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
DrawZigzag()                    #zigzag is drawn
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(60)
turtle.right(180)
DrawMountain()                  #mountain is drawn
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
DrawZigzag()                    #zigzag is drawn
turtle.left(90)
turtle.forward(20)
turtle.left(90)
DrawStick()                     #stick is drawn
DrawMountain()                  #mountain is drawn
turtle.right(180)
turtle.forward(20)
turtle.left(90)
DrawSquare()                    #square is drawn
turtle.right(90)
turtle.forward(20)
turtle.right(180)
DrawZigzag()                    #zigzag is drawn
turtle.up()
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(20)
turtle.down()
DrawZigzag()                    #zigzag is drawn
turtle.done()                   #end of drawing




'''
Draw tetris board and use user input to place shapes.
author: Youssef Naguib
file:tetris2.py
language: python3.7
description: lab 02 solution
'''
import turtle   #turtle library imported
turtle.speed(0) #maximum turtle speed

def DrawShapeMenu():            #draws shape menu next to board
    """
    This function draws a menu of shapes next to the board for the user to see.
    pre: the turtle is at the datum point (center of canvas facing east).
    post: shape menu is drawn and turtle returns to datum point.
    """
    turtle.up()
    turtle.left(180)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(220)
    turtle.right(90)
    turtle.down()
    DrawB(0)
    turtle.up()
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.down()
    DrawI(0)
    turtle.right(90)
    turtle.up()
    turtle.forward(40)
    turtle.left(90)
    turtle.down()
    DrawL(0)
    turtle.up()
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.down()
    DrawJ(0)
    turtle.up()
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(10)
    turtle.down()
    DrawZ(0)
    turtle.up()
    turtle.forward(-10)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.down()
    DrawS(0)
    turtle.up()
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.down()
    DrawT(0)
    turtle.up()
    turtle.forward(100)
    WriteShapeMenu()
    turtle.down()

def WriteShapeMenu():           #writes letters next to shapes menu
    """
    This function writes the corresponding letter next to its shape in the shape menu.
    pre: the turtle is at the datum point (center of canvas facing east).
    post:letters are drawn into menu and turtle returns to datum point.
    """
    turtle.right(180)
    turtle.forward(115)
    turtle.right(90)
    turtle.forward(220)
    turtle.right(90)
    turtle.write('B')
    turtle.right(90)
    turtle.forward(50)
    turtle.write('I')
    turtle.forward(40)
    turtle.write('L')
    turtle.forward(40)
    turtle.write('J')
    turtle.forward(30)
    turtle.write('Z')
    turtle.forward(30)
    turtle.write('S')
    turtle.forward(30)
    turtle.write('T')
    turtle.left(90)
    turtle.forward(115)
    

def DrawBoard():        #draws the tetris board
    '''
    This function draws an empty 100x200 long rectangular tetris board
    Pre: Turtle is in exact middle of canvas, facing east (this is the datum point)
    Post: Turtle returns to datum point.
    '''
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
  

def ColorBlock():       #draws one block
    '''
    This function draws a 10x10 square, and contains a turtle.begin_fill and turtle.end_fill that
    allows the square to be filled in with a color. The color is determined by turtle.fillcolor,
    a command implemented in the different shapes.
    Pre: turtle starts at bottom left corner of the square and faces east. 
    Post: turtle returns to starting corner and is facing east.
    '''
    turtle.begin_fill()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.end_fill()

def DrawB(rotation):        #draws square (cube)
    '''
    This function draws a red 20x20 square tetris shape, composed of four 10x10 smaller squares.
    Pre: The turtle will begin at the bottom left corner of the cube, facing east.
    Post: The turtle will finish at the bottom left corner, east.Square is drawn.
    Param: rotation determines the orientation at which the shape is drawn(0,90,180,270).
    '''
    turtle.fillcolor('red')
    ColorBlock()
    turtle.forward(10)
    turtle.fillcolor('red')
    ColorBlock()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.fillcolor('red')
    ColorBlock()
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.fillcolor('red')
    ColorBlock()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
 

def DrawI(rotation):        #draws I shape 
    '''
    This function draws four 10x10 blocks atop one another, resembling the letter I. The shape is green.
    Pre: turtle will begin at bottom left corner of bottom square, facing east.
    Post: turtle will return to bottom left corner and face east. The shape will be drawn.
    Param: rotation determines the orientation at which the shape is drawn(0,90,180,270).
    '''
    TurnI(rotation,10)
    turtle.fillcolor('green')
    ColorBlock()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.fillcolor('green')
    ColorBlock()
    turtle.forward(10)
    turtle.fillcolor('green')
    ColorBlock()
    turtle.forward(10)
    turtle.fillcolor('green')
    ColorBlock()
    turtle.forward(-30)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(180)
    TurnI(-rotation,10)
   

def TurnI(rotation,shift):      #rotates I shape
    """
    This function rotates the I shape.
    pre: degree of rotation (0,90,180,270) is input by user when DrawI function is called.
    post: turtle is rotated by the number of degrees the User input (0,90,180,270), and shape is then drawn.
    param: rotation determines the orientation at which the shape is drawn(0,90,180,270).
    """
    turtle.up()
    if rotation == 180 or rotation == -180:
        turtle.left(90)
        turtle.forward(shift)
        turtle.left(90)
        turtle.forward(-shift)
    elif rotation == 90 or rotation == -270:
        turtle.forward(shift)
        turtle.left(90)
    elif rotation == -90 or rotation == 270:
        turtle.right(90)
        turtle.forward(-shift)       
    turtle.down()    

def DrawZ(rotation):            #draws Z shape
    '''
    This function draws a tetris shape that resembles a letter z by using four 10x10 blocks. The shape is purple.
    Pre: the turtle starts at the bottom left corner of the top left square facing east.
    Post: the turtle finishes at the bottom left corner of the top left square facing east. The z is drawn.
    Param: rotation determines the orientation at which the shape is drawn(0,90,180,270).
    '''
    TurnZ(rotation,10)
    turtle.fillcolor('purple')
    ColorBlock()
    turtle.forward(10)
    turtle.fillcolor('purple')
    ColorBlock()
    turtle.left(90)
    turtle.forward(10)
    turtle.fillcolor('purple')
    ColorBlock()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.fillcolor('purple')
    ColorBlock()
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    TurnZ(-rotation,10)

def TurnZ(rotation,shift):          #rotates Z shape
    """
    This function rotates the Z shape.
    pre: degree of rotation (0,90,180,270) is input by user when DrawZ function is called.
    post: turtle is rotated by the number of degrees the User input (0,90,180,270), and shape is then drawn.
    param: rotation determines the orientation at which the shape is drawn(0,90,180,270).
    param: shift moves the turtle forward one block so it is in the right position to begin drawing.
    """
    turtle.up()
    if rotation == 180 or rotation == -180:
        turtle.forward(shift)
        turtle.left(90)
        turtle.forward(shift)
        turtle.left(90)
    elif rotation == 90 or rotation == -270:
        turtle.forward(shift)
        turtle.left(90)
    elif rotation == -90 or rotation == 270:
        turtle.right(90)
        turtle.forward(-shift)
        
    turtle.down()    

def DrawS(rotation):            #Draws S shape
    '''
    This function draws a tetris shape that resembles the letter S by using four 10x10 blocks. The shape is yellow.
    Pre: the turtle starts at the bottom left corner of the bottom left square facing east.
    Post: the turtle returns to the bottom left corner of the bottom left square facing east. The S is drawn.
    Param: rotation determines the orientation at which the shape is drawn(0,90,180,270).
    '''
    TurnS(rotation,10)
    turtle.fillcolor('yellow')
    ColorBlock()
    turtle.forward(10)
    turtle.fillcolor('yellow')
    ColorBlock()
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.fillcolor('yellow')
    ColorBlock()
    turtle.forward(10)
    turtle.fillcolor('yellow')
    ColorBlock()
    turtle.forward(-20)
    turtle.left(90)
    turtle.forward(-10)
    turtle.right(90)
    TurnS(-rotation,10)

def TurnS(rotation,shift):              #rotates S shape
    """
    This function rotates the S shape.
    pre: degree of rotation (0,90,180,270) is input by user when DrawS function is called.
    post: turtle is rotated by the number of degrees the User input (0,90,180,270), and shape is then drawn.
    param: rotation determines the orientation at which the shape is drawn(0,90,180,270).
    param: shift moves the turtle forward one block so it is in the right position to begin drawing.
    """

    turtle.up()
    if rotation == 180 or rotation == -180:
        turtle.forward(shift)
        turtle.left(90)
        turtle.forward(shift)
        turtle.left(90)
    elif rotation == 90 or rotation == -270:
        turtle.forward(shift)
        turtle.left(90)
    elif rotation == -90 or rotation == 270:
        turtle.right(90)
        turtle.forward(-shift)
        
    turtle.down()


def DrawT(rotation):                #draws T shape
    '''
    This function draws a tetris shape that resembles an upside down letter T by using four 10x10 blocks. The shape is blue.
    Pre: the turtle starts at the bottom left corner of the bottom left square facing east.
    Post: the turtle finishes at the bottom left corner of the bottom left square facing east. The T is drawn.
    Param: rotation determines the orientation at which the shape is drawn(0,90,180,270).
    '''
    TurnT(rotation,10)
    turtle.fillcolor('blue')
    ColorBlock()
    turtle.forward(10)
    turtle.fillcolor('blue')
    ColorBlock()
    turtle.forward(10)
    turtle.fillcolor('blue')
    ColorBlock()
    turtle.left(90)
    turtle.forward(10)
    turtle.fillcolor('blue')
    ColorBlock()
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    TurnT(-rotation,10)

def TurnT(rotation,shift):                  #rotates T shape
    """
    This function rotates the T shape.
    pre: degree of rotation (0,90,180,270) is input by user when DrawT function is called.
    post: turtle is rotated by the number of degrees the User input (0,90,180,270), and shape is then drawn.
    param: rotation determines the orientation at which the shape is drawn(0,90,180,270).
    """
    turtle.up()
    if rotation == 180 or rotation == -180:
        turtle.forward(shift)
        turtle.left(90)
        turtle.forward(shift)
        turtle.left(90)
    elif rotation == 90 or rotation == -270:
        turtle.forward(shift)
        turtle.left(90)
    elif rotation == -90 or rotation == 270:
        turtle.left(-90)
        turtle.forward(-shift)
        
    turtle.down()

def DrawL(rotation):                #draws L shape
    '''
    This function draws a tetris shape that resembles a letter L by using four 10x10 blocks. The shape is orange.
    Pre: the turtle starts at the bottom left corner of the bottom left square facing east.
    Post: the turtle finishes at the bottom left corner of the bottom left square facing east. The L is drawn.
    Param: rotation determines the orientation at which the shape is drawn(0,90,180,270).
    '''
    TurnL(rotation,10)
    turtle.fillcolor('orange')
    ColorBlock()
    turtle.forward(10)
    turtle.fillcolor('orange')
    ColorBlock()
    turtle.left(90)
    turtle.forward(10)
    turtle.fillcolor('orange')
    ColorBlock()
    turtle.forward(10)
    turtle.fillcolor('orange')
    ColorBlock()
    turtle.forward(-20)
    turtle.right(90)
    turtle.forward(-10)
    TurnL(-rotation,10)

def TurnL(rotation,shift):              #turns L shape
    """
    This function rotates the L shape.
    pre: degree of rotation (0,90,180,270) is input by user when DrawL function is called.
    post: turtle is rotated by the number of degrees the User input (0,90,180,270), and shape is then drawn.
    param: rotation determines the orientation at which the shape is drawn(0,90,180,270).
    param: shift moves the turtle forward one block so it is in the right position to begin drawing.
    """
    turtle.up()
    if rotation == 180 or rotation == -180:
        turtle.forward(shift)
        turtle.left(90)
        turtle.forward(shift)
        turtle.left(90)
    elif rotation == 90 or rotation == -270:
        turtle.forward(shift)
        turtle.left(90)
    elif rotation == -90 or rotation == 270:
        turtle.left(90)
        turtle.forward(shift)
        turtle.right(180)
    turtle.down()
    
def DrawJ(rotation):        #draws J shape (backwards L)
    '''
    This function draws a tetris shape that resembles a letter J by using four 10x10 blocks. The shape is maroon.
    Pre: the turtle starts at the bottom left corner of the bottom left square facing east.
    Post: the turtle finishes at the bottom left corner of the bottom left square facing east. The J is drawn.
    Param: rotation determines the orientation at which the shape is drawn(0,90,180,270).
    '''
    TurnJ(rotation,10)
    turtle.fillcolor('maroon')
    ColorBlock()
    turtle.forward(10)
    turtle.fillcolor('maroon')
    ColorBlock()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.fillcolor('maroon')
    ColorBlock()
    turtle.forward(10)
    turtle.fillcolor('maroon')
    ColorBlock()           
    turtle.forward(-20)
    turtle.right(90)
    turtle.forward(-20)
    TurnJ(-rotation,10)
    
def TurnJ(rotation,shift):          #rotates J shape
    """
    This function rotates the J shape.
    pre: degree of rotation (0,90,180,270) is input by user when DrawJ function is called.
    post: turtle is rotated by the number of degrees the User input (0,90,180,270), and shape is then drawn.
    param: rotation determines the orientation at which the shape is drawn(0,90,180,270).
    param: shift moves the turtle forward one block so it is in the right position to begin drawing.
    """
    turtle.up()
    if rotation == 180 or rotation == -180:
        turtle.forward(shift)
        turtle.left(90)
        turtle.forward(shift)
        turtle.left(90)
    elif rotation == 90 or rotation == -270:
        turtle.forward(shift)
        turtle.left(90)
    elif rotation == -90 or rotation == 270:
        turtle.left(90)
        turtle.forward(shift)
        turtle.right(180)
        
    turtle.down()
    

def MoveTo(row,column):     #moves turtle around board
    """
    This function moves the turtle to the user's chosen spot on the board, where the chosen shape will be drawn)
    pre:turtle is at datum point.
    post:turtle is at specified point on 10x20 block board.
    param:row determines the height away from the datum at which the block will be drawn.
    param:column determines the length away from the datum at which the block will be drawn.
    """
    turtle.up()
    turtle.forward(10*column)
    turtle.left(90)
    turtle.forward(10*row)
    turtle.right(90)
    turtle.down()
    


def Start():            #draws shapes using user's input
    """
    this function asks the user to input a shape, orientation, row position, and column position in order
    to draw any chosen shape in any orientation anywhere on the board.
    pre:turtle is at datum point, user will be asked to input variables.
    post: shape will be drawn according to user's input. turtle returns to datum point and the function may
    be repreated.
    """
    shape = input("Enter a letter {BILJZST} to choose shape to place: ")
    rotation = int(input("Enter 0,90,180, or 270 for the rotation: "))
    row = int(input("row number (0 to 19) for lower left space: "))
    column = int(input("column number (0 to 9) for lower left space "))
    MoveTo(row,column)
    if shape == 'B':
            DrawB(0)
    elif shape == 'I':
            DrawI(rotation)
    elif shape == 'L':
            DrawL(rotation)
    elif shape == 'J':
            DrawJ(rotation)
    elif shape == 'Z':
            DrawZ(rotation)
    elif shape == 'S':
            DrawS(rotation)
    elif shape == 'T':
            DrawT(rotation)

    turtle.up()
    turtle.left(90)
    turtle.forward(-row*10)
    turtle.right(90)
    turtle.forward(-column*10)
             
def main():                 #main program
    """
    This function runs the main program. It draws the board and the shape menu, then proceeds to ask
    the user for inputs. (shape, rotation, row, column)
    Pre:Turtle is in middle of canvas facing east.
    Post:Turtle returns to datum point. Program will finish, user can close window to quit.
    """
    DrawBoard()
    DrawShapeMenu()
    DrawS(0)
    turtle.forward(30)
    DrawL(0)
    turtle.forward(20)
    DrawT(0)
    turtle.forward(30)
    DrawZ(0)
    turtle.forward(-80)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    DrawI(0)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    DrawJ(0)
    turtle.forward(30)
    DrawI(-90)
    turtle.forward(40)
    DrawT(90)
    turtle.right(90)
    turtle.forward(-10)
    turtle.left(90)
    turtle.forward(-30)
    DrawB(90)
    turtle.forward(-50)
    turtle.left(90)
    turtle.forward(-30)
    turtle.right(90)
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    Start()
    print("Close canvas window to quit")

if __name__=="__main__":
    main()
    

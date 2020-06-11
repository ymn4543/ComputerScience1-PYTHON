"""
Draw a recursive bowtie pattern.
file: bowties.py
author: Youssef Naguib
language: python3.7
description: lab 3 solution
"""
import turtle as tt              #imports turtle library and renames it tt 
tt.speed(0)                      #max turtle speed


def DrawBowtie0(size):
    """
    Draws nothing. Base case for recusrive function. turtle doesnt move.
    pre: size must be zero:
    post: turtle remains where it is.
    size: length of one side of a triangle in a bowtie.
    """
    pass

def DrawOneBowtie(size):
    """
    Draws one bowtie in the middle of the screen.
    pre: turtle is facing east,pen is down.
    post: turtle returns to starting point, bowtie is drawn.
    size: length of one side of a triangle in a bowtie.
    """
    tt.pencolor('red')
    tt.right(30)
    tt.forward(size)
    tt.left(120)
    tt.forward(size)
    tt.left(120)
    tt.forward(size*2)
    tt.right(120)
    tt.forward(size)
    tt.right(120)
    tt.forward(size)
    tt.left(30)
    tt.up()
    tt.forward(size/4)
    tt.left(90)
    tt.down()
    tt.fillcolor('Blue')
    tt.begin_fill()
    tt.circle(size/4)
    tt.end_fill()
    tt.up()
    tt.left(90)
    tt.forward(size/4)
    tt.right(180)
    tt.down()
    
def DrawBowtie1(size):
    """
    Draws one bowtie in the middle of the screen, goes to four different
    positions where the bowtie pattern would continue, and calls DrawBowtie0,
    which passes. This is helpful for the recursive function.
    pre: turtle is facing east,pen is down.
    post: turtle returns to starting point, bowtie is drawn.
    size: length of one side of a triangle in a bowtie.
    """
    DrawOneBowtie(size)
    tt.up()
    tt.left(30)
    tt.forward(size*2)
    tt.down()
    DrawBowtie0(size)
    tt.up()
    tt.forward(-size*2)
    tt.right(60)
    tt.forward(size*2)
    tt.down()
    DrawBowtie0(size)
    tt.up()
    tt.forward(-size*2)
    tt.right(120)
    tt.forward(size*2)
    tt.right(180)
    tt.down()
    DrawBowtie0(size)
    tt.up()
    tt.forward(size*2)
    tt.left(180)
    tt.forward(size*2)
    tt.right(180)
    tt.down()
    DrawBowtie0(size)
    tt.up()
    tt.forward(size*2)

    
def DrawBowties(size,depth):
    """
    Recursive function which draws bowtie pattern, with one bowtie in center,
    and 4 bowties with centers 2 * the triangle side length away. Each
    level of depth makes bowties smaller by factor of 3.
    pre: turtle is facing east,pen is down.
    post: turtle returns to starting point, bowtie pattern is drawn.
    size: length of one side of a triangle in a bowtie.
    depth: number of times user wants to repeat recursion. The larger the depth,
    the more bowties drawn.
    """
    if depth == 0:
        pass
    else:
        DrawOneBowtie(size)
        tt.up()
        tt.left(30)
        tt.forward(2*size)
        tt.down()
        DrawBowties(size/3,depth-1)
        tt.up()
        tt.forward(-2*size)
        tt.right(60)
        tt.forward(size*2)
        tt.down()
        DrawBowties(size/3, depth-1)
        tt.up()
        tt.forward(-size*2)
        tt.right(120)
        tt.forward(size*2)
        tt.right(180)
        tt.down()
        DrawBowties(size/3,depth-1)
        tt.up()
        tt.forward(size*2)
        tt.left(120)
        tt.forward(size*2)
        tt.right(180)
        tt.down()
        DrawBowties(size/3,depth-1)
        tt.up()
        tt.forward(size*2)
        tt.left(30)


def main():
    """
    Main function runs the program. asks for user input for size and depth,
         parameters that DrawBowties() uses.
    Pre: User inputs data. Must be integers.
         Turtle is facing east and in center of canvas.
    Post: Program is run, turtle returns to starting point and
          recursive pattern is drawn.
    """
    size=int(input('enter size: '))
    depth=int(input('enter depth: '))
    tt.setup(size*6,size*6)
    DrawBowties(size,depth)
    
if __name__ == "__main__":
    main()

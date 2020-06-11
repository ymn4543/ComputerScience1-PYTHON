"""
file: circles.py
author: Youssef Naguib   <ymn4545@g.rit.edu>
Language: python3.7
Description: hw03 solution
purpose: draws a circle shaped pattern to a certain detail.
"""

import turtle as tt     #imports turtle library and names it tt    
tt.speed(0)             #sets turtle speed to max

def DrawCircle(N,size):       #recursive function for circle drawing
    """
    This function draws a circle pattern that depends on the parameters.
    Pre:turtle is in middle of canvas facing east.
    Post:turtle returns to starting point anf faces east. The pattern is drawn.
    Param: N determines the number of recursions. This will change the number of
    times the function is called.
    Param: size determines the radius of the first circle.Each row of circles
    have a radius that is cut in half to the row below it.
    """
    if N == 0:
        pass
    if N == 1:
        tt.down()
        tt.pensize(2)
        tt.circle(size)
        tt.up()
    if N > 1:
        tt.down()
        tt.pensize(2)
        tt.circle(size)
        tt.up()
        tt.left(90)
        tt.forward(size)
        tt.right(90)
        tt.forward(size)
        tt.down()
        DrawCircle(N-1,size/2)
        tt.up()
        tt.forward(-size*2)
        tt.down()
        DrawCircle(N-1,size/2)
        tt.up()
        tt.forward(size)
        tt.right(90)
        tt.forward(size)
        tt.left(90)
    
        
def main():                                             #main program
    """
    This function runs the main program, it takes the user input for
    N and size and draws the circle pattern.
    Pre:Canvas is empty. Turtle is in middle of canvas facing east.
    Post: After user has input arguments, the pattern is drawn and the turtle
    returns to starting point facing east. "close canvas to quit" is printed.
    """
    N = int(input("Enter a positive integer for N:"))
    size = int(input("Enter circle radius:"))       
    DrawCircle(N,size)
    tt.done
    print("close canvas to quit")

if __name__=="__main__":
    main()
    

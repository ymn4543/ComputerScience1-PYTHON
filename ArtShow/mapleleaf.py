"""
A recursive maple leaf is drawn, it looks 3D.
file: mapleleaf.py
author: Youssef Naguib
language: Python3.7
description: Python art show submission
"""
import turtle as tt
import random
tt.speed(0)
tt.colormode(255)
tt.bgcolor('black')
tt.title('Youssef Naguib')

def DrawToronto(x,s):
    """
    This function keeps drawing maple leaves, increasing their size each
    time and rotating them by 1 degree to the right.
    Pre:x and s must be positive intigers
    Post: A maple leaf pattern is drawn that looks 3D
    """
    if x==0:
        pass
    elif x == 1:
        DrawLeaf(s)      
    elif x > 1:
        DrawLeaf(s)
        tt.right(1)
        x-=1
        s+=10
        DrawToronto(x,s)
        tt.done()
    print('The drawing is finished')   
      
def DrawLeaf(s):
    """
    This function draws one maple leaf of size s.
    Pre: s must be a positive intiger
    Post: A red maple leaf is drawn
    """
    tt.up()
    tt.right(90)
    tt.forward(s/1.5)
    tt.left(90)
    tt.pensize(1)
    tt.pencolor('red')
    tt.down()
    tt.forward(s/30)
    tt.left(90)
    tt.forward(s/3) #top of stem at right
    tt.right(105)
    tt.forward(s/2.5) #bottom right edge leaf
    tt.left(120)
    tt.forward(s/6)
    tt.right(70)
    tt.forward(s/2)
    tt.left(120)
    tt.forward(s/8)
    tt.right(90)
    tt.forward(s/4) #top point of right leaf
    tt.left(130)
    tt.forward(s/4)
    tt.right(105)
    tt.forward(s/8)
    tt.left(130)
    tt.forward(s/3) # right indent
    tt.right(140)
    tt.forward(s/2)
    tt.left(120)
    tt.forward(s/7) 
    tt.right(80)
    tt.forward(s/2.5) #top point
    tt.left(120)
    tt.forward(s/2.5)
    tt.right(80)
    tt.forward(s/7)
    tt.left(120)
    tt.forward(s/2) #left indent
    tt.right(140)
    tt.forward(s/3)
    tt.left(130)
    tt.forward(s/8)
    tt.right(110)
    tt.forward(s/4) #top left leaf
    tt.left(130)
    tt.forward(s/4)
    tt.right(105)
    tt.forward(s/8)
    tt.left(130)
    tt.forward(s/2)
    tt.right(70)
    tt.forward(s/6)
    tt.left(130.5)
    tt.forward(s/2.5)
    tt.right(105)
    tt.forward(s/3)
    tt.left(90)
    tt.forward(s/10)
    tt.up()
    tt.goto(0,0)  
  
def main():
    """
    This is the main function and it is executed when the user runs this program.
    It will draw a maple leaf pattern with 35 maple leaves.
    """
    tt.tracer(0,0)
    DrawToronto(35,50)
    tt.update()
    
    
    

if __name__ == "__main__":
    main()
        

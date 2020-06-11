"""
Draws a trail of triangles.
file: arrows.py
author: Youssef Naguib
language: Python3.7
description: lab 4 solution
"""
import turtle as tt
import random
import math
MAX_FIGURES = 500
BOUNDING_BOX = 200
MAX_DISTANCE = 30
MAX_SIZE = 30
MAX_ANGLE = 30

def draw_triangle(size):
    """
    This function draws an equilateral triangle with side lengths of the
    parameter size.
    Pre: size must be positive integer.
    Post: triangle is drawn on canvas.
    Param: size is the length of one side of the triangle.
    """
    tt.down()
    tt.forward(size)
    tt.left(120)
    tt.forward(size)
    tt.left(120)
    tt.forward(size)
    tt.left(120)

def draw_fig_iter(number, z=0):
    """
    This function draws a trail of triangles, iteratively.
    Pre:number must be a positive integer.
    Post: triangle path is drawn on canvas.
    Param: number is the ammount of triangles that will be drawn.
    Param: z is an accumulator that stores the sum of the areas
           of all the triangles drawn.
    Variable: distance is the distance between each triangle and the next,
              it is randomly generated each time a new triangle is drawn.
    Variable: size is the parameter that draw_triangle uses to set the
              side lengths of the triangle.
    Variable: R is the red color value, between 0 and 255, randomly generated
    Variable: G is the green color value, between 0 and 255, randomly generated
    Variable: B is the blue color value, between 0 and 255, randomly generated
    Variable: angle is the amount in degrees that the turtle will rotate
              after drawing each triangle. It is randomly determined each time.
    """
    while number > 0:
        distance = random.randint(1, MAX_DISTANCE)
        size = random.randint(1, MAX_SIZE)
        R = random.random()
        G = random.random()
        B = random.random()
        angle = random.randint(-MAX_ANGLE, MAX_ANGLE)
        tt.down()
        tt.fillcolor(R,G,B)
        tt.begin_fill()
        draw_triangle(size)
        tt.end_fill()
        tt.left(angle)
        tt.up()
        tt.forward(distance)
        z += ((math.sqrt(3))/4) * (size**2)
        number = number-1
        if tt.xcor() > BOUNDING_BOX-50 or tt.xcor() < -BOUNDING_BOX+50:
            tt.up()
            tt.forward(-distance)
            tt.left(180)
            tt.down()
        elif tt.ycor() > BOUNDING_BOX-50 or tt.ycor() < -BOUNDING_BOX+50:
            tt.up()
            tt.forward(-distance)
            tt.left(180)
            tt.down()
    print("The total area painted is ", float(z), "units.")
    return z
    
    
def draw_fig_rec(number,accum=0):
    """
    This function draws a trail of triangles, recursively.
    Pre:number must be a positive integer.
    Post: triangle path is drawn on canvas.
    Param: number is the ammount of triangles that will be drawn.
    Param: accum is an accumulator that stores the sum of the areas
           of all the triangles drawn.
    Variable: distance is the distance between each triangle and the next,
              it is randomly generated each time a new triangle is drawn.
    Variable: size is the parameter that draw_triangle uses to set the
              side lengths of the triangle.
    Variable: R is the red color value, between 0 and 255, randomly generated
    Variable: G is the green color value, between 0 and 255, randomly generated
    Variable: B is the blue color value, between 0 and 255, randomly generated
    Variable: angle is the amount in degrees that the turtle will rotate
              after drawing each triangle. It is randomly determined each time.
    """
    distance = random.randint(1, MAX_DISTANCE)
    size = random.randint(1, MAX_SIZE)
    R = random.random()
    G = random.random()
    B = random.random()
    angle = random.randint(-MAX_ANGLE, MAX_ANGLE)
    if number > 0 :
        tt.fillcolor(R,G,B)
        tt.begin_fill()
        draw_triangle(size)
        tt.end_fill()
        tt.up()
        tt.forward(distance)
        tt.left(angle)
        tt.down()
        accum = accum + ((math.sqrt(3))/4) * (size**2)
        if tt.xcor() > BOUNDING_BOX-50 or tt.xcor() < -BOUNDING_BOX+50:
            tt.up()
            tt.forward(-distance)
            tt.left(180)
            tt.down()
        elif tt.ycor() > BOUNDING_BOX-50 or tt.ycor() < -BOUNDING_BOX+50:
            tt.up()
            tt.forward(-distance)
            tt.left(180)
            tt.down()
        return draw_fig_rec(number-1,accum)
       
    else:
        print("The total area painted is ", float(accum), "units.")
        return accum
   
    
def main():
    """
    This is the main function that runs the program.It will prompt user to input
    the number of triangles they want drawn. Then it will draw a recursive
    pattern and print the total area of the trinagles. It will then pause,
    wait for the user to hit enter, and repeat the process iteritively.
    User must close window to end program.
    Pre: User must input positive number for number of triangles.
    Post: Two patterns have been drawn, and their areas printed. Only the second
          pattern is visable at this point since the first gets erased.
          User can end program.
    """
    tt.setup(BOUNDING_BOX*2,BOUNDING_BOX*2)
    tt.speed(0)
    arrows = int(input('Arrows (0-500): '))
    if arrows >= 0 and arrows <= MAX_FIGURES:
        draw_fig_rec(arrows)
        input('Hit enter to continue')
        tt.reset()
        tt.setup(BOUNDING_BOX*2,BOUNDING_BOX*2)
        tt.speed(0)
        draw_fig_iter(arrows)
        input("close window to exit")
    else:
        print("Arrows must be between 0 and 500 inclusive.")
        exit()

    
if __name__ == "__main__" :
    main()

"""
Find real roots of polynomials.
file: roots.py
author: Youssef Naguib
language: python3.7
description:homework 2 solution
"""
import math

def quadratic_roots(a,b,c):
    """
    This function determines whether a second degree polynomial
    has 0,1, or 2 roots, displays the full equation, and calculates the roots.
    Param: a,b,c refer to the A,B,C coefficiant values in a second degree
    polynomial (Ax^2+Bx+C)
    Pre: three parameters must be entered into the function for a, b, and c.
    Post: function calculates roots, equation, and number of roots using
    the given parameters as coefficiants.
    """

    #ONE ROOT
    if ((b**2) - (4 * a * c)) == 0:
        #write full equation in (Ax^2+Bx+C) form
        print("Equation:", a, "x^2+", b, "x+", c, "=0",sep="")
        #state there is only one root  
        print("One root.")
        # calculate root
        print("x=",((-b)+( (math.sqrt( (b**2) - (4 * a * c))/(2*a))))) 
         
    #TWO ROOTS    
    elif ((b**2) -(4 * a * c)) >= 1:
        #write full equation in (Ax^2+Bx+C) form
        print("Equation:", a, "x^2+", b, "x+", c, "=0",sep="" )
        #state there is only two roots  
        print("Two roots.")
        # calculate roots
        print("x=",((-b+math.sqrt((b**2) - (4 * a * c)))/(2*a)),sep="")
        print("x=",((-b-math.sqrt((b**2) - (4 * a * c)))/(2*a)),sep="")      
             
    #NO ROOTS    
    else:
        #write full equation in (Ax^2+Bx+C) form
        print("Equation:", a, "x^2+", b, "x+", c, "=0", sep="" )
        # state that there are no roots
        print("No roots.")


def test_quadratic_roots():
    """
    This function tests 15 different cases of the quadratic_roots function to verify that
    the calculations are valid.
    Pre: once function is called, it will ask user to press enter each time a test is run
    Post: the quadratic_roots function will be tested 15 times and all equations, roots, and number of roots
    will be displayed for each test.
    """
    input("Press enter to start tests")
    quadratic_roots(2,4,2)                  #all positive numbers
    input("Press enter to continue tests")
    quadratic_roots(2,-11,-21)              #a is positive, b and c are negative
    input("Press enter to continue tests")    
    quadratic_roots(4,1,-4)                 #a and b are positive, c is negative
    input("Press enter to continue tests")
    quadratic_roots(1,1,-3)                 #a and b are equal and positive,c is negative
    input("Press enter to continue tests")    
    quadratic_roots(7,-49,27)               #a and c are positive, b is negative
    input("Press enter to continue tests")
    quadratic_roots(1,-1,-2)                #a is positive, b and c are negative
    input("Press enter to continue tests")
    quadratic_roots(100,-2,304)             #a and c are very large numbers, b is negative
    input("Press enter to continue tests")
    quadratic_roots(-10,-9,-6)              #a,b,and c are negative
    input("Press enter to continue tests")
    quadratic_roots(-7,3,6)                 #a is negative, b and c are positive
    input("Press enter to continue tests")
    quadratic_roots(8,-7,-47)               #a is positive, b and c are negative, c is a very low number
    input("Press enter to continue tests")
    quadratic_roots(2,0,0)                  #a is positive,b and c are 0
    input("Press enter to continue tests")
    quadratic_roots(-2,-5,-4)               #a,b,c are negative
    input("Press enter to continue tests")
    quadratic_roots(3,6,3)                  #a,b,c are positive
    input("Press enter to continue tests")
    quadratic_roots(.54,20,6)               #a is a decimal,b and c are positive
    input("Press enter to continue tests")
    quadratic_roots(.64,-1.4,.47)           #a,b,c are decimals, b is negative
    print("Tests complete.")
    
quadratic_roots(1,2,1)




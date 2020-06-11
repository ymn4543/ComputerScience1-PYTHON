"""
Shapy Turtle is a turtle interpreter
file:shapy_turtle.py
author: Youssef Naguib
language: Python#.7
description: Lab 5 solution
"""
import turtle as tt

def ShapyTurtle(st):
    """
    This function takes in a string given by user and interprets the string as
    a line of turtle commands which are executed in order.
    Param st: st is a string input by the user
    Pre: st must be a valid string.
    Post: Turtle commands are interpreted and run on canvas in correct order.
    Variable x: keeps track of the index of the character in the loop
    """
    x=0
    for ch in st:
        if st != '':
            tt.setup(1000,1000)
            if ch == '<':
                x+=1
                st = st[int(x):]
                ProcessLeft(st)
            elif ch == ">":
                x+=1
                st = st[int(x):]
                ProcessRight(st)
            elif ch == "S":
                x+=1
                st = st[int(x):]
                Process_S(st)
            elif ch == "T":
                x+=1
                st = st[int(x):]
                Process_T(st)
            elif ch == "C":
                x+=1
                st = st[int(x):]
                Process_C(st)
            elif ch == "F":
                x+=1
                st = st[int(x):]
                Process_F(st)
            elif ch == "B":
                x+=1
                st = st[int(x):]
                Process_B(st)
            elif ch == "U":
                 x+=1
                 st = st[int(x):]
                 Process_U(st)
            elif ch == "D":
                 x+=1
                 st = st[int(x):]
                 Process_D(st)
            elif ch == "R":
                 x+=1
                 st = st[int(x):]
                 Process_R(st)
            elif ch == "P":
                 x+=1
                 st = st[int(x):]
                 Process_P(st)
            if ch == "G":
                x+=1
                st = st[int(x):]
                print("Inside G")
                Process_G(st)
            elif ch == "Z":
                x+=1
                st = st[int(x):]
                Process_Z(st)
            else:
                print("Command not read")
                x+=1
                break
    tt.done()

def NumberCheck(x):
    """
    This function checks if the next character is a number, and if true
    adds it to a string, it does this until it hits a character that is
    not a number.
    pre: a string is input as the parameter
    post: a resulting string is returned that is a number
    :param x: is the string that the function will read
    variable result: result is a string that displays the digits found in a row
    """
    result = ''
    for chr in x:
        if chr.isdigit():
            result += chr
        else:
            break
    return result

def ProcessLeft(st):
    """
    This function makes the turtle rotate left
    pre: ShapyTurtle function must come across <
    post: Turtle rotates left x degrees
    :param st: string that is read by function
    variable x: the number of degrees for rotation
    variable st: the new string that slices off x
    """
    x = NumberCheck(st)
    st = st[(len(x)):]
    tt.left(int(x))
    ShapyTurtle(st)

def ProcessRight(st):
    """
    This function makes the turtle rotate right
    pre: ShapyTurtle function must come across >
    post: Turtle rotates right x degrees
    :param st: string that is read by function
    variable x: the number of degrees for rotation
    variable st: the new string that slices off x
    """
    x = NumberCheck(st)
    st = st[(len(x)):]
    tt.right(int(x))
    ShapyTurtle(st)

def Process_S(st):
    """
    This function makes the turtle draw a square
    pre: ShapyTurtle function must come across letter S
    post: Turtle draws square of length size x
    :param st: string that is read by function
    variable x: the length of one side of the square
    variable st: the new string that slices off x
    """
    x = NumberCheck(st)
    st = st[(len(x)):]
    tt.left(90)
    tt.forward(int(x))
    tt.left(90)
    tt.forward(int(x))
    tt.left(90)
    tt.forward(int(x))
    tt.left(90)
    tt.forward(int(x))
    ShapyTurtle(st)

def Process_T(st):
    """
    This function makes the turtle draw a triangle
    pre: ShapyTurtle function must come across letter T
    post: Turtle draws triangle of length size x
    :param st: string that is read by function
    variable x: the length of one side of the triangle
    variable st: the new string that slices off x
    """
    x = NumberCheck(st)
    st = st[(len(x)):]
    tt.left(120)
    tt.forward(int(x))
    tt.left(120)
    tt.forward(int(x))
    tt.left(120)
    tt.forward(int(x))
    ShapyTurtle(st)

def Process_C(st):
    """
    This function makes the turtle draw a circle
    pre: ShapyTurtle function must come across letter C
    post: Turtle draws circle of radius x
    :param st: string that is read by function
    variable x: the length of the radius of the circle
    variable st: the new string that slices off x
    """
    x = NumberCheck(st)
    st = st[(len(x)):]
    tt.circle(int(x))
    ShapyTurtle(st)

def Process_F(st):
    """
    This function moves the turtle forward
    pre: ShapyTurtle function must come across letter F
    post: Turtle moves forward by x
    :param st: string that is read by function
    variable x: the distance forward that turtle will travel
    variable st: the new string that slices off x
    """
    x = NumberCheck(st)
    st = st[(len(x)):]
    tt.forward(int(x))
    ShapyTurtle(st)

def Process_B(st):
    """
    This function moves the turtle backward
    pre: ShapyTurtle function must come across letter B
    post: Turtle moves backward by x
    :param st: string that is read by function
    variable x: the distance backward that turtle will travel
    variable st: the new string that slices off x
    """
    x = NumberCheck(st)
    st = st[(len(x)):]
    tt.forward(-(int(x)))
    ShapyTurtle(st)

def Process_U(st):
    """
    This function lifts the turtle pen up
    pre: ShapyTurtle function must come across letter U
    post: Turtle pen is up
    :param st: string that is read by function
    variable x: checks if there is a number after U in string
    variable st: the new string that slices off x
    """
    x = NumberCheck(st)
    st = st[(len(x)):]
    tt.up()
    ShapyTurtle(st)

def Process_D(st):
    """
    This function puts the turtle pen down
    pre: ShapyTurtle function must come across letter D
    post: Turtle pen is down
    :param st: string that is read by function
    variable x: checks if there is a number after D in string
    variable st: the new string that slices off x
    """
    x = NumberCheck(st)
    st = st[(len(x)):]
    tt.down()
    ShapyTurtle(st)

def Process_R(st):
    """
    This function draws a rectangle with turtle
    pre: ShapyTurtle function must come across letter R
    post: Rectangle of width w and length l is drawn
    :param st: string that is read by function
    variable l: length of rectangle
    variable w: width of rectangle
    variable st: the new string that slices off x
    """
    l = str(NumberCheck(st))
    st = st[(len(l)+1):]
    w = str(NumberCheck(st))
    st = st[len(w):]
    tt.down()
    tt.left(90)
    tt.forward(int(w))
    tt.left(90)
    tt.forward(int(l))
    tt.left(90)
    tt.forward(int(w))
    tt.left(90)
    tt.forward(int(l))
    tt.up()
    ShapyTurtle(st)

def Process_P(st):
    """
    This function draws a polygon with turtle
    pre: ShapyTurtle function must come across letter P
    post: Polygon with s sides of l lengths is drawn
    :param st: string that is read by function
    variable l: length of one side
    variable s: number of sides
    variable a: angle of rotation after each side is drawn
    variable i: intiger value of s used in while loop to keep track of
                remaining sides
    variable st: the new string that slices off x
    """
    s = str(NumberCheck(st))
    print(s)
    st = st[(len(s)+1):]
    l = str(NumberCheck(st))
    st = st[len(l):]
    a = 360/int(s)
    i = int(s)
    tt.down()
    while i != 0:
        i -= 1
        tt.left(a)
        tt.forward(int(l))
    tt.up()
    ShapyTurtle(st)

def Process_G(st):
    """
    This function makes turtle go to coordinates x,y
    pre: ShapyTurtle function must come across letter G
    post: turtle is at position x,y, maintains its orientation
    :param st: string that is read by function
    variable x: x coordinate
    variable y: y coordinate
    variable st: the new string that slices off x
    """
    x = str(NumberCheck(st))
    st = st[(len(x)+1):]
    y = str(NumberCheck(st))
    st = st[len(y):]
    tt.up()
    tt.goto(int(x),int(y))
    tt.down()
    ShapyTurtle(st)

def Process_Z(st):
    """
    This function changes the turtle's pen color
    pre: ShapyTurtle function must come across letter Z
    post: Turtle's pen color is changed to appropriate color
    :param st: string that is read by function
    variable color: string that will determine which color to use
    variable st: the new string that slices off x
    """
    color = str(NumberCheck(st))
    st = st[len(color):]
    if int(color) == 0:
        tt.pencolor('red')
    elif int(color) == 1:
        tt.pencolor('blue')
    elif int(color) == 2:
        tt.pencolor('green')
    elif int(color) == 3:
        tt.pencolor('yellow')
    elif int(color) == 4:
        tt.pencolor('brown')
    else:
        tt.pencolor('black')
    ShapyTurtle(st)

def main():
    """
    This is the main function which prompts for user input and runs the
    ShapyTurtle function.
    pre: user input is taken and converted to string
    post: string is run through ShapyTurtle function and appropriate actions
          are completed.
    """
    st = input('Please enter ShapyTurtle command string: ')
    ShapyTurtle(st)

if __name__ == '__main__':
    main()
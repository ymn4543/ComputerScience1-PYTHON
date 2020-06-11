"""
Youssef Naguib
"""

import turtle as tt


def init(a):
    tt.setworldcoordinates(-a,-a,a,a)
    tt.forward(-a/2)
    tt.color('#009900')
    tt.speed(0)

def DrawTriangleSpiral(a,area=0):
    tt.down()
    while a>0:
        tt.forward(a)
        tt.left(120)
        area+=a
        a -=10
    return area
    
    

def main():
    a = int(input('Please enter length of A:' ))
    init(a)
    print('Total length:',DrawTriangleSpiral(a))

   
if __name__ == '__main__':
    main()

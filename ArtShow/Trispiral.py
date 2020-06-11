import turtle as tt
import random
tt.speed(0)

tt.colormode(255)
tt.bgcolor('black')

def DrawToronto(x,s):
    if x==0:
        pass
    elif x == 1:
        DrawTriangle(s)
        
    elif x > 1:
        DrawPattern(s)
        tt.right(5)
        x-=1
        s+=1
        DrawToronto(x,s)


        
def DrawTriangle(s):
    tt.up()
    tt.right(90)
    tt.forward(s/3.5)
    tt.left(90)
    tt.pensize(1)
    tt.pencolor('light blue')
    tt.down()
    tt.forward(s/2)
    tt.left(120)
    tt.forward(s)
    tt.left(120)
    tt.forward(s)
    tt.left(120)
    tt.forward(s/2)
    tt.up()
    tt.left(90)
    tt.forward(s/3.5)
    tt.right(90)
    

def DrawPattern(s):
    DrawTriangle(s)
    tt.left(90)
    tt.forward(s)
    tt.left(90)
    tt.down()
    tt.pencolor('blue')
    tt.circle(s/4)
    tt.up()
    tt.right(90)
    tt.forward(-s)
    tt.right(180)
    tt.forward(s/3)
    tt.left(90)
    tt.forward(s/2.5)
    tt.right(90)
    tt.down()
    tt.pencolor('white')
    tt.circle(s/4)
    tt.up()
    tt.right(90)
    tt.forward(s/2.5)
    tt.forward(s/2.5)
    tt.right(90)
    tt.down()
    tt.pencolor('blue')
    tt.circle(s/4)
    tt.up()
    tt.right(90)
    tt.forward(s/2.5)
    tt.left(90)
    tt.forward(s/2.5)
    tt.right(90)
    
    
   
    
def main():          
    DrawToronto(185,50)        

if __name__ == "__main__":
    main()



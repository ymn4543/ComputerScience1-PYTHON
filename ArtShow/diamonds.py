import turtle as tt
import random
tt.speed(0)

tt.colormode(255)
tt.bgcolor('black')
tt.pencolor('white')

def DrawToronto(x,s):
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)
    if x==0:
        pass
    elif x == 1:
        DrawSquare(s)
        
    elif x > 1:
        DrawSquare(s)
        tt.left(1)
        tt.pencolor(R,G,B)
        x-=1
        s+=3
        DrawToronto(x,s)
    

        
def DrawSquare(s):
    tt.up()
    tt.right(90)
    tt.forward(s/1.15)
    tt.left(150)
    tt.pensize(1)
    tt.down()
    tt.forward(s)
    tt.left(60)
    tt.forward(s)
    tt.left(120)
    tt.forward(s)
    tt.left(60)
    tt.forward(s)
    tt.up()
    tt.left(150)
    tt.forward(s/1.15)
    tt.right(90)
    

def main():
    DrawToronto(100,75)        



if __name__=="__main__":
    main()
    

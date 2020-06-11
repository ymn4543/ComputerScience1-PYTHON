"""
Youssef Naguib
"""
import turtle as tt


def init(size):
    tt.reset()
    tt.setup(600,600)
    tt.setworldcoordinates(-2*size, -2*size, 2*size, 2*size)
    tt.speed(0)
    tt.up()
    tt.left(180)
    tt.forward(size/2)
    tt.left(90)
    tt.forward(size)
    tt.left(90)



def main():
    init(50)


if __name__ == '__main__':
    main()
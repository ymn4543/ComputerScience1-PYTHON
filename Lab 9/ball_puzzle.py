"""
Ball Puzzle
File: ball_puzzle.py
Author: Youssef Naguib
Language: Python3.7
Description: Lab 9 solution
"""
import ball_animate
from dataclasses import dataclass
from typing import Any, Union
from node import Node
from stack import *

@dataclass
class stack:
    size: Any
    top: Union[None,Node]

def ConvertStringToStack(string):
    """
    This function takes a user input string and creates a stack.
    Pre: string must not be empty
    Post: A stack is made with the last character in the string as its top
          element
    :param string: the user input string that will become a stack
    :return: a stack with values of each character in string
    """
    LL = []
    stack = make_empty_stack()
    for i in string:
        LL.append(i)
    for x in LL:
        push(stack,x)
    return stack

def BallSort(StackR,StackG,StackB):
    """
    This function sorts colored balls into their matching colored cans.
    Pre: only red can stack should have elements, blue and green can strings
         must be empty.
    Post: All balls are stored into their correctly colored cans
    :param StackR is the stack representing the red can.
    :param StackG is the stack representing the green can.
    :param StackB is the stack representing the blue can.
    :return: balls are sorted into place, and number of moves required to sort
             them is returned.
    """
    move_count = 0
    stack_list =[StackR,StackG,StackB]
    if is_empty(StackR) == True:
        raise IndexError('No balls in stack')
    else:
        while StackR.top != None:
            if StackR.top.value == 'R':
                push(StackG, pop(StackR))
                ball_animate.animate_move(stack_list,0,1)
                move_count += 1
            else:
                push(StackB,pop(StackR))
                ball_animate.animate_move(stack_list,0,2)
                move_count += 1
        if StackR.top == None:
            while is_empty(StackG) == False:
                push(StackR,pop(StackG))
                ball_animate.animate_move(stack_list,1,0)
                move_count += 1
        if StackG.top == None:
            while is_empty(StackB) == False:
                if StackB.top.value == 'B':
                    push(StackR,pop(StackB))
                    ball_animate.animate_move(stack_list,2,0)
                    move_count += 1
                else:
                    push(StackG,pop(StackB))
                    ball_animate.animate_move(stack_list,2,1)
                    move_count += 1
        if StackB.top == None:
            while StackR.top.value != 'R':
                push(StackB,pop(StackR))
                ball_animate.animate_move(stack_list,0,2)
                move_count += 1
    return move_count

def main():
    """
    This is the main function, it takes a user input string, turns it into a
    stack, and solves the ball puzzle. It records the number of moves the
    solution required and prints the result.
    Pre: File must be run by user, string must be input and less than 50
         characters.
    Post: Ball puzzle is solved and animated, number of moves required
          is revealed to user.
    """
    Balls = input('Please enter initial balls string:')
    ball_animate.animate_init(Balls)
    StackB = make_empty_stack()
    StackG = make_empty_stack()
    StackR = ConvertStringToStack(Balls)
    moves = BallSort(StackR,StackG,StackB)
    print("The ball puzzle was solved in", moves,'moves!')
    print('Close window to quit.')
    ball_animate.animate_finish()

if __name__ == '__main__':
    main()

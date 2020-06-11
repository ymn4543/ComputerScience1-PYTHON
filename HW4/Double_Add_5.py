"""
Double the start and add five.
file: double_add_5.py
author: Youssef Naguib
language: Python3.7
description: hw 4 solution
"""

def print_sequence_rec(start, count):
    """
    This function recursively generates and prints count*steps of the
    double add five sequence. Values are printed on a single line and
    seperated by a space. Prints starting value as well.
    Pre: start and count must be positive integers.
    Post: The sequence of numbers is printed on a single line.
    :param start: starting value in sequence
    :param count: number of times the sequence is repeated
    """
    if count >= 0:
        print(start, end=" ")
        start = start*2+5
        print_sequence_rec(start, count-1)
    elif count < 0:
        print()


def print_sequence_iter( start, count ):
    """
    This function iteratively generates and prints count*steps of the
    double add five sequence. Values are printed on a single line and
    seperated by a space. Prints starting value as well.
    Pre: start and count must be positive integers.
    Post: The sequence of numbers is printed on a single line.
    :param start: starting value in sequence
    :param count: number of times the sequence is repeated
    """
    while count >= 0:
        print(start, end=" ")
        start = (start*2)+5
        count = count-1
    print()

def find_end_rec(start, count):
    """
    This function recursively generates and returns the last number
    in the double add five sequence, when it starts at "start" and
    is repeated "count" times.
    Pre: start and count must be positive integers.
    Post: The final value in the sequence is returned
    :param start: starting value in sequence
    :param count: number of times the sequence is repeated
    """
    if count == 0:
        return start
    else:
        start = (start*2)+5
        return find_end_rec(start, count-1)

def find_end_iter(start, count):
    """
    This function iteratively generates and returns the last number in the
    double add five sequence, when it starts at "start" and is repeated "count" times.
    Pre: start and count must be positive integers.
    Post: The final value in the sequence is returned
    :param start: starting value in sequence
    :param count: number of times the sequence is repeated
    """
    while count > 0:
        start = (start * 2) + 5
        count = count - 1
    return (start)

def find_start_rec(goal, count, accum=0):
    """
    This function recursively searches forward from an initial value
    of 0 (accum), and returns the smallest integer value that reaches or exceeds the goal.
    Pre: goal must be more than or equal to 0 and count must be more than 0
    Post: the smallest integer value that reaches or exceeds the goal is returned
    :param goal: minimum value that must be reached by an integer in the sequence
    :param count: number of times the sequence is repeated
    :param accum: accumulator that adds 1 each time it is used
    """
    if find_end_rec(accum,count) < goal:
        accum = accum+1
        return find_start_rec(goal,count,accum)
    else:
        return accum

def find_start_iter( goal, count, n=0 ):
    """
    This function iteratively searches forward from an initial value
    of 0 (accum), and returns the smallest integer value that reaches or exceeds the goal.
    Pre: goal must be more than or equal to 0 and count must be more than 0
    Post: the smallest integer value that reaches or exceeds the goal is returned
    :param goal: minimum value that must be reached by an integer in the sequence
    :param count: number of times the sequence is repeated
    :param accum: accumulator that adds 1 each time it is used
    """
    while find_end_iter(n, count) < goal:
        n+=1
        find_start_rec(goal,count)
    return n

def main():
    """
    This function is the main function and gets executed when the program is run.
    """
    test_runs()

def test_runs():
    """
    This function runs different test cases of all the functions in this file.
    This aids in determining if the functions are valid.
    """
    print("Here are a few test cases")
    print_sequence_rec(0, -1)
    print_sequence_rec(0, 0)
    print_sequence_rec(1, 2)
    print_sequence_iter(2, 5)
    print_sequence_rec(1, 0)
    print_sequence_iter(1, 1)
    print_sequence_iter(3, 19)
    print(find_end_rec(100, 3))
    print(find_end_iter(100, 3))
    print(find_end_iter(1, 10))
    print(find_end_rec(2, 40))
    print(find_end_iter(1, 1001))
    print(find_start_rec(7, 3))
    print(find_start_iter(8, 3))
    print(find_start_rec(9, 2))
    print(find_start_iter(100, 1))
    print(find_start_rec(100, 3))
    print(find_end_rec(2018, 4))
    print(find_end_iter(2018, 4))
    print(find_end_iter(88, 14))
    print(find_end_rec(88, 14))
    print(find_end_iter(500, 134))
    print(find_end_rec(500, 134))
    print(find_end_iter(-45, 324))
    print(find_end_rec(-45, 324))
    print(find_start_iter(222, 4))
    print(find_start_rec(222, 4))
    print(find_start_iter(680, 5))
    print(find_start_rec(680, 5))
    print_sequence_rec(-4, 55)
    print_sequence_rec(-4, 55)
    print_sequence_rec(-22, 2.2)
    print_sequence_iter(-22, 2.2)
    print_sequence_rec(4, 83)
    print_sequence_iter(4, 83)
    print(find_end_rec(10, 3))
    print(find_end_iter(10, 3))
    print(find_end_iter(.0291, 40))
    print(find_end_rec(.0291, 40))
    print(find_start_iter(-.655, 5))
    print(find_start_rec(-.655, 5))
    print(find_end_iter(500, 45))
    print(find_end_rec(500, 45))

if __name__== "__main__":
    main()

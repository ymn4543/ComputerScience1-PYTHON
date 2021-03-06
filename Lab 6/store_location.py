"""
quick_sort method implementation
file: store_location.py
author: Youssef Naguib <ymn4543@rit.edu>
language: python3.7
description: Lab 6 solution
"""
import time

def FileList(file):
    """
    This function reads an input text file and converts it into a string of integers.
    pre: parameter must be a valid filename
    post: a list of integers only is created
    :param file: the name of the file used for list. must be inside quotations.
    :return: a list of integers
    """
    with open(file,"r") as f:
        list1 = [r.split()[1] for r in f]
    list1 = [int(i) for i in list1]
    return list1

def median_distance(L):
    """
    Finds the median value in a sorted list of numbers.
    Pre: L must be a sorted list.
    Post: Median value is returned from list.
    :param L: a sorted list
    :return: the median element in the sorted list
    """
    if len(L) % 2 == 0:
        m = (L[len(L)//2] + L[(len(L)//2)-1])/2
    elif len(L) % 2 == 1:
        m = L[len(L)//2]
    return m

def find_sums(lst, m):
    """
    This function calculates the sum of the distances of all the locations
    from the median location.
    Pre: lst must be valid list of numbers only.
    post: Sum of distances from median is returned
    :param lst: a list of numbers
    :param m: the median value
    :return: sum of distances from median value
    """
    sum = 0
    for i in range(0,len(lst)):
        if m > lst[i]:
            sum1 = abs(m - lst[i])
        elif m < lst[i]:
            sum1 = abs(lst[i] - m)
        else:
            pass
        sum += sum1
    return sum

def quick_sort( L ):
    """
    quickSort: List( A ) -> List( A )
        where A is 'totally ordered'
    pre: L parameter must be valid list
    post: a sorted list is returned
    param: L is a list, it does not have to be sorted.
    return: a sorted version of L
    """
    if L == []:
        return []
    else:
        pivot = L[0]
        ( less, same, more ) = partition( pivot, L )
        return quick_sort( less ) + same + quick_sort( more )

def partition( pivot, L ):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    """
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    pre: 2 parameters required, pivot must be 0 or greater, and L must be a
         list.
    post: 3 sub lists of L are created (less than, equal to, and greater than)
    param: pivot is the element being compared to each other element in list.
    param: L is a list (sorted or unsorted)
    return: a tuple of 3 lists is returned
    """
    ( less, same, more ) = ( [], [], [] )
    for e in L:
        if e < pivot:
            less.append( e )
        elif e > pivot:
            more.append( e )
        else:
            same.append( e )
    return (less,same,more)


def main():
    """
    This is the main function which is executed when user runs the program.
    pre: user must run program and input valid filename.
    post: Using values in file, the optimum store location, sum of distances
          of other locations to store, and elapsed time of program are
          calculated and displayed to user.
    """
    list = FileList(input('Enter data file: '))
    start = time.time()
    L = quick_sort(list)
    print('Optimum new store Location:', median_distance(L))
    print('Sum of distances to new store:', find_sums(L,median_distance(L)),'\n')
    end = time.time()
    print('elapsed time:', end-start)
if __name__=='__main__':
    main()

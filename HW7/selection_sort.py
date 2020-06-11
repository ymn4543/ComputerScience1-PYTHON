"""
Selection Sort
file: selection_sort.py
author: Youssef Naguib <ymn4543Grit.edu>
language: python3.7
description: homework 7 solution

Answers to questions:
1. InsertionSort works better in test cases where the list is already partially
sorted, because the iteration requires each index to be less than the index to its
right. It does not go through the while loop until it finds a case where this is true.
SelectionSort on the other hand, iterates for every index even if that index is already
in order.

2. SelectionSort takes up more memory and is more complex. It has a complexity of
O(n(n-1)/2) always. This is the complexity of InsertionSort only at its worst case
scenario, so in most cases it will be more linear and sort the list faster.
"""

def SelectionSort(file1):
    """
    This function takes an unsorted list from a text file and returns the
    same listed sorted.
    Pre: file must contain positive integers, each element must be separated
    by being on its own line. They do not need to be in order
    Post: A sorted list is returned and printed.
    Param: file1 is the text file from which the list will be created
    """
    list1 = FileList(file1)
    print('Unsorted list is:', list1)
    for mark in range(len(list1)-1):
        select(list1,mark)
    print('Sorted list is:',list1)

def swap(lst, i, j):
    """
    This function swaps the elements of the list at index i and j.
    Pre: list must contain positive integers, they do not need to be sorted.
         i and j should be in range of the list
    Post: i and j are swapped in the list, list is returned. It is not a new list,
          just the same list rearranged.
    Param: lst is the list in which the swapping will be done
    Param: i is the next smallest value that will be moved to its proper sorted index
    Param: j is the index of the marker, it is swapped with i each call
   """
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

def select(lst, mark):
    """
    This function finds the smallest element in the list, and calls the swap
    function which puts it in the proper index.
    Pre: list must contain positive integers, they do not need to be sorted.
         mark is initially 0.
    Post: smallest element is sorted into place. mark is increased by 1.
    Param: lst is the list in which the function will select the smallest element
    Param: mark is a marker which tells the function where to put the next minimum value,
           it is increased by 1 each time so that the list is sorted in ascending and not
           descending order.
    Built in function: min finds the minimum element in a list and lst.index
                       returns the index of that element.
    """
    minimum = lst.index(min(lst[mark:]))
    swap(lst,minimum,mark)
    mark += 1

def FileList(file1):
    """
    This function takes a file and transforms it into a list
    Pre: file must be a .txt file and contain positive integers,
         they do not need to be sorted.
         elements must be separated by being on their own line.
    Post: an unsorted list is returned, file is closed.
    Param: file1 is the file that's contents will be transformed into a list
   """
    list1 = [(line.rstrip('\n')) for line in open(file1)]
    return list1
    # numbers from file are in a list, not in order however

def TestSelectionSort():       #This tests The SelectionSort function
    """
    This is a test function for personal testing of the function SelectionSort
    pre: SelectionSort must be called with a proper file as argument.
         filename must be inside '' like a string
    post: SelectionSort function is tested and results may be observed
    """
    SelectionSort('ss.txt')
    SelectionSort('tss1.txt')       # integers only, unsorted
    SelectionSort('tss2.txt')       # integers only, unsorted
    SelectionSort('tss3.txt')       # integers only, sorted
    SelectionSort('tss4.txt')       # integers and floats, unsorted
    SelectionSort('tss5.txt')       # integers and strings, unsorted
    SelectionSort('tss6.txt')       # integers, floats, and strings unsorted

def main():
    """
    This is the main function that will run when the file is executed.
    pre: user input must be valid name of file in directory. Must be .txt file
    post: SelectionSort is run with the input file, unsorted and sorted lists are
          printed.
    """
    file1 = input('Please enter the name of the file: ')
    SelectionSort(file1)

if __name__ == "__main__":
    main()
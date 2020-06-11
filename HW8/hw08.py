"""
File: HW08.py
Author: Youssef Naguib <ymn4543@rit.edu>
Description: HW 8 solution
Language: Python3.7
"""
import random
import time
import merge_sort
import insertion_sort
import quick_sort

def get_list1(n):
    """
    :param n: the length of a list
    :return: a list with random elements (favorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L+[random.random()]
    return L

def get_list2(n):
    """
    :param n: the length of a list
    :return: a list with many repeated elements (favorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L+[random.randint(1,100)]
    return L

def get_list3(n):
    """
    Expected behavior of quick sort: poor
    :param n: the length of a list
    :return: a list of elements increasing overall
    (unfavorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L + [random.random()*i]
    return L

def get_list4(n):
    """
    :param n: the length of a list
    :return: a list with many zeros but neither increasing nor decreasing
    (unfavorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L + [random.randint(-8, 8)*i]
    return L

def test_compare():
    """
    This function compares the length of time each sorting algorithm elapses
    in sorting a list of 10000 elements.
    Pre: function should be called in main function, all 4 sorting algorithms must function properly,
         time library must be imported, and generated lists must contain 10000 random elements.
    Post: results are returned and printed, user may observe which sorting algorithm is the quickest
          in different scenarios and test cases.
    """
    print('Time comparison test begins.\nAll lists used in this test are of length 10000.\n')
    print('Testing with list 1 - random elements')
    lst = get_list1(10000)
    start = time.time()
    sorted_list = insertion_sort.insertion_sort(lst)
    end = time.time()
    print("Insertion sort elapsed time:", end-start, "seconds")
    lst = get_list1(10000)
    start = time.time()
    sorted_list = merge_sort.merge_sort(lst)
    end = time.time()
    print("Merge sort elapsed time:", end-start, "seconds")
    lst = get_list1(10000)
    start = time.time()
    sorted_list = merge_quick_sort(lst)
    end = time.time()
    print("Merge quick sort elapsed time:", end-start, "seconds")
    lst = get_list1(10000)
    start = time.time()
    sorted_list = quick_sort.quick_sort(lst)
    end = time.time()
    print("Quick sort elapsed time:", end-start, "seconds\n")
    print('Testing with list 2 - repeated elements')
    lst = get_list2(10000)
    start = time.time()
    sorted_list = insertion_sort.insertion_sort(lst)
    end = time.time()
    print("Insertion sort elapsed time:", end-start, "seconds")
    lst = get_list2(10000)
    start = time.time()
    sorted_list = merge_sort.merge_sort(lst)
    end = time.time()
    print("Merge sort elapsed time:", end-start, "seconds")
    lst = get_list2(10000)
    start = time.time()
    sorted_list = merge_quick_sort(lst)
    end = time.time()
    print("Merge quick sort elapsed time:", end-start, "seconds")
    lst = get_list2(10000)
    start = time.time()
    sorted_list = quick_sort.quick_sort(lst)
    end = time.time()
    print("Quick sort elapsed time:", end-start, "seconds\n")
    print('Testing with list 3 - overall increasing elements, not favorable to quick sort')
    lst = get_list3(10000)
    start = time.time()
    sorted_list = insertion_sort.insertion_sort(lst)
    end = time.time()
    print("Insertion sort elapsed time:", end-start, "seconds")
    lst = get_list3(10000)
    start = time.time()
    sorted_list = merge_sort.merge_sort(lst)
    end = time.time()
    print("Merge sort elapsed time:", end-start, "seconds")
    lst = get_list3(10000)
    start = time.time()
    sorted_list = merge_quick_sort(lst)
    end = time.time()
    print("Merge quick sort elapsed time:", end-start, "seconds")
    lst = get_list3(10000)
    start = time.time()
    sorted_list = quick_sort.quick_sort(lst)
    end = time.time()
    print("Quick sort elapsed time:", end-start, "seconds\n")
    print('Testing with list 4 -  not favorable to quick sort')
    lst = get_list4(10000)
    start = time.time()
    sorted_list = insertion_sort.insertion_sort(lst)
    end = time.time()
    print("Insertion sort elapsed time:", end-start, "seconds")
    lst = get_list4(10000)
    start = time.time()
    sorted_list = merge_sort.merge_sort(lst)
    end = time.time()
    print("Merge sort elapsed time:", end-start, "seconds")
    lst = get_list4(10000)
    start = time.time()
    sorted_list = merge_quick_sort(lst)
    end = time.time()
    print("Merge quick sort elapsed time:", end-start, "seconds")
    lst = get_list4(10000)
    start = time.time()
    sorted_list = quick_sort.quick_sort(lst)
    end = time.time()
    print("Quick sort elapsed time:", end-start, "seconds\n")
    print('Time comparison test ends.')

def merge_quick_sort(L):
    """
    This is a sorting algorithm that combines quick_sort and merge_sort.
    Pre: the argument must be a list
    Post: list elements are sorted , sorted list is returned
    :param L: the list that will be sorted
    """
    list1 = []
    list2 = []
    (evens, odds) = merge_sort.split(L)
    list1 += quick_sort.quick_sort(evens)
    list2 += quick_sort.quick_sort(odds)
    x = merge_sort.merge(list1,list2)
    return x

def test_merge_quick_sort():
    """
    This function tests the correctness of the merge_quick_sort function.
    Pre: random list must be generated and unsorted list is printed
    Post: list elements are sorted and the sorted list is returned and printed
    """
    print('Testing the correctness of merge_quick_sort: ')
    lst = get_list2(20)
    print('Before Sorted:\n', lst)
    x = merge_quick_sort(lst)
    print('After Sorted:\n',x ,'\n')

def main():
    """
    This is the main function, it is executed when the program is run.
    Pre: program must be run
    Post: merge_quick_sort is tested, and all 4 sorting algorithms are compared in regards
    to how long they take to sort the same list.
    """
    test_merge_quick_sort()
    test_compare()

if __name__ == '__main__':
    main()

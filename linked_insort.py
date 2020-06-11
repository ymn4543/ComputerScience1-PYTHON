"""
file: linked_insort.py
author: Youssef Naguib <ymn4543@rit.edu>
language: Python3.7
description: homework 10 solution
"""
from dataclasses import dataclass
from typing import Any, Union
import linked_code

@dataclass(frozen=True)
class LinkNode:
    """
    A singly linked node structure
    :field value: the element value stored in this node, i.e.,
                  at the head of this sequence
    "field rest: a reference to the next node in the sequence, i.e.,
                 the tail of this sequence
    """
    value: Any
    rest: Union[None, 'LinkNode']

def convert_to_nodes(string):
    """
    This function converts a string into a linked list.
    Pre: parameter must be string
    Post: string converted into linked list.
    :param dna_string: a string
    :return: a linked list
    """
    if string == '':
        return None
    else:
        value = string[0]
        rest = string[1:]
        return LinkNode(int(value), convert_to_nodes(rest))


def insert( value, lnk ):
    """
    Put the value in the proper spot in the linked list to keep it sorted.
    New nodes are created.
    :param value: the value to add to the sequence of values in the list
    :param lnk: the node at the head of the list
    :return: a (partially) new linked list with the value inserted
    :pre: the list headed by lnk is sorted.
    :post: the link returned refers to a list that is sorted.
    """
    if lnk is None or value <= lnk.value:
        return LinkNode(value,lnk)
    else:
        return LinkNode(lnk.value,insert(value,lnk.rest))


def insort( lnk ):
    """
    Return a copy of a linked list where all the values are sorted,
    with the lowest value at the head.
    :param lnk: the node at the head of the provided list
    :return: the head node of the sorted linked list
    """
    SortedList = None
    while lnk is not None:
        SortedList = insert(lnk.value,SortedList)
        lnk = lnk.rest
    return SortedList


def pretty_print( lnk ):
    """
    Print the contents of a linked list in standard Python format.
    [value, value, value] (Note the spaces.)
    :param lnk: the node at the head of the provided list
    :return: None
    """
    list = []
    while lnk is not None:
        list.append(int(lnk.value))
        lnk = lnk.rest
    print(list)

def read_file( fname ):
    """
    Open a file of containing one integer per line,
    prepend each integer to a linked sequence,
    and return the reverse of the sequence.
    :param fname: A string containing the name of the file
    :return: A linked list of the numbers in the file, ordered
            identically to how they are ordered in the file
    """
    list = []
    string = ''
    with open(fname) as f:
        for line in f:
            list.append(line.strip())
    for i in list:
        string+=i
    return convert_to_nodes(string)


if __name__ == '__main__':
    main()
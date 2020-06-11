"""
This file contains recursive functions for DNA structures. (Linked lists)
Author: Youssef Naguib <ymn4543@rit.edu>
File: dna.py
Language: Python3.7
Description: Lab 8 solution
"""
import linked_code
from dataclasses import dataclass
from typing import Any, Union

@dataclass(frozen=True)
class LinkNode:
    """
    An object type to hold any kind of data that can be put into a sequence
    """
    value: any
    rest: Union["LinkNode",None]

def convert_to_nodes(dna_string):
    """
    This function converts a string into a linked list.
    Pre: parameter must be string
    Post: string converted into linked list.
    :param dna_string: a string
    :return: a linked list
    """
    if dna_string == '':
        return None
    else:
        value = dna_string[0]
        rest = dna_string[1:]
        return LinkNode(value, convert_to_nodes(rest))

def is_match(dna_seq1, dna_seq2):
    """
    This function determines whether two linked lists are identical.
    Pre: must be given two parameters, both must be linked lists.
    Post: If the lists are identical function returns True, otherwise
          it will return False.
    :param dna_seq1: linked list
    :param dna_seq2: linked list
    :return: True or False
    """
    if dna_seq1 == None and dna_seq2 == None:
        return True
    if dna_seq1 == None or dna_seq2 == None:
        return False
    if dna_seq1.value == dna_seq2.value:
        return is_match(dna_seq1.rest,dna_seq2.rest)
    else: return False

def insertion(dna_seq1, dna_seq2, idx):
    """
    This function inserts a linked list into another linked list at a chosen
    index.
    Pre: takes three parameters, idx must be integer, dna_seq1 and dna_seq2
         must be linked lists.
    :param dna_seq1: a linked list
    :param dna_seq2: a link list that will be inserted into dna_seq1
    :param idx: the index of dna_seq1 where dna_seq2 will be inserted
    :return:
    """
    if idx == 0:
        return linked_code.concatenate(dna_seq2,dna_seq1)
    if dna_seq1 == None:
        raise IndexError('Invalid insertion error')
    if dna_seq2 == None:
        return dna_seq1
    else:
        return LinkNode(dna_seq1.value,insertion(dna_seq1.rest,dna_seq2,idx-1))


def convert_to_string(dna_seq):
    """
    This function takes a linked list and converts it to a list.
    Pre: dna_seq must be a linked list
    Post: dna_seq is converted to a string and returned
    :param dna_seq: a linked list
    :return: a string
    """
    if dna_seq == None:
        return ''
    else:
        return '' + dna_seq.value + convert_to_string(dna_seq.rest)



def is_pairing(dna_seq1, dna_seq2):
    """
    This function determines whether two linked lists are valid DNA pairs.
    The following are correct pairs: T-->A, A-->T, G-->C, C-->G.
    Pre: dna_seq1 and dna_seq2 must both be valid linked lists
    Post: if both lists are valid pairs, the Function returns True, otherwise,
          it returns False
    :param dna_seq1: a linked list
    :param dna_seq2: a linked list
    :return: True or False
    """
    if dna_seq1 == None and dna_seq2 == None:
        return True
    if dna_seq1 == None or dna_seq2 == None:
        return False
    if dna_seq1.value == 'T':
        if dna_seq2.value == 'A':
            return is_pairing(dna_seq1.rest,dna_seq2.rest)
        else:
            return False
    if dna_seq1.value == 'A':
        if dna_seq2.value == 'T':
            return is_pairing(dna_seq1.rest,dna_seq2.rest)
        else:
            return False
    if dna_seq1.value == 'G':
        if dna_seq2.value == 'C':
            return is_pairing(dna_seq1.rest,dna_seq2.rest)
        else:
            return False
    if dna_seq1.value == 'C':
        if dna_seq2.value == 'G':
            return is_pairing(dna_seq1.rest,dna_seq2.rest)
        else:
            return False

def is_palindrome(dna_seq):
    """
    This function checks if a linked list is a palindrome. A palindrome is a
    list that reads identically in a backwards fashion.
    Pre: dna_seq must be valid linked list
    Post: if dna_seq is a palindrome, the function returns True, otherwise,
          it will return False.
    :param dna_seq: a linked list
    :return: True or False
    """
    reversed = linked_code.reverse_tail_rec(dna_seq)
    if is_match(dna_seq,reversed):
        return True
    else:
        return False

def substitution(dna_seq1, idx, base):
    """
    This function substitutes a value in a linked list with another value.
    Pre: dna_seq must be a linked list, idx must be an integer.
    Post: a new linked list is returned with the substituted value.
    :param dna_seq1: a linked list
    :param idx: index at which substitution occurs
    :param base: value that will replace the one already at the chosen index.
    :return: a linked list with correctly substituted value
    """
    if dna_seq1.value == None:
        return False
    else:
        if idx < 0:
            raise IndexError('Index out of range')
        elif idx == 0:
            dna_seq1 = linked_code.remove_at(idx,dna_seq1)
            dna_seq1 = linked_code.insert_at(idx,base,dna_seq1)
            return dna_seq1
        else:
            return LinkNode(dna_seq1.value,
                            substitution(dna_seq1.rest,idx-1, base))


def deletion(dna_seq, idx, segment_size):
    """
    This function deletes a segment of chosen size, beginning at a chosen
    index, in a linked list.
    Pre: dna_seq must be a linked list, idx must be an integer, and
         segment_size should be an integer.
    Post: a linked list with deleted values is returned
    :param dna_seq: a linked list
    :param idx: index at which deletion occurs
    :param segment_size: size of segment being deleted
    :return: a linked list with a correctly deleted segment
    """
    if segment_size == 0:
        return dna_seq
    elif linked_code.length_rec(dna_seq) < idx + segment_size:
        raise IndexError('Index out of range')
    else:
        if idx == 0:
            dna_seq = linked_code.remove_at(0,dna_seq)
            return deletion(dna_seq,idx,segment_size-1)
        else:
            return LinkNode(dna_seq.value,
                            deletion(dna_seq.rest,idx-1,segment_size))


def duplication(dna_seq, idx, segment_size):
    """
    This function duplicates a segemnt of length segment_size at a chosen
    index in a linked list.
    Pre: dna_seq must be a valid linked list, idx must be an integer, and
         segment_size should be an integer.
    Post: a linked list with duplicated segment in place is returned
    :param dna_seq: linked list
    :param idx: index at which duplicated segment begins
    :param segment_size: length of duplicated segment
    :return: a linked list with correctly duplicated segment in place
    """
    if segment_size == 0:
        return dna_seq
    elif linked_code.length_rec(dna_seq) < idx + segment_size:
        raise IndexError('Index out of range')
    else:
        if idx > 0:
            return LinkNode(dna_seq.value,
                            duplication(dna_seq.rest,idx-1,segment_size))
        if idx == 0:
            dna_seq2 = find_values_sequence(dna_seq,segment_size)
            dna_seq3 = linked_code.concatenate(dna_seq2,dna_seq)
            return dna_seq3


def find_values_sequence(dna_seq, segment_size):
    """
    This is a helper function for the duplication function. It finds and
    returns the segment which will be added into the linked list.
    Pre: dna_seq must be a linked list, while segment_size must be an
         integer
    Post: a segment of length segment_size from dna_seq is returned
    :param dna_seq: a linked list
    :param segment_size: length of segment
    :return: a segment of length segment_size
    """
    if dna_seq is None:
        return dna_seq
    if segment_size == 1:
        x = linked_code.value_at(dna_seq,0)
        return convert_to_nodes(x)
    else:
        x = linked_code.value_at(dna_seq,0)
        return LinkNode(x,find_values_sequence(dna_seq.rest, segment_size-1))
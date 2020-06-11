"""
file: hashtable.py
description: open addressing Hash Table for CS 141 Lecture
language: python3.7
author: RIT CS Instructors
author: Youssef Naguib
"""

from dataclasses import dataclass
from typing import Any, Hashable, Callable

@dataclass
class HashTable:
    """
        The HashTable data structure contains a collection of values
        where each value is located by a hashable key.
        No two values may have the same key, but more than one
        key may have the same value.
        table is the list holding the hash table
        size is the number of elements in occupying the hash table
    """
    table: list
    size: int
    capacity: int
    hash_func: Callable[[Hashable],int] # a function of (Hashable) -> int

@dataclass
class Entry:
    """
       A class used to hold key/value pairs.
    """
    key: Hashable
    value: Any



def create_hash_table(hash_function, capacity):
    """
    create_hash_table: (Func : KT -> NatNum) NatNum? -> HashTable
    """
    if capacity < 2:
        capacity = 2
    table=[]
    for i in range(capacity):
        table.append(None)
    aHashTable = HashTable( table, 0, capacity, hash_function)
    return aHashTable   


def hash_table_to_str(hashtable):
    """
    hash_table_to_str: HashTable -> String
    """
    result = ""
    for i in range(hashtable.capacity):
        e = hashtable.table[i]
        if not e == None:
            result += str(i) + ": "
            result += entry_to_str(e) + "\n"
    return result


def entry_to_str(entry):
    """
    entry_to_str: Entry -> String
    return the string representation of the entry.
    """
    return "(" + str(entry.key) + ", " + str(entry.value) + ")"


def keys(hTable):
    """
    keys: HashTable(K, V) -> List(K)
    Return a list of keys in the given hashTable.
    """
    result = []
    for entry in hTable.table:
        if entry != None:
            result.append(entry.key)
    return result

def has(hTable, key):
    """
    has: HashTable(K, V) K -> Boolean
    Return True iff hTable has an entry with the given key.
    """
    index = hTable.hash_func( key ) % hTable.capacity
    startIndex = index  # We must make sure we don't go in circles.
    while hTable.table[ index ] != None and hTable.table[ index ].key != key:
        index = (index + 1) % hTable.capacity
        if index == startIndex:
            return False
    return hTable.table[ index ] != None

def put(hTable, key, value):
    """
    put: HashTable(K, V) K V -> Boolean

    Using the given hash table, set the given key to the
    given value. If the key already exists, the given value
    will replace the previous one already in the table.
    If the table is full, an Exception is raised.
    """
    if hTable.size / hTable.capacity >= .75:
        resize_hash_table(hTable)
    index = hTable.hash_func(key) % hTable.capacity
    startIndex = index  # We must make sure we don't go in circles.
    while hTable.table[ index ] != None and hTable.table[ index ].key != key:
        index = (index + 1) % hTable.capacity
        if index == startIndex:
            raise Exception("Hash table is full.")
    if hTable.table[ index ] == None:
        hTable.table[ index ] = Entry(key, value)
        hTable.size += 1
    else:
        hTable.table[ index ].value = value
    return hTable

def get(hTable, key):
    """
    get: HashTable(K, V) K -> V

    Return the value associated with the given key in
    the given hash table.

    Precondition: has(hTable, key)
    """
    index = hTable.hash_func(key) % hTable.capacity
    startIndex = index  # We must make sure we don't go in circles.
    while hTable.table[ index ] != None and hTable.table[ index ].key != key:
        index = (index + 1) % hTable.capacity
        if index == startIndex:
            raise Exception("Hash table does not contain key.")
    if hTable.table[ index ] == None:
        raise Exception("Hash table does not contain key:", key)
    else:
        return hTable.table[ index ].value


def resize_hash_table(hTable):
    """
    This function doubles the capacity of a hash table
    pre: hash table more than 74% full
    post: hash table capacity doubled, old items rehashed into new table
    :param hTable: HashTable class
    :return: updated hash table
    """
    tab = []
    OriginalTable = hTable.table
    hTable.capacity = hTable.capacity*2
    hTable.size = 0
    for i in range(0,hTable.capacity):
        tab.append(None)
    hTable.table = tab
    for obj in OriginalTable:
        if obj is not None:
            put(hTable,obj.key,obj.value)
    print('capacity increased to:',hTable.capacity)
    return hTable


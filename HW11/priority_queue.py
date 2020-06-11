"""
Priority Queue
Author: Youssef Naguib <ymn4543@rit.edu>
File: Priority_queue.py
Language: Python3.7
Description: Homework 11 solution
"""

from node import Node
from dataclasses import dataclass
from typing import Any, Union

@dataclass()
class PriorityQueue:
    size: int
    front: Union[None, Node]
    back: Union[None, Node]

def make_priority_queue():
    """
    This Function Makes an empty PriorityQueue.
    Pre: function must be called for a PQ to be made, PQ must be empty with size of 0
    Post: Empty PQ is made with size of 0
    """
    return PriorityQueue(0,None,None)

def enqueue(queue, element):
    """
    This function inserts an element into the correct position in the queue,
    depending on it's priority.
    Pre: function must take a valid priority queue, and a task with a name
         and priority
    Post: task is inserted into correct location in queue, if it has the
          smallest priority it will also become the back.
    Param: queue is the PQ in which the element will be inserted into.
    Param: element is what is being inserted into the PQ, in this case
           it should be a task class with a name and priority.
    """
    queue.size = queue.size + 1
    newnode = Node(element, None)
    if is_empty(queue):
        queue.front = newnode
        queue.back = newnode
    else:
        minimum = queue.back.value.priority
        if newnode.value.priority <= minimum:
            queue.back = newnode
        queue = queue.front
        if queue.value.priority > element.priority:                    # if priority is more than task priority
            while queue.value.priority > element.priority:
                if queue.rest is None or queue.rest.value.priority < element.priority:
                    break
                else:
                    queue = queue.rest
        if queue.value.priority < element.priority:                      #if priority is less than task priority
            y = queue.value
            queue.value = element
            queue.rest = Node(y, queue.rest)
        else:                                                  #otherwise
            x = newnode
            x.rest = queue.rest
            queue.rest = x


def dequeue(queue):
    """
    This function removes and returns the element at the front of the queue.
    Pre: queue must not be empty
    Post: front element of queue is removed and returned
    Param: queue is the PQ in which the element will be removed from.
    """
    if is_empty(queue):
        raise IndexError("dequeue on empty queue")
    removed = queue.front.value
    queue.front = queue.front.rest
    queue.size = queue.size - 1
    return removed

def front(queue):
    """
    This function returns the first element in a queue, does not destruct.
    Pre: queue must not be empty
    Post: front element of queue is returned
    Param: queue is the PQ in which the element will be returned from.
    """
    if is_empty(queue):
        raise IndexError("front on empty queue")
    return queue.front.value

def back(queue):
    """
    This function returns the last(back) element in a queue, does not destruct.
    Pre: queue must not be empty
    Post: back element of queue is returned
    Param: queue is the PQ in which the element will be returned from.
    """
    if is_empty(queue):
        raise IndexError("back on empty queue")
    return queue.back.value

def is_empty(queue):
    """
    This function checks if a queue is empty
    Pre: parameter must be valid queue
    Post: True or False returned
    Param: queue is the queue that is being checked for emptiness.
    """
    return queue.front == None

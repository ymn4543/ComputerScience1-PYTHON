"""
Test file for PriorityQueue
File: tasks.py
Author: Youssef Naguib <ymn4543@rit.edu>
Language: Python3.7
Description: HW 11 solution
"""
import priority_queue
from dataclasses import dataclass
import random

@dataclass()
class Task:
    name: str
    priority: int

def TaskPriority():
    """
    This function generates a priority for a task.
    Pre: function must be called
    Post: a random priority between 1 and 10 is returned
    """
    return random.randint(1,10)

def make_task(x):
    """
    This function makes a task class
    Pre: function must be called
    Post: A task class is created and given a name and priority.
    Param: x is the n'th task. example if x is 5 than the 5th task is made.
    """
    name = 'Task' + str(x)
    priority = TaskPriority()
    return Task(name, priority)



print('TESTING PRIORITY QUEUE:  ')

q = priority_queue.make_priority_queue()
priority_queue.enqueue(q, make_task(1))
priority_queue.enqueue(q, make_task(2))
priority_queue.enqueue(q, make_task(3))
priority_queue.enqueue(q, make_task(4))
priority_queue.enqueue(q, make_task(5))
priority_queue.enqueue(q, make_task(6))
priority_queue.enqueue(q, make_task(7))
priority_queue.enqueue(q, make_task(8))
priority_queue.enqueue(q, make_task(9))
priority_queue.enqueue(q, make_task(10))

print('The PriorityQueue is: ', q)

print('Is the queue empty?', priority_queue.is_empty(q))

t = priority_queue.front(q)
print("Highest priority task is", t.name, "with priority",
      t.priority)
t = priority_queue.back(q)
print("Lowest priority task is", t.name, "with priority",
      t.priority)
print('Tasks in order of highest priority:')
while not priority_queue.is_empty(q):
    t = priority_queue.dequeue(q)
    print(t.name,'with a priority of:',t.priority)


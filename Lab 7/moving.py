"""
Different methods of packing items into boxes, using dataclasses
Author: Youssef Naguib <ymn4543@rit.edu>
File: moving.py
Language: Python3.7
Description: Lab 7 solution
"""
from dataclasses import dataclass

@dataclass
class box:
    max_cap: float
    id: int
    curr_cap: int
    items_list: list

@dataclass
class items:
    name: str
    weight: float

def FillBox(file):
    """
    This function takes a text file and creates 2 lists.
    Pre: Parameter must be valid text file, with box sizes separated by spaces
         in the first line, and each line after containing a name and weight
         of an item.
    Post: 2 lists are made and returned. I_list contains instances
          of the class items, each index has a name and weight assigned.
          box_list is a list of instances of the class box, each index
          contains a maximum capacity, and ID number, a current capacity,
          and a list of the items in the box.
    """
    with open(file,'r') as f:
        info = f.readline().split()
        box_list = []
        id = 1
        I_list =[]
        for i in range(0,len(info)):
            box_list.append(box(float(info[i]),id,0,[]))
            id+=1
        for line in f:
            words = line.split()
            I_list.append(items(words[0], float(words[1])))
    return box_list, I_list

def RoomyStrategy(I_list,box_list):
    """
    This function goes through each item in a list of items sorted by
    decreasing weight, and places it in the box with the most remaining
    space left.
    Pre: 2 lists must be input as parameters, I_list must be a list of
         items and box_list a list of boxes. Dataclasses are used to
         store values.
    Post: The items are stored according to the roomy strategy,
          and the contents of each box are printed along with their
          weights.
    """
    SortedItems = quick_sort(I_list)
    lemon = []
    iso = 0
    for element in range(0, len(SortedItems)):
        w = SortedItems[element].weight
        x = FindMaxCap(box_list)
        if w <= x.max_cap - x.curr_cap:
            x.curr_cap += w
            x.items_list.append(SortedItems[element])
            lemon.append(SortedItems[element])
            iso+=1
        else:
            pass
    print('Results from Greedy Strategy 1')
    if len(SortedItems) == iso:
        print('All items successfully packed into boxes!')
    else:
        print('Unable to pack all items!')
    for box in box_list:
        print('Box',box.id,'of weight capacity',box.max_cap,'contains:')
        for item in box.items_list:
            print(item.name,'of weight',item.weight)
    for item in SortedItems:
        if item not in lemon:
            print(item.name,'of weight',item.weight,'got left behind')
    print('\n')

def TightStrategy(I_list,box_list):
    """
    This function goes through each item in a list of items sorted by
    decreasing weight, and places it in the box with the least remaining
    space left that will fit the item.
    Pre: 2 lists must be input as parameters, I_list must be a list of
         items and box_list a list of boxes. Dataclasses are used to
         store values.
    Post: The items are stored according to the tightest fit strategy,
          and the contents of each box are printed along with their
          weights.
    """
    iso = 0
    lemon = []
    SortedItems = quick_sort(I_list)
    for element in range(0, len(SortedItems)):
        w = SortedItems[element].weight
        x = FindTightFit(box_list, w)
        if x == None:
            iso+=1
            pass
        else:
            if w <= x.max_cap - x.curr_cap:
                x.curr_cap += w
                x.items_list.append(SortedItems[element])
                lemon.append(SortedItems[element])
            else:
                pass
    print('Results from Greedy Strategy 2')
    if iso > 0:
        print('Unable to pack all items!')
    else:
        print('All items were successfully packed!')
    for s in box_list:
        print('Box',s.id,'of weight capacity',s.max_cap,'contains:')
        for item in s.items_list:
            print(item.name,'of weight',item.weight)
    for item in SortedItems:
        if item not in lemon:
            print(item.name,'of weight',item.weight,'got left behind')
    print('\n')

def OneByOneStrategy(I_list,box_list):
    """
    This function goes through each item in a list of items sorted by
    decreasing weight, and iterates through each box, placing items
    until there is no more space in the box for any more.
    Pre: 2 lists must be input as parameters, I_list must be a list of
         items and box_list a list of boxes. Dataclasses are used to
         store values.
    Post: The items are stored according to the One box at a time strategy,
          and the contents of each box are printed along with their
          weights.
    """
    SortedItems = quick_sort(I_list)
    lemon = []
    for i in box_list:
        for item in range(len(SortedItems)):
            if i.max_cap - i.curr_cap == 0:
                break
            if SortedItems[item].weight <= i.max_cap - i.curr_cap:
                if SortedItems[item] not in lemon:
                    lemon.append(SortedItems[item])
                    i.items_list.append(SortedItems[item])
                    i.curr_cap += SortedItems[item].weight
            else:
                pass
    print('Results from Greedy Strategy 3')
    if len(lemon) != len(SortedItems):
        print('Unable to pack all items')
    else:
        print('All items successfully packed!')
    for s in box_list:
        print('Box',s.id,'of weight capacity',s.max_cap,'contains:')
        for item in s.items_list:
            print(item.name,'of weight',item.weight)
    for item in SortedItems:
        if item not in lemon:
            print(item.name,'of weight',item.weight,'got left behind')
    print('\n')

def FindMaxCap(box_list):
    """
    This is a helper function for RoomyStrategy(), it finds the box in
    box_list that has the most space left.
    Pre: parameter must be valid list of instances of class box.
    Post: box with most remaining space is found and returned.
    """
    rem = 0
    for i in range(0,len(box_list)):
        curr = box_list[i].max_cap - box_list[i].curr_cap
        if curr >= rem:
            rem = curr
            box = box_list[i]
        elif curr < rem:
            pass
    return box

def FindTightFit(box_list,w):
    """
    This is a helper function for TightStrategy(), it finds the box in
    box_list that has the least space left, while still having enough space
    for the chosen item.
    Pre: parameters include valid list of instances of class box, and a number
         which represents weight of chosen item (w)
    Post: box with least remaining space that will still fit item of weight
          w is found and returned.
    """
    mini = w
    x = None
    for i in range(0,len(box_list)):
        curr = box_list[i].max_cap - box_list[i].curr_cap
        if curr >= w:
            x = box_list[i]
            rem = curr - w
            if curr > mini:
                mini = rem
                x = box_list[i]
    return x

def quick_sort( L ):
    """
    quickSort: List( A ) -> List( A )
        where A is 'totally ordered'
    """
    if L == []:
        return []
    else:
        pivot = L[0].weight
        (less, same, more ) = partition( pivot, L )
        return quick_sort( more ) + same + quick_sort( less )

def partition( pivot, L ):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    """
    ( less, same, more ) = ( [], [], [] )
    for e in L:
        if e.weight < pivot:
            less.append( e )
        elif e.weight > pivot:
            more.append( e )
        else:
            same.append( e )
    return (less, same, more)

def main():
    """
    This is the main function which is executed when user runs this file.
    Pre: User must run this python file and input a valid .txt file.
    Post: Program will sort items in file into boxes in files using
          three separate strategies, and print the results.
    """
    file = input('Please enter filename: ')
    (box_list, I_list) = FillBox(file)
    RoomyStrategy(I_list, box_list)
    (box_list, I_list) = FillBox(file)
    TightStrategy(I_list,box_list)
    (box_list, I_list) = FillBox(file)
    OneByOneStrategy(I_list,box_list)

if __name__ == '__main__':
    main()
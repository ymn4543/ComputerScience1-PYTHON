"""
file: test_link_sort.py
author: Youssef Naguib <ymn4543@rit.edu>
language: Python3.7
description: tester for functions in linked_insort.py
"""
import linked_insort

def main():
    """
       Read file, build sequence, print it, sort it, print result, and
       pretty-print both lists.
    """

    name = input( "Enter file name: " )
    if name == "":
        return

    original_s = linked_insort.read_file( name )
    print( "unsorted:", original_s )

    sorted_s = linked_insort.insort( original_s )

    print( "sorted:", sorted_s )

    print( "pretty printed original: ", end="")
    linked_insort.pretty_print( original_s )
    print( "pretty printed sorted: ", end="")
    linked_insort.pretty_print( sorted_s )

if __name__ == "__main__":
    main()

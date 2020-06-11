""" 
description: Word Count Program for CSCI 141
file: word_count.py
language: python3.7
author: RIT CS Instructors
"""

from hashtable import *

def word_count( filename ):
    """Report on the frequency of different words in the
       file named by the argument.
    """
    hTable = create_hash_table( hash , 1000 )

    # Read the words of the text file into the word count table.
    with open( filename ) as inFile:
        for line in inFile:
            for word in line.split():
                word = word.strip(",.\"\';:-!?").lower()
                if has( hTable, word ):
                    count = get( hTable, word )
                    put( hTable, word, count + 1 )
                else:
                    put( hTable, word, 1 )
    return hTable

def print_summary( theTable ):
    """
    printSummary : HashTable -> NoneType
    printSummary prints a summary of information about the table contents.
    """

    # Find the most common word in the text file.
    total = 0
    maxWord = ""
    maxCount = 0
    for key in keys( theTable ):
        thisCount = get( theTable, key )
        total += thisCount
        if thisCount > maxCount:
            maxCount = thisCount
            maxWord = key

    print( "There are " + str( len( keys( theTable ) ) ) + " unique words." )
    print( "Total words:", total )
    print( '"' + maxWord + "\" appeared ", str( maxCount ),
           " times, more than any other word." )

def print_table( hTable ):
    """Print the contents of the given hash table.
       Each key/value pair is displayed in parentheses, tuple-style.
       All pairs appear on a single line.
    """
    answer = input( "Do you want to see the entire table?(y/n) " )
    if answer != "y":
        return
    print( "Word Count Data ---------------" )
    ltext = 0
    for key in keys( hTable ):
        txt = "(" + key + "," + str( get( hTable, key ) ) + ")"
        ltext += len( txt )
        if ltext > 51:
            print( txt )
            ltext = 0
        else:
            print( txt, end=" " )
    print()

def main():
    filename = input( "Enter filename: " )
    wordTable = word_count( filename )
    print_summary( wordTable )
    while True:
        print( "Commands: k[ey] <word> f[ind] <word> q[uit] ? ", end=" " )
        response = \
            input( ":- " )
        query = response.split()
        if len( response ) == 0 or not response[0] in "fkq":
            print( response + " invalid. Please enter a command and a word." )
            response = ""
            continue
        if query[0] == "k":
            print( "( " + query[1] + " in text ) is " \
                   + str( has( wordTable, query[1] ) ) + "." )
        if query[0] == "f":
            if has( wordTable, query[1] ):
                print( query[1] + " appears " \
                       + str( get( wordTable, query[1] ) ) + " times." )
            else:
                print( query[1] + " in not in the text." )
        if query[0] == "q":
            break
    # 
    print_table( wordTable )

main()

"""
This is a module file for spellotron.py, it is responsible for the spell
checking functions of strings.
Author: Youssef Naguib <ymn4543@rit.edu>
File: typo.py
Language: Python3.7
Description: CS1 python project soltion
"""

LEGAL_WORD_FILE = 'american-english.txt'
KEY_ADJACENCY_FILE = 'keyboard-letters.txt'
ALPHABET = tuple( chr( code ) for code in range( ord( 'a' ), ord( 'z' ) + 1 ) )

def init():
    """
    This function creates a dictionary of adjacent keys and a list of legal
    english words.
    Pre: function called with correct global constants
    Post: AdjacentKeys dictionary and LegalList list are returned.
    :return:
    """
    AdjacentKeys = {}
    LegalList = set()
    with open(LEGAL_WORD_FILE) as L:
        for line in L:
            LegalList.add(line.strip())
    with open(KEY_ADJACENCY_FILE) as K:
        for line in K:
            line = line.strip()
            AdjacentKeys[line[0]] = line[1:]
    return AdjacentKeys, LegalList

def WrongKey(word,K,L):
    """
    This function attempts to correct a misspelled word by replacing every
    letter with adjacent characters to check if an incorrect key was typed.
    Pre: word must be string
    :param word: a misspelled string
    :return: if the word can be corrected, correct word is returned, otherwise
             the original word is returned.
    """
    org = word
    for chr in range(0,len(word)):
        if word[chr] in K:
            value = K[word[chr]]
            for v in value:
                if v!= ' ':
                    original = word
                    word = word[:chr] + v + word[chr+1:]
                    if word in L:
                        correct = word
                        return correct
                    else:
                        word = original
    return org

def ExtraKey(word,L):
    """
    This function attempts to correct a misspelled word by removing one letter
    each time to check if an extra key was typed.
    Pre: word must be string
    :param word: a misspelled string
    :return: if the word can be corrected, correct word is returned, otherwise
             the original word is returned.
    """
    org = word
    for chr in range(0,len(word)):
        original = word
        word = word[0:chr]+ word[chr+1:]
        if word in L:
            correct = word
            return correct
        else:
            word = original
    return org

def MissingKey(word,L):
    """
    This function attempts to correct a misspelled word by adding each letter
    of the alphabet in each position of the word to check if a key is missing.
    Pre: word must be string
    :param word: a misspelled string
    :return: if the word can be corrected, correct word is returned, otherwise
             the original word is returned.
    """
    org = word
    for chr in range(0,len(word)+1):
        for letter in ALPHABET:
            original = word
            word = word[:chr] + letter + word[chr:]
            if word in L:
                correct = word
                return correct
            else:
                word = original
    return org



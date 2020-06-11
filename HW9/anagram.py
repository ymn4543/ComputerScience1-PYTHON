"""
Author: Youssef Naguib <ymn4543@rit.edu>
File: anagram.py
Language: Python3.7
Description: HW 9 solution
"""

EnglishDictionary = {}

def ListFile(file):
    """
    This function reads through a text file and creates a dictionary of items.
    The file contains words in the english language, each separated by a line.
    The keys are strings of words sorted lexicographically. Each key's value is
    a list containing valid words in the file made up of the same letters.
    Pre: Program must be executed, file must be .txt file
    Post: Dictionary is created with proper keys, values.
    :param file: a valid .txt file
    :return: a dictionary
    """
    with open(file) as f:
        for line in f:
            Words = []
            Wordlist = []
            for chr in line.strip():
                Wordlist += chr
            RealWord = ''
            for element in Wordlist:
                RealWord += element
            word = sorted(Wordlist)
            lex = ''
            for i in word:
                lex += i   #here we have a sorted lexis of the word
            Words.append(RealWord)
            if lex not in EnglishDictionary:
                EnglishDictionary[lex] = Words
            elif lex in EnglishDictionary:
                EnglishDictionary[lex] += Words

def FindAnagrams(string):
    """
    This function takes a user input string and finds all anagrams made up
    from the same letters in the Dictionary. They are returned in a list.
    Pre:input should be string of letters, does not have to be real word.
    Post: A list of anagrams of string is printed, function will run again
          unless user hits enter without putting in a string.
    :param string: a string, does not have to be valid english word.
    :return: list of anagrams of string, all valid words.
    """
    if string != '':
        LexList = []
        lex = ''
        for chr in string:
            LexList.append(chr)
        SortedLex = sorted(LexList)
        for i in SortedLex:
            lex += i
        if lex in EnglishDictionary:
            print('Corresponding words: ',end ='')
            print(EnglishDictionary[lex])
        else:
            print('No words can be formed from:',lex)
        string = input("Enter input string (hit enter key to go to task 3): ")
        FindAnagrams(string)
    else:
        pass

def MaxAnagrams(n):
    """
    This function takes a user input integer for length of a word and finds
    the maximum amount of anagrams that can be formed with any key of that
    length.
    Pre:input should be an integer not a float or string
    Post: the max anagrams possible for the length is printed, along with
          a list of those anagrams.The function will run again unless
          user hits enter without putting in a string.
    :param n: an integer representing length of word
    :return: maximum amount of anagrams possible(int) with that word length,
             and list of the anagrams.
    """
    if n != '':
        n = int(n)
        max = 0
        word = []
        ListWord = []
        for key in EnglishDictionary.keys():
            for chr in key:
                word.append(chr.strip(''))
            if len(word) != n:
                word.clear()
            else:
                x = EnglishDictionary[key]
                if len(x) > max:
                    max = len(x)
                    ListWord = EnglishDictionary[key]
        print('Max Anagrams for length',n,':',max)
        print('anagram list:',ListWord)
        n = (input('Enter word length (hit enter to go to task 4): '))
        MaxAnagrams(n)
    elif n == ' ':
        pass

def JumbleWords(x):
    """
    This function takes a user input integer for length of a word and finds
    the  amount of keys of equal length that only have one combination.
    These words are called good Jumble words
    Pre:input should be an integer not a float or string
    Post: the number of good jumble words with equal length of x
          in the dictionary is printed. Function will run again unless
          user hits enter to end program.
    :param x: an integer representing length of word
    :return: number of good jumble words with length x (int)
    """
    if x == '':
        pass
    else:
        x = int(x)
        word = []
        sum = 0
        for key in EnglishDictionary.keys():
            for chr in key:
                word.append(chr.strip())
            if len(word) == x:
                if len(EnglishDictionary[key]) == 1:
                    sum += 1
            else:
                word.clear()
        print("Number of jumble usable words of length",x,':',sum)
        x = input('Enter word length (hit enter to quit): ')
        JumbleWords(x)

def main():
    """
    This is the main function that is executed when user runs the program.
    It contains four sub-functions that perform different tasks.
    1. A dictionary is created from the file 'american-english.txt'
    2. All anagrams of user input string are found
    3. Maximum anagrams of user input length are found
    4. Maximum good Jumble words of user input length are found
    These functions will repeat themselves  until user hits enter to
    move to the next. Program ends after fourth function.
    Pre: Program must be run by user, functions require valid inputs.
    Post: Functions return and print correct results.
    """
    ListFile('american-english.txt')
    string = input("Enter input string (hit enter key to go to task 3): ")
    FindAnagrams(string)
    n = input('Enter word length (hit enter to go to task 4): ')
    MaxAnagrams(n)
    x = int(input('Enter word length (hit enter to quit): '))
    JumbleWords(x)

if __name__ == '__main__':
    main()
"""
Computer Science 1 Final Project: Spelling corrector
Author: Youssef Naguib <ymn4543@rit.edu>
File: spellotron.py
Language: Python3.7
Description: Final project solution
"""
import sys
import typo
modes = {'words','lines'}

K,L = typo.init()
LA = tuple(chr(code) for code in range(ord('a'),ord('z')+1))
UA = tuple(chr(code) for code in range(ord('A'),ord('Z')+1))

def SpellCheck(word):
    """
    This function corrects typos due to wrong keys typed, extra keys typed, or
    missing keys in words.
    Pre: word must be a string
    Post: Corrected word is returned, if the word cannot be corrected the
    original is returned.
    :param word: a string with a typo
    """
    original = word
    word = typo.WrongKey(word,K,L)
    if word != original:
        return word
    else:
        word = typo.MissingKey(word,L)
        if word != original:
            return word
        else:
            word = typo.ExtraKey(word,L)
            if word != original:
                return word
    return original

def ModeOneOperations(WordList):
    """
    This is a function that runs operations to fulfill the user chosen "words"
    mode.
    Pre: WordList must be a list of strings
    Post: Words in WordList are corrected if possible and stored in a
          dictionary, unknown words are placed in a list
    :param WordList: A list of strings
    :return:A Dictionary of changed words with keys as original and values as
            Corrected words. Additionally, a list of unknown words is returned.
    """
    ChangedWords = {}
    UnknownWords = []
    for word in WordList:
        prepunc = ''
        postpunc = ''
        if word.isdigit() is True or word in L:
            pass
        else:
            while word[0] not in UA and word[0] not in LA:
                prepunc += word[0]
                word = word[1:]
            while word[-1] not in UA and word[-1] not in LA:
                postpunc += word[-1]
                word = word[:-1]
            if word in L:
                pass
            case = word
            word = word.lower()
            if word in L:
                pass
            elif word not in L:
                result = SpellCheck(word)
                if result in L:
                    ChangedWords[prepunc + case + postpunc] = prepunc + result + postpunc
                else:
                    UnknownWords.append(prepunc + case + postpunc)
    return ChangedWords, UnknownWords


def ModeTwoOperations(WordList):
    """
    This is a function that runs operations to fulfill the user chosen "lines"
    mode.
    Pre: WordList must be a list of strings
    Post: Words in WordList are corrected if possible and stored in a
          corrected words list, unknown words are placed in another list.
    :param WordList: A list of strings
    :return: A list of corrected words. Additionally, a list of unknown words.
        Finally, a corrected version of WordList is returned as CorrectList.
    """
    CorrectList = []
    CorrectedWords = []
    UnknownWords = []
    for word in WordList:
        prepunc = ''
        postpunc = ''
        if word.isdigit() is True or word in L:
            CorrectList.append(word)
        else:
            while word[0] not in UA and word[0] not in LA:
                prepunc += word[0]
                word = word[1:]
            while word[-1] not in UA and word[-1] not in LA:
                postpunc += word[-1]
                word = word[:-1]
            if word in L:
                CorrectList.append(prepunc + word + postpunc)
            else:
                case = word
                word = word.lower()
                if word in L:
                    CorrectList.append(prepunc+case+postpunc)
                elif word not in L:
                    result = SpellCheck(word)
                    if result in L:
                        CorrectedWords.append(prepunc+word+postpunc)
                        CorrectList.append(prepunc + result + postpunc)
                    else:
                        UnknownWords.append(prepunc + word + postpunc)
                        CorrectList.append(word)
    return CorrectList,CorrectedWords,UnknownWords


def WordFileOperations(file):
    """
    This is a function that runs operations to fulfill the user chosen "words"
    mode, if the user has also input a filename.
    Pre: file must be a correct .txt file in the directory. should be str
    Post: ModeOneOperations is preformed on each line in the file.
    :param File: a filename
    """
    MasterCW = {}
    MasterUW = []
    MasterWL = 0
    CoList = []
    cw = 0
    with open(file) as f:
        for line in f:
            WordList = line.split()
            MasterWL += len(WordList)
            ChangedWords, UnknownWords = ModeOneOperations(WordList)
            for word in ChangedWords:
                cw += 1
                MasterCW[word] = ChangedWords[word]
            for word in UnknownWords:
                MasterUW.append(word)
    for word in MasterCW:
        print(word,'-->',MasterCW[word])
        CoList.append(word)
    print('\n')
    print(MasterWL,'words read from file.')
    print('\n')
    print(cw,' Corrected Words')
    print(CoList)
    print('\n')
    print(len(MasterUW), 'Unknown Words')
    print(MasterUW)


def LineFileOperations(file):
    """
    This is a function that runs operations to fulfill the user chosen "lines"
    mode, if the user has also input a filename.
    Pre: file must be a correct .txt file in the directory. should be str
    Post: ModeTwoOperations is preformed on each line in the file.
    :param file: a filename
    """
    s = ' '
    MasterCW = []
    MasterUW = []
    wr = 0
    with open(file) as f:
        for line in f:
            WordList = line.split()
            CorrectList,CorrectedWords,UnknownWords = ModeTwoOperations(WordList)
            print(s.join(CorrectList))
            wr += len(CorrectList)
            for word in CorrectedWords:
                MasterCW.append(word)
            for word in UnknownWords:
                MasterUW.append(word)
    print('\n')
    print(wr,"words read from file.")
    print('\n')
    print(len(MasterCW),' Corrected Words')
    print(MasterCW)
    print('\n')
    print(len(MasterUW),' Unknown Words')
    print(MasterUW)


def main():
    """
    This is the main function which runs console operations depending on user
    input into the terminal.
    Input should be entered as follows:
    for file:
    python spellotron.py mode filename
    for user input:
    python spellotron.py mode
    enter input
    """
    s = ' '
    if sys.argv[1] not in modes:
        print('Usage: Python3.7 Mode1/Mode2 [Filename]')
    else:
        if sys.argv[1] == 'words':
            if len(sys.argv) > 2:
                print('Processing file ',sys.argv[2])
                WordFileOperations(sys.argv[2])
            else:
                WordList = sys.stdin.readline().split()
                ChangedWords, UnknownWords = ModeOneOperations(WordList)
                print(s.join(WordList))
                cw = 0
                altered = []
                for word in ChangedWords:
                    altered.append(word)
                    cw += 1
                    print(word,'-->',ChangedWords[word])
                print('\n')
                print(len(WordList),'words read from file.')
                print('\n')
                print(cw,'Corrected Words')
                print(altered)
                print('\n')
                print(len(UnknownWords),'Unknown Words')
                print(UnknownWords)
        else:
            if len(sys.argv) > 2:
                print('Processing file ',sys.argv[2])
                LineFileOperations(sys.argv[2])
            else:
                WordList = sys.stdin.readline().split()
                CorrectList,CorrectedWords,UnknownWords = ModeTwoOperations(WordList)
                print(s.join(CorrectList),'\n')
                print(len(CorrectedWords),'Corrected Words.')
                print(CorrectedWords,'\n')
                print(len(UnknownWords),'Unknown Words.')
                print(UnknownWords)

if __name__ == '__main__':
    main()

"""
Compares two text files
File: file_compare.py
Author: Youssef Naguib
Language: Python3.7
Description: hw 5 solution
"""

def char_by_char(file1,file2):
    """
    This function compares two files line by line and returns the number of lines of
    different length, the number of characters in each file, the number of unmatched characters,
    and where they are in (Line:character) format.
    :param file1: the first file that will be compared
    :param file2: the second file that will be compared
    Pre: User inputs two files and this function takes them as parameters
    Post: The function compares the two files and prints the appropriate information.
    Variable: A, is the first file, opened
    Variable: B, is the second file, opened
    Variable: CharactersA, is the number of characters in first file (A)
    Variable: CharactersB, is the number of characters in second file (B)
    Variable: LineNumber, is the number of lines read so far by the function
    Variable: UnMatchedC, is the number of unmatched characters
    Variable: UnMatchedC, is the number of unmatched characters
    Variable: UnMatchedL, is the number of lines of different length
    Variable: UnMatchedN, is the position of unmatched characters in the files.
    :return:
    """
    A = open(str(file1))
    B = open(str(file2))
    CharactersA = 0
    CharactersB = 0
    LineNumber = 0
    UnMatchedC = 0
    UnMatchedL = 0
    UnMatchedN = ""
    for line in range(0,10):
        LineA = A.readline()
        LineB = B.readline()
        LineNumber += 1
        if LineA == LineB:
            CharactersA += len(LineA.strip())
            CharactersB += len(LineB.strip())
            continue
        elif LineA != LineB:
                CharactersA += len(LineA.strip())
                CharactersB += len(LineB.strip())
                if len(LineA.strip()) == len(LineB.strip()):
                    for x in range(0,len(LineA)):
                        if LineA[x] != LineB[x]:
                                UnMatchedC += 1
                                UnMatchedN = UnMatchedN + str(LineNumber) + ':' + str(x+1) + ","
                else:
                    UnMatchedL += 1
                    UnMatchedN += str(LineNumber)
    A.close()
    B.close()
    print("Character by character: ")
    print("Unmatched Characters:", UnMatchedN)
    print('There are', CharactersA,'characters in', file1)
    print('There are', CharactersB,'characters in', file2)
    print('There were',UnMatchedC,'unmatched characters in the files.')
    print('There were',UnMatchedL,'lines of different length.')

def main():
    """
    This is the main function that is executed when the program is run. It
    takes two user inputs for files that will be compared and runs them through
    the function char_by_char(file1,file2).
    Pre: Program is run, user input is asked and user enters valid file names.
    Post: char_by_char function is run and the two chosen files are compared.
    """
    file1 = input("Please enter the name of file 1: ")
    file2 = input("Please enter the name of file 2: ")
    char_by_char(file1,file2)

if __name__ == '__main__':
    main()



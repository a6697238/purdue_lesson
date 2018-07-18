#
# CS 177 – labprep7.py
# {NICK YUNING CUI}
# this programme prompts the user for two (2) filenames, (a ‘words’ file and a ‘search’ file). Then, after reading a sequence of individual words
# from the words file, the program searches through the search file to find occurrences of each word. The
# words and the line numbers where they are found are stored in a new List and returned by the program

from graphics import *


def main():
    word_file = str(input('Enter words filename:'))
    search_file = str(input('Enter search filename: '))
    wordList = words(word_file)
    search(search_file, wordList)


# words() function return the word of the file
def words(wordFileName):
    file = open(wordFileName)
    wordList = []
    for line in file:
        wordStr = line.strip()
        wordStr = ''.join([x.lower() for x in wordStr if (x.isalpha() or x == ' ')])
        wordStr = wordStr.split(" ")
        for x in wordStr:
            wordList.append(x)
    file.close()
    return wordList

# search() function return the line location of the searchFileName
def search(searchFileName, wordList):
    resultMap = {}
    for word in wordList:
        tempList = []
        tempList.append(word)
        resultMap[word] = tempList

    file = open(searchFileName)
    occurrences = []
    num_count = 0
    for line in file:
        num_count = num_count + 1;
        wordStr = line.strip()
        wordStr = ''.join([x.lower() for x in wordStr if (x.isalpha() or x == ' ')])
        wordStr = wordStr.split(" ")
        for x in wordStr:
            if x in wordList:
                resultMap[x].append(num_count)
    file.close()
    for (k, v) in resultMap.items():
        occurrences.append(v)
    return occurrences


main()

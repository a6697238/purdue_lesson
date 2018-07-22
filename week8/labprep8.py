#
# CS 177 – labprep8.py
# {NICK YUNING CUI}
# This programme prompts the user for filename and creates a dictionary
# of the characters contained in the file and their number of occurrences


def main():
    filename = str(input('Enter filename:'))
    print(count(filename))


# count() function  Return the char count completed Dictionary
def count(fileName):
    file = open(fileName)
    wordDict = {}
    for line in file:
        wordStr = line.strip()
        for charItem in wordStr:
            if (wordDict.__contains__(charItem)):
                 wordDict[charItem] = wordDict[charItem] + 1
            else:
                wordDict[charItem] = 1
    file.close()
    return wordDict



main()

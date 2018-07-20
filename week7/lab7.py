#
# CS 177 – lab7.py
# {NICK YUNING CUI}
# this programme reads a series of 'sequences' from a file
# and searches a 'source' file for matching occurrences
#
# The sequences may include the following wildcards:
#          '$'       Representing any single character
#          '*'       Representing any number of characters
#

from graphics import *


def main():
    seqList, sourceList = read()
    occurrences = search(seqList, sourceList)
    display(occurrences)

def display(occurrences):
    place = " "*30
    place_str = '%s'+place+'%s'+place+'%s'+place+'%s'+place+'%s'+place;
    print("====================================================================================================================")
    print("Seq"+place+"Match"+place+"Line"+place+"Pos"+place+"Snippet")
    print("====================================================================================================================")
    for occurrence in occurrences:
        for i in occurrence:
            print(place_str %(i[0],i[1],i[2],i[3],i[4]))


# read() function return the source list and  seq list
def read():
    print("this programme reads a series of 'sequences' from a file")
    print("and searches a 'source' file for matching occurrences")
    print("The sequences may include the following wildcards:")
    print("'$'       Representing any single character")
    print("'*'       Representing any number of characters")
    print("====================================================================================================================")
    seq_file = str(input('Enter the sequences filename: '))
    file = open(seq_file)
    seqList = []
    for line in file:
        seqStr = line.strip()
        seqStr = ''.join([x.lower() for x in seqStr if (x.isalpha() or x == ' ' or x == '*' or x == "$")])
        seqStr = seqStr.split(" ")
        for x in seqStr:
            seqList.append(x)
    file.close()

    source_file = str(input('Enter the source filename: '))
    file = open(source_file)
    sourceList = []
    for line in file:
        line_list = []
        sourceStr = line.strip()
        wordStr = ""
        for s in range(0, len(sourceStr)):
            if sourceStr[s] == '-':
                wordStr = wordStr + " "
            else:
                wordStr = wordStr + sourceStr[s]
        sourceStr = wordStr
        sourceStr = ''.join([x.lower() for x in sourceStr if (x.isalpha() or x == ' ' or x == '*' or x == "$")])
        sourceStr = sourceStr.split(" ")
        for x in sourceStr:
            line_list.append(x)
        sourceList.append(line_list)
    file.close()
    return seqList, sourceList


# search() function return the line location of
def search(seqList, sourceList):
    occurrences = []
    for seq in seqList:
        for idx in range(0, len(sourceList)):
            occurrence = searchContent(seq, sourceList[idx], idx + 1)
            if (len(occurrence) > 0):
                occurrences.append(occurrence)
    return occurrences


# searchContent() function return the search type of  wildcard character
def searchContent(seq, content, lineNum):
    if seq.find("$") == 0:
        return searchBeforeOne(seq, content, lineNum)
    elif seq.find("$") > 0:
        return searchAfterOne(seq, content, lineNum)
    elif seq.find("*") == 0:
        return searchBeforeAny(seq, content, lineNum)
    elif seq.find("*") > 0:
        return searchAfterAny(seq, content, lineNum)
    return []


# searchAfterOne() function return the result  like aaa$
def searchAfterOne(seq, content, lineNum):
    occurrences = []
    seq_m = seq[0:-1]
    for idx in range(0, len(content)):
        if seq_m in content[idx] and len(content[idx]) == len(seq):
            occurrence = []
            occurrence.append(seq)
            occurrence.append(content[idx])
            occurrence.append(lineNum)
            occurrence.append(idx)
            occurrence.append(content[idx] + " " + content[idx + 1])
            occurrences.append(occurrence)
    return occurrences


# searchBeforeOne() function return the result  like $aaa
def searchBeforeOne(seq, content, lineNum):
    occurrences = []
    seq_m = seq[1:]
    for idx in range(0, len(content)):
        if seq_m in content[idx] and len(content[idx]) == len(seq):
            if content[idx].find(seq_m) > 0 and (content[idx].find(seq_m) + len(seq_m)==len(content[idx])):
                occurrence = []
                occurrence.append(seq)
                occurrence.append(content[idx])
                occurrence.append(lineNum)
                occurrence.append(idx + 1)
                occurrence.append(content[idx - 1] + " " + content[idx])
                occurrences.append(occurrence)
    return occurrences


# searchAfterAny() function return the result  like aaa*
def searchAfterAny(seq, content, lineNum):
    occurrences = []
    seq_m = seq[0:-1]
    for idx in range(0, len(content)):
        if seq_m in content[idx] and content[idx].find(seq_m)==0:
            occurrence = []
            occurrence.append(seq)
            occurrence.append(content[idx])
            occurrence.append(lineNum)
            occurrence.append(idx)
            occurrence.append(content[idx] + " " + content[idx + 1])
            occurrences.append(occurrence)
    return occurrences


# searchBeforeAny() function return the result  like *aaa
def searchBeforeAny(seq, content, lineNum):
    occurrences = []
    seq_m = seq[1:]
    for idx in range(0, len(content)):
        if seq_m in content[idx]:
            if content[idx].find(seq_m) > 0 and (content[idx].find(seq_m) + len(seq_m)==len(content[idx])):
                occurrence = []
                occurrence.append(seq)
                occurrence.append(content[idx])
                occurrence.append(lineNum)
                occurrence.append(idx + 1)
                occurrence.append(content[idx - 1] + " " + content[idx])
                occurrences.append(occurrence)
    return occurrences

main()

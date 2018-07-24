#
# CS 177 – lab8.py
# {NICK YUNING CUI}
# This programme prompts the user for filename and creates a file analyze map
# analyze contains word, sentence and character of the file




def main():
    filename = str(input('Enter filename:'))
    sentence_list = read(filename)
    sentence_result = sentenceAnalyze(sentence_list)
    word_result = wordAnalyze(sentence_list)
    character_result = characterAnalyze(sentence_list)

    for key in  sentence_result:
        print(key + " : ", end=' ')
        print(sentence_result[key])
    for key in word_result:
        print(key + " : ", end=' ')
        print(word_result[key])
    for key in character_result:
        print(key + " : ", end=' ')
        print(character_result[key])

# read() function  Return the file sentence list
def read(fileName):
    sentence_list = []
    sentence = []
    file = open(fileName)
    for line in file:
        for word in line.split(" "):
            if(word=='\n'):
                continue
            if(word.find('.')>-1):
                sentence.append(word)
                sentence_list.append(sentence)
                sentence = []
            else:
                sentence.append(word)
    file.close()
    return sentence_list

# sentenceAnalyze() function  Return sentence analyze result of the file
def sentenceAnalyze(sentence_list):
    sentenceAnalyze = {}
    sentenceAnalyze['sentence count'] = len(sentence_list)
    longest = 0
    longest_sentence = ""
    shortest = 99999
    shortest_sentence=""
    for sentence in sentence_list:
        if(len(sentence)>longest):
            longest = len(sentence)
            longest_sentence = (" ").join(sentence)
        if(len(sentence)<shortest):
            shortest = len(sentence)
            shortest_sentence = (" ").join(sentence)
    sentenceAnalyze['longest_sentence'] = longest_sentence
    sentenceAnalyze['shortest_sentence'] = shortest_sentence
    return sentenceAnalyze


# wordAnalyze() function  Return word analyze result of the file
def wordAnalyze(sentence_list):
    wordAnalyze = {}
    totalNum = 0
    wordMap = {}
    uniqueSet = set()
    for sentence in sentence_list:
        for word in sentence:
            totalNum = totalNum +1
            if(wordMap.__contains__(word)):
                wordMap[word] = 1 + wordMap[word]
            else:
                wordMap[word] = 1

    for word in wordMap:
        wordLen = 0
        maxWordLen = 0
        if(wordMap[word]==1):
            uniqueSet.add(word)
        for charItem in word:
            wordLen = wordLen + 1
            if(wordLen>maxWordLen):
                maxWordLen = wordLen


    maxWordList = []
    for i in range(0,5):
        maxWord = max(wordMap, key=wordMap.get)
        maxWordList.append(maxWord)
        maxWordList.append(str(round(wordMap[maxWord]/totalNum * 1.0 * 100,2)) + '%')
        wordMap.pop(maxWord)

    wordAnalyze['totalWordNum'] = totalNum
    wordAnalyze['uniqueWordSet'] = uniqueSet
    wordAnalyze['maxWordLen'] = maxWordLen
    wordAnalyze['maxWordList'] = maxWordList

    return wordAnalyze


# characterAnalyze() function  Return character analyze result of the file
def characterAnalyze(sentence_list):
    characterAnalyze = {}
    characterMap = {}
    uniqueCharacterSet = set()
    characterCount = 0
    for sentence in sentence_list:
        for word in sentence:
            for character in word:
                if(characterMap.__contains__(character)):
                    characterMap[character] = characterMap[character] + 1
                else:
                    characterMap[character] = 1

    for key in characterMap:
        characterCount = characterMap[key] + characterCount
        if(characterMap[key]==1):
            uniqueCharacterSet.add(key)

    characterAnalyze['characterCount']=characterCount
    characterAnalyze['uniqueCharacterSet']=uniqueCharacterSet
    return characterAnalyze

main()

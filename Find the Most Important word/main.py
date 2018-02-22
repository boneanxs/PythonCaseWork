import re
import collections
import os

stop_words = []
def getStopWords(filePath):
    global stop_words
    with open(filePath,'r') as f:
        line = f.readline()
        while line:
            stop_words.append(line.replace('\n',''))
            line = f.readline()
    pass
def findWords(filePath):
    wordsList = []
    wordsCounts = {}
    global stop_words
    with open(filePath,'r') as f:
        isEnd = 0
        while isEnd == 0:
            line = f.readline().lower()
            if line == '':
                isEnd = 1
                continue
            tempList = re.split(r'[^a-zA-Z\-]',line)
            for item in tempList:
                if (len(item) == 1) or item in stop_words:
                    continue
                if item not in wordsList:
                    wordsList.append(item)
                    wordsCounts[item] = 1
                else:
                    wordsCounts[item] = wordsCounts[item] + 1
            pass
    word = ''
    count = 0
    for key in wordsCounts.keys():
        if count < wordsCounts[key]:
            word = key
            count = wordsCounts[key]
    return word, count
if __name__ == '__main__':
    getStopWords(r'E:/PythonCaseWork/Find the Most Important word/stopWords.txt')
    paths = [os.path.join(r,fileName) for r,d,f in os.walk(r'E:/PythonCaseWork/Find the Most Important word/Notes') for fileName in f]
    for path in paths:
        word,count = findWords(path)
        print('the file ' + path + ' most important word is ' + word + ', the count is ' + str(count))
    

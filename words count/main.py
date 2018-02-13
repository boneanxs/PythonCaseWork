import re


wordsList = []
wordsCounts = {}
with open(r'E://PythonCaseWork/words count/text.txt','r') as f:
    isEnd = 0
    while isEnd == 0:
        line = f.readline().lower()
        if line == '':
            isEnd = 1
            continue
        tempList = re.split(r'[^a-zA-Z\-]',line)
        for item in tempList:
            if len(item) == 1:
                continue
            if item not in wordsList:
                wordsList.append(item)
                wordsCounts[item] = 1
            else:
                wordsCounts[item] = wordsCounts[item] + 1
        pass
print(wordsCounts)

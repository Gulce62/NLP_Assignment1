import os
import re
import nltk


def readTxtFile(filePath):
    # read a txt file with the given path
    with open(filePath, 'r', encoding='utf8', errors='ignore') as f:
        txtFile = f.read()
    return txtFile


def writeTxtFile(filePath, text):
    # write into a txt file with the given text
    with open(filePath, 'w', encoding='utf8', errors='ignore') as f:
        f.truncate(0)
        f.write(text)


def tokenize(text):
    # get rid of every punctuation marks
    text = re.sub(r'[^\w\s]|_', '', text)  # TODO maybe you can divide to '' and ' '
    # cast every word to lowercase
    words = text.lower().split()
    text = ' '.join(words)
    freqDict = createFrequencyDict(words)
    return text, freqDict


def getStopWordsList():
    nltk.download('stopwords')
    stopWords = nltk.corpus.stopwords.words('english')
    for w in range(len(stopWords)):
        word = stopWords[w].replace("'", "")
        stopWords[w] = word
    return stopWords


def removeStopWords(text, stopWords):
    words = text.split()
    removedWords = [word for word in words if word not in stopWords]
    removedText = ' '.join(removedWords)
    freqDict = createFrequencyDict(removedWords)
    return removedText, freqDict


def createFrequencyDict(words):
    freqDict = {}
    for word in words:
        if word in freqDict:
            freqDict[word] += 1
        else:
            freqDict[word] = 1
    return freqDict


stopWords = getStopWordsList()

directoryPath = r'Books'
tokenizedPath = r'TokenizedBooks'
stopRemovedPath = r'StopRemovedBooks'

tokenizedFrequencies = []
stopRemovedFrequencies = []

for book in os.listdir(directoryPath):
    bookPath = os.path.join(directoryPath, book)
    tokenizedBookPath = os.path.join(tokenizedPath, book)
    stopRemovedBookPath = os.path.join(stopRemovedPath, book)

    txtBook = readTxtFile(bookPath)

    tokenizedText, tokenizedFreqDict = tokenize(txtBook)
    writeTxtFile(tokenizedBookPath, tokenizedText)
    tokenizedFrequencies.append(tokenizedFreqDict)

    stopRemovedText, stopRemovedFreqDict = removeStopWords(tokenizedText, stopWords)
    writeTxtFile(stopRemovedBookPath, stopRemovedText)
    stopRemovedFrequencies.append(stopRemovedFreqDict)


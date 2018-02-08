# -*- coding: utf-8 -*-
import numpy as np

def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec


def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


def setOfWord2Vec(vocabList,inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print("the word: %S is not in my Vocabulary!"%word)
    return returnVec


def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix) #How many sentence vector, the train set has 
    numWords = len(trainMatrix[0])  #How many word in each sentence vector
    pAbusive = sum(trainCategory) / float(numTrainDocs) #probabilty of abused word class, 3/6
    p0Num = np.ones(numWords)
    p1Num = np.ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1 :
            p1Num += trainMatrix[i] #If the sentense including the abused word, each word of the whole vocabulary appeared times 
            p1Denom += sum(trainMatrix[i]) #If the sentense including the abused word, the sum of appeared word 
        else:
            p0Num +=trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = np.log(p1Num/p1Denom) #log, monotonically increasing,calculate, if the sentence is abused, the probability of each word on total number of word, p(w1|c1)
    p0Vect = np.log(p0Num/p0Denom) #p(w1|c1)
    return p0Vect,p1Vect,pAbusive
    
def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    print(vec2Classify)
    print(p1Vec)
    p1 = sum(vec2Classify*p1Vec) + np.log(pClass1)    # This testing sentense, the P(W1|C1)*P(W2|C1)....
    p0 = sum(vec2Classify*p0Vec) + np.log(1.0 - pClass1)
    if p1>p0:
        return 1
    else:
        return 0
    
def testingNB():
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWord2Vec(myVocabList,postinDoc))
    p0V,p1V,pAb = trainNB0(trainMat,listClasses)
    testEntry = ['love','my','dalmation']
    thisDoc = np.array(setOfWord2Vec(myVocabList,testEntry))
    print(testEntry,'classified as: ', classifyNB(thisDoc,p0V,p1V,pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = np.array(setOfWord2Vec(myVocabList,testEntry))
    print(testEntry,'classified as: ', classifyNB(thisDoc,p0V,p1V,pAb))
    
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in vocabList:
        returnVec[vocabList.index(word)] +=1
    return returnVec

testingNB()
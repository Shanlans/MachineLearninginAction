# -*- coding: utf-8 -*-
import numpy as np

#arrayA = np.random.rand(4,4)
#print(arrayA)
#
#randMat = np.mat(arrayA)
#print(randMat)
#
#invRandMat = randMat.I
#print(invRandMat)
#
#myEye=randMat*invRandMat
#print(myEye)
#print(myEye-np.eye(4))

import knn
import os

#group,labels = knn.createDataSet()
#
#
#classCount = knn.classify0([0,0],group,labels,3)
#print(classCount)

path=os.getcwd()

filedir = os.path.join(path,'datingTestSet.txt')
datingDataMat,datingLabels = knn.file2matrix(filedir)

knn.autoNorm(datingDataMat[0])

#import matplotlib.pyplot as plt
#fig =plt.figure()
#ax = fig.add_subplot(111)
#ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15*np.array(datingLabels),15*np.array(datingLabels))
#plt.show()

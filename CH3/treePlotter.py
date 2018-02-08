'''
Created on Oct 14, 2010

@author: Peter Harrington
'''
import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth",fc="0.8")
leafNode = dict(boxstyle="round4",fc="0.8")
arrow_args = dict(arrowstyle="<-")

def plotNode(nodeTxt,centerPt,parentPt,nodeType):
    createPlot.ax1.annotate(nodeTxt,
                            xy=parentPt,
                            xycoords='axes fraction',
                            xytext=centerPt,
                            textcoords='axes fraction',
                            va="center",
                            ha="center",
                            bbox=nodeType,
                            arrowprops = arrow_args)
    
#def createPlot():
#    fig = plt.figure(1,facecolor="white")
#    fig.clf()
#    createPlot.ax1 = plt.subplot(111,frameon=False)
#    plt.axis('off')
#    createPlot.a = 1
#    plotNode(U'DecisionNode',(0.5,0.1),(0.1,0.5),decisionNode)
#    plotNode(U'Leafnode',(0.8,0.1),(0.3,0.8),leafNode)
#    plt.show()
    
def getNumLeafs(myTree):
    numLeafs = 0 
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:   
            numLeafs+=1 
    return numLeafs

def getTreeDepth(myTree):
    maxDepth = 0 
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else: thisDepth = 1
        if thisDepth > maxDepth : maxDepth = thisDepth    
    return maxDepth

def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid,yMid,txtString)
    
def plotTree(myTree, parentPt, nodeTxt):
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = list(myTree.keys())[0]
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0/plotTree.totalW, plotTree.yOff)
    '''
    This node's all leafs take the length: numLeafs * (1/plotTree.totalW)
    This node place shoule be half the leafs length: 1/2 * (numLeafs * (1/plotTree.totalW))
    'Because the whole image x start from 'plotTree.xOff = -0.5 / plotTree.totalW ' (0.5 half point)
    So all the node centre point can start from integer point, each time, just need add the integer'
    Adventually, this node center point should be: 1/2 * (numLeafs * (1/plotTree.totalW)) + 1/2*(1/plotTree.totalW) = 
    (1+numbLeafs) / (2*plotTree.totalW) 
    
    '''

    plotMidText(cntrPt,parentPt,nodeTxt)
    plotNode(firstStr,cntrPt,parentPt,decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key],cntrPt,str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondDict[key],(plotTree.xOff, plotTree.yOff),cntrPt,leafNode)
            plotMidText((plotTree.xOff,plotTree.yOff),cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD

def createPlot(inTree):
    fig = plt.figure(1, facecolor = 'white')
    fig.clf()
    axprops = dict(xticks = [], yticks = [])
    createPlot.ax1 = plt.subplot(111,frameon=False, **axprops)
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5 / plotTree.totalW 
    '''
    'Because the whole image x start from 'plotTree.xOff = -0.5 / plotTree.totalW ' (0.5 half point)
    So all the node centre point can start from integer point, each time, just need add the integer'
    '''
    plotTree.yOff = 1.0 
    plotTree(inTree,(0.5,1.0),'')
    plt.show()

def retrieveTree(i):
    listOfTrees = [{'no surfacings': {0: 'no', 1:{'flippers': {0: 'no',1 :'yes'}}}}, 
                   {'no surfacings': {0: 'yes',1:{'flippers': {0: {'head':{0: 'no', 1: 'yes'}}, 1: 'no'}}}}]
    return listOfTrees[i]



    

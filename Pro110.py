import pandas as pd 
import csv
import random
import statistics
import plotly.figure_factory as ff 
df=pd.read_csv('medium_data.csv')
data=df['reading_time'].tolist()
#fig=ff.create_distplot([data],['reading_time'],show_hist=False)
#fig.show()
populationMean=statistics.mean(data)
populationStd=statistics.stdev(data)
def randomSetOfMean(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    std=statistics.stdev(dataSet)
    return mean

def showFig(meanList):
    df=meanList
    fig=ff.create_distplot([df],['reading_time'],show_hist=False)
    fig.show()

def setUp():
    meanList=[]
    for i in range(0,1000):
        setOfMeans=randomSetOfMean(10)
        meanList.append(setOfMeans)
    showFig(meanList)
    print(statistics.mean(meanList))
setUp()
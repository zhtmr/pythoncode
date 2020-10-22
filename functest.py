import matplotlib.pyplot as plt
import pandas as pd

def showPlot(data,maxYear,maxDay,xcolname,ycolname):
    for i in range(maxYear):
        data1=data.loc[0+(maxDay*i):(maxDay-1)+(maxDay*i)]
        plt.plot(data1[xcolname],data1[ycolname]) 
    plt.show()

def getSortData(data,groupList,asc=True):
    data1 = data.set_index(groupList).sort_index(ascending=asc)
    print(data1)
    print("===============================")
    return data1.reset_index(inplace=False)


# month + day 값이 필요함
def setMonthDay(data, maxRange, col1, col2, newcol):
    for i in range(maxRange):
        month=str(data.loc[i,col1])
        day=str(data.loc[i,col2])
        data.loc[i,newcol]=month+day
    return data

def showPlotTwinx(x,y1,y2,leg):
    ax1=plt.subplot()
    ax2=ax1.twinx()
    line1=ax1.plot(x,y1,'r')
    line2=ax2.plot(x,y2,'g')
    lines=line1+line2
    plt.legend(lines,leg)
    plt.show()

def readCsv(csvdata,names1):
    data=pd.read_csv(csvdata,sep="\t|,",names=names1)
    print(data)
    print("===============================")
    return data
    

def showBar(data,ylim1,ylim2,xcol,ycol,top10=10):
    data1=data.loc[:top10-1]    
    plt.figure()      
    plt.ylim([ylim1, ylim2])
    plt.bar(data1[xcol],data1[ycol])
    plt.show()

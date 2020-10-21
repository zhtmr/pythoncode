import pandas as pd
import matplotlib.pyplot as plt

# 함수화 규칙
#  입력 데이터는 괄호안에 작성
#  데이터의 출력은 return
#  출력 관련 함수 사용금지

def getSortData(data,groupList):
    data1 = data.set_index(groupList).sort_index()
    return data1.reset_index(inplace=False)

data=pd.read_csv("ymd.csv",sep="\t|,",names=['year','month','day','data'])
groupList=['year','month','day']


data1 = getSortData(data,groupList)

# month + day 값이 필요함
def setMonthDay(data, maxRange, col1, col2, newcol):
    for i in range(maxRange):
        month=str(data.loc[i,col1])
        day=str(data.loc[i,col2])
        data.loc[i,newcol]=month+day
    return data

maxYear=4
maxDay=12*3
data2 = setMonthDay(data1,maxYear*maxDay,'month','day','monthday')


plt.show()

print(data2)



# for i in range(4):
#     data3=data2.loc[0+(36*i):35+(36*i)]
#     print(data3)
#     plt.plot(data2['month'],data2['data']) 


# plt.show()
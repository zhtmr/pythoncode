import pandas as pd
import matplotlib.pyplot as plt

# data=pd.read_csv("canceldata.csv",sep="\t",names=['yearmonth','data'])
# plt.bar(data['yearmonth'],data['data'])

# canceldata.csv : 미리 메모장에서 2005,01,234 식으로 바꿔온다
data=pd.read_csv("canceldata.csv",names=['year','month','data'])

for i in range(4):
    data1=data.loc[0+(12*i):11+(12*i)]
    print(data1)
    plt.plot(data1['month'],data1['data'])

plt.legend(['2005','2006','2007','2008'])
plt.show()
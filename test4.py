import pandas as pd
import matplotlib.pyplot as plt

# data=pd.read_csv("canceldata.csv",sep="\t",names=['yearmonth','data'])
# plt.bar(data['yearmonth'],data['data'])

# canceldata.csv : 미리 메모장에서 2005,01,234 식으로 바꿔온다
data=pd.read_csv("ymd.csv",sep="\t|,",names=['year','month','day','data'])
data1 = data.set_index(['year','month','day']).sort_index()
data2 = data1.reset_index(inplace=False)

# print(data2.loc[0:12*3-1])
# print(data2.loc[36:71])




for i in range(4):
    data3=data2.loc[0+(36*i):35+(36*i)]
    print(data3)
    plt.plot(data2['day'],data2['data'])


plt.show()
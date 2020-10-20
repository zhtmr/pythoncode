import pandas as pd
import matplotlib.pyplot as plt

# 위쪽 라벨
data1 = pd.read_csv("monthdata.csv", names=['year','month','data'])
# year, month 기반으로 인덱스, 정렬
data2 = data1.set_index(['year','month']).sort_index()
# 차트에 맞는 형식으로 바꾸기
data3 = data2.reset_index(inplace=False)

for i in range(4):
    data4 = data3.loc[0+(i*12):11+(i*12)] # [0:11]2005.1~12월, [12:23]2006.1~12월, ...
    print(data4)
    plt.plot(data4['month'],data4['data'])

# 범례
plt.legend(['2005','2006','2007','2008'])
plt.show()

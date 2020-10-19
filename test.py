import pandas as pd
import matplotlib.pyplot as plt

s1=pd.read_csv("monthdata.csv", names=['year','month','data'])
data1=s1.set_index(['year','month']).sort_index()
data2=data1.reset_index(inplace=False)
for i in range(4):
    data3=data2.loc[0+(i*12):11+(i*12)]
    plt.plot(data3['month'], data3['data'])
plt.legend(['2005','2006','2007','2008'])
plt.show()

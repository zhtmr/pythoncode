import pandas as pd
import matplotlib.pyplot as plt



#데이터 추출
s1=pd.read_csv("monthdata.csv", names=['year', 'month', 'data'])
#데이터 정렬
data1 = s1.set_index(['year','month']).sort_index()
#멀티인덱스 해제
data2=data1.reset_index(inplace=False)
#시각화 데이터 입력
for i in range(4):
    data3 = data2.loc[0+(i*12):11+(i*12)]
    plt.plot(data3['month'], data3['data'])
#범례 작성
plt.legend(['2005', '2006', '2007', '2008'])
#시각화
plt.show()
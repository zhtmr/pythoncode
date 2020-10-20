import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc 
import platform



def setHangleFont():
    if platform.system()=='Windows':
        font_name=font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font',family=font_name)
    else:
        rc('font',family='AppleGothic')
    mpl.rcParams['axes.unicode_minus'] = False
    

def ConvertFile(file,delim):
    with open(file,"rb") as infile, open("conv"+file,"w") as outfile:
        data=infile.read().decode('utf-8').split(delim)
        print(data)
        data=','.join(data)
        outfile.write(data)
    print('convert file : {}'.format(file))

ConvertFile('canceldata.csv','\t')
setHangleFont()
csvdata=pd.read_csv('convcanceldata.csv',encoding='cp949', names=['year&month','count'])
print(csvdata)
plt.figure()

# year, month 기반으로 인덱스, 정렬
data2 = csvdata.set_index(['year&month']).sort_index()
# 차트에 맞는 형식으로 바꾸기
data3 = data2.reset_index(inplace=False)
x=[1,2,3,4,5,6,7,8,9,10,11,12]

for i in range(4):
    data4 = data3.loc[0+(i*12):11+(i*12)] # [0:11]2005.1~12월, [12:23]2006.1~12월, ...
    print(data4)
    plt.plot(x,data4['count'])
    # plt.bar(data4['year&month'],data4['count'])

plt.legend(['2005','2006','2007','2008'])
plt.show()

# data1 = pd.read_csv("daydata.csv", names=['day','data'])
# plt.bar(range(len(data1['day'])),data1['data'])
# ax=plt.subplot()
# ax.set_xticks([0,1,2,3,4,5,6])
# ax.set_xticklabels(['월요일','화요일','수요일','목요일','금요일','토요일','일요일'])
# plt.show()

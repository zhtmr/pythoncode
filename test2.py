import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc 
import platform

# mpl.rcParams['axes.unicode_minus'] = False
# plt.rcParams["font.size"] = 12
# plt.rcParams["font.family"] = 'NanumGothic'
# plt.rcParams['xtick.labelsize'] = 12.
# plt.rcParams['ytick.labelsize'] = 12.

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

ConvertFile('daydata.csv','\t')
setHangleFont()
csvdata=pd.read_csv('convdaydata.csv',encoding='cp949', names=['day','count'])
print(csvdata)
plt.figure()
plt.bar(csvdata['day'],csvdata['count'])
plt.show()

# data1 = pd.read_csv("daydata.csv", names=['day','data'])
# plt.bar(range(len(data1['day'])),data1['data'])
# ax=plt.subplot()
# ax.set_xticks([0,1,2,3,4,5,6])
# ax.set_xticklabels(['월요일','화요일','수요일','목요일','금요일','토요일','일요일'])
# plt.show()

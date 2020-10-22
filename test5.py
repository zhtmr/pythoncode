import functest as ft
# data=pd.read_csv("canceldata.csv",sep="\t",names=['yearmonth','data'])
# plt.bar(data['yearmonth'],data['data'])




# data=pd.read_csv("old.csv",sep="\t|,",names=['airflight','data'])
# data1=data.loc[0:19]
# # print(data.loc[0:19])
# data2 = data1.set_index(['data']).sort_index()
# data3 = data2.reset_index(inplace=False)
# plt.ylim([150, 300])
# plt.bar(data3['airflight'],data3['data'])
# print(data3)

csvdata="old.csv"
names=['airflight','data']

xcol='airflight'
ycol='data'



data = ft.readCsv(csvdata,names)
data1= ft.getSortData(data,['data'],False)
ft.showBar(data1,1200,2000,xcol,ycol,20)





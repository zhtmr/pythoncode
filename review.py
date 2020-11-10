import pandas as pd
import functest as ft
import matplotlib.pyplot as plt

data = pd.read_csv("olist/product.csv", sep='\t|,', names=['product_category_name'])
print(data)

# groupList = ['sum', 'avg']
# data1 = ft.getSortData(data, groupList)
# print(data1)


# ft.showPlotTwinx(data['carrier'], data['sum'], data['avg'], groupList)

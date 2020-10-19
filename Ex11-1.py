from bs4 import BeautifulSoup
import requests
import time

def getURLInfo(url,tag):
    urlHeader=requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
    html=BeautifulSoup(urlHeader.text,"html.parser")
    return html.select(tag)

url="https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=101"
tag="div.cluster div.cluster_group._cluster_content div.cluster_body ul li div.cluster_text a"
headline=getURLInfo(url,tag)

for news in headline:
    print(news.text)
    articleURL=news.attrs["href"]
    articleTag="#articleBodyContents"
    data=getURLInfo(articleURL,articleTag)
    #data가 리스트 형식이라 직접적으로 .text를 사용할 수 없음
    print(data[0].text)
    print("------------------------")
    #break
    time.sleep(1)
from bs4 import BeautifulSoup
import requests

def getURLinfo(url,tag):
    urlHeader = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(urlHeader.text, "html.parser")
    return html.select(tag)

url = "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=101"    

tag = "#main_content > div > div._persist"
data = getURLinfo(url,tag)
for d in data:
    div = d.find("div","cluster")
    print(div.text)

# tag = "#main_content > div > div._persist > div > div > div.cluster_body > ul > li > div.cluster_text > a"
# data = getURLinfo(url,tag)
# for news in data:
#     print(news.text)
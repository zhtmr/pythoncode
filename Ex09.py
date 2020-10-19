from bs4 import BeautifulSoup
import urllib.request as req
import time

def getURLinfo(url, tag):
    html = req.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    return soup.select(tag) # 배열형식으로 리턴


url = "https://news.daum.net/"
tag = ".box_peruse .pop_news.pop_cmt ol li a"
values = getURLinfo(url, tag)

for v in values:
    articleUrl = (v.attrs["href"])
    articleTag = "#harmonyContainer"
    data = getURLinfo(articleUrl,articleTag)
    print(data[0].text)

    time.sleep(3)


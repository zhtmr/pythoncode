from bs4 import BeautifulSoup
import urllib.request as req

def getURLinfo(url, tag):
    html = req.urlopen(url)
    soup = BeautifulSoup(html,"html.parser")
    return soup.select(tag)


url = "https://ko.wikipedia.org/wiki/%EC%9C%A4%EB%8F%99%EC%A3%BC#%EC%9E%91%ED%92%88"
tag = "#mw-content-text div.mw-parser-output > ul"
values = getURLinfo(url,tag)


for v in values:
    if v.string is None:
       aUrl = "https://ko.wikipedia.org/" + v.a.attrs["href"]
       aTag = "#mw-content-text > div.mw-parser-output > ul"
       vv=getURLinfo(aUrl, aTag)
       print(vv[0].text)
       break

# print(aUrl)





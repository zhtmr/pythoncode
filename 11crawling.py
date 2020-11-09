import urllib.request
from bs4 import BeautifulSoup

uri = "http://www.11st.co.kr/products/1594537769"

values = {
    "trTypeCd":"21",
    "trCtgrNo":"585021"
}

dataEncode = urllib.parse.urlencode(values)

url = uri+"?"+dataEncode
html = urllib.request.urlopen(url)
# print(data.decode("utf-8"))

soup = BeautifulSoup(html, "html.parser")
review = soup.select("#review-list-page-area > ul > li > div")
review1 = soup.select("#review-list-page-area > ul > li:nth-child(2) > div > div > div.cont_text_wrap > p")
review2 = soup.select("#review-list-page-area > ul")
# print(review2[0].text)

for r in review2:
    d=r.find("li").find("div").find("div", class_="cont_text_wrap").find("p").string
    print(d[0].text)


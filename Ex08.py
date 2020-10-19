from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"
html = req.urlopen(url)

soup = BeautifulSoup(html, "html.parser")

# value 추출
# value = soup.select_one("span.value")
# change = soup.select_one("div.point_up > .value")

# print(value, " : ", value.string)
# print(change, " : ", change.string)

# 여러개 추출 select
# values = soup.select("span.value")
# # pList의 값을 하나씩 p에전달
# for v in values:
#     print(v.string)

change = soup.select(".point_up > .value")
up = soup.select(".point_up > .change")
worldEx = soup.select("#worldExchangeList li a .point_up>.value")
worldEx2 = soup.select("#worldExchangeList li a")

print("\n")
print("point_up value : ")
for c in change:
    print(c.string)
print("\n")
print("up : ")
for u in up:
    print(u.string)
print("\n")
print("worldEx : ")
for w in worldEx:
    print(w.string)
print("\n")
print("worldEx2 : ")
for v in worldEx2:
    div = v.find("div", "head_info point_up")
    if div is None:
        continue
    moneyName = v.h3.span.string
    money = v.find("div").find("span", "value").string
    print(moneyName +" : "+ money)
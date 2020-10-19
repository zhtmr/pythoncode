from bs4 import BeautifulSoup

html = """
<html><body>
	<h1 id="title">스크래핑이란</h1>
	<p id="body" class="pTag">웹페이지를 분석하는것</p>
	<p class="pTag">원하는 부분을 추출하는것</p>
</body></html>
"""

soup = BeautifulSoup(html, "html.parser")

# title 추출, select_one
title = soup.select_one("body > h1")
print(title, " : ", title.string)

# p태그 추출, select
pList = soup.select("p")
# pList의 값을 하나씩 p에전달
for p in pList:
    print(p.string)
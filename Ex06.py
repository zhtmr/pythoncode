from bs4 import BeautifulSoup

html = """
<html><body>
	<h1 id="title">스크래핑이란</h1>
	<p id="body" class="pTag">웹페이지를 분석하는것</p>
	<p class="pTag">원하는 부분을 추출하는것</p>
</body></html>
"""

soup = BeautifulSoup(html, "html.parser")

# print(soup.html.body.h1)
# print(soup.html.body.h1.string)

title = soup.find(id="title")
print(title," : ", title.string)
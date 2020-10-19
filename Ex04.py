import urllib.request

uri = "https://newsearch.seoul.go.kr/ksearch/search.do"

values = {
    "kwd":"뉴딜일자리"
}
dataEncode = urllib.parse.urlencode(values)
# 
url = uri +"?"+ dataEncode

data = urllib.request.urlopen(url).read()
# print(data.decode("utf-8"))

with open("seoul_quiz2.html",mode="w") as f:
    f.write(data.decode("utf-8"))
    print("파일 다운 완료.")
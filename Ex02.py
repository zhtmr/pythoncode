# import 라이브러리 등록
import urllib.request

# 변수 선언
# "접속할 URL" 
url = "https://www.seoul.go.kr/main/index.jsp"
req = urllib.request

mem = req.urlopen(url).read()
# euc-kr, utf-8
decodeMem = mem.decode("utf-8")
# print(decodeMem)

with open("seoul.html", mode="wb") as f:
    f.write(mem)
    print("파일 다운 완료")
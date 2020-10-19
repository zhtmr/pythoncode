# import 라이브러리 등록
import urllib.request

# 변수 선언
# "접속할 URL"
url = "https://www.seoul.go.kr"#"upload/hotissue/931b44fec2474246ae4f20e95934e9e3.jpg"
saveFile = "test.jpg"

# url 에 접속하여 saveFile 로 저장
urllib.request.urlretrieve(url,saveFile)

import urllib.request

uri = "https://search.naver.com/search.naver"

values = {
    "sm":"top_hty",
    "fbm":"1",
    "ie":"utf8",
    "query":"빅데이터"
}
dataEncode = urllib.parse.urlencode(values)
# 
url = uri +"?"+ dataEncode

data = urllib.request.urlopen(url).read()
print(data.decode("utf-8"))
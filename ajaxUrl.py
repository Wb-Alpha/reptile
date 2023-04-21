from urllib import request
from urllib import parse
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
url = "https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&start=0&count=20&selected_categories=%7B%22%E7%B1%BB%E5%9E%8B%22:%22%E5%8A%A8%E4%BD%9C%22%7D&uncollect=false&tags=%E5%8A%A8%E4%BD%9C"
rq = request.Request(url=url, headers=headers)
response = request.urlopen(rq)
text = response.read().decode('utf-8')
print(text)
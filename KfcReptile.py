import urllib.parse
from urllib import request
from urllib import parse
import json

post_url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
data_dict = {
    "cname": "",
    "pid": "",
    "keyword": "广州",
    "pageIndex": "1",
    "pageSize": "40"
}

data = urllib.parse.urlencode(data_dict)
data = data.encode('utf-8')

# 配置Post请求参数
# 请求头（优先级：ua>cookies>referer>origin
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
# 封装Request
req = request.Request(url=post_url, headers=headers, data=data)
response = request.urlopen(req)
print(response.getcode())

# 读取response内容
text = response.read().decode('utf-8')
print(text)

json_obj = json.loads(text)
canteen_list = json_obj["Table1"]

for detail in canteen_list:
    print(detail["storeName"]+" "+detail["addressDetail"]+" ")
from urllib import request
from urllib import parse
import json

# # 如何处理post请求
# url = "https://fanyi.baidu.com/#en/zh/code"
# re = request.Request(url=url, headers={})
#
# response = request.urlopen(url)
# text = response.read().decode('utf=8')
# print(text)
#
# with open('baidufanyi.html', 'w', encoding='utf-8') as fp:
#     fp.write(text)

# post请求地址
pos_url = "https://fanyi.baidu.com/sug"
# post表单
data_dict = {
    "kw": "apple"
}
# url编码
data = parse.urlencode(data_dict)
# 字节编码
data = data.encode('utf-8')

# 获取对应的Request对象
rq = request.Request(url=pos_url, headers={}, data=data)
response = request.urlopen(rq)
text = response.read().decode('utf-8')
print(text)

# text是一个str，所以需要进一步解析他
# json字符串需要使用json解析
# xml(html)可以使用xml(html)解析
# print(type(text))
# json字符串编码为json对象
json_obj = json.loads(text)
print(json_obj)
print(json_obj["data"])


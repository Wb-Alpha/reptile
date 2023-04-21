from lxml import etree
from urllib import request
from urllib import parse

url = "https://sc.chinaz.com/tupian/jianzhutupian.html"
req = request.Request(url, headers={})
response = request.urlopen(req)
message = response.read().decode('utf-8')

# 如果希望对一个html使用xpath解析，首先要将他封装成一个可以被xpath解析的tree对象
tree = etree.parse(message)
print(tree)

# 使用xpath函数，传递一个xpath路径


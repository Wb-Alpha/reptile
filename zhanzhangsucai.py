from urllib import request
from urllib import parse
import json

# url = "https://scpic3.chinaz.net/files/default/imgs/2023-04-13/8050fa0bf18b00ce_s.jpg"
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
# }
#
# req = request.Request(url=url, headers=headers)
#
# # 下载多媒体资源的时候，一般使用二进制存储
# # json\html等资源，则使用文本格式存储
# response = request.urlopen(req)
# # 默认read出来的就是二进制流
# content = response.read()
#
# # 将请求到的资源本地存储
# with open('building.jpg', 'wb') as fp:
#     fp.write(content)


# 找到网站中的所有照片
# 首页链接
url = "https://sc.chinaz.com/tupian/jianzhutupian.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
req = request.Request(url=url, headers=headers)
response = request.urlopen(req)
text = response.read().decode('utf-8')

with open('zhanzhangsucai.html', 'w', encoding='utf-8') as fp:
    fp.write(text)

# lazy loading懒加载:一般应用于前端或者移动端，是一种设计逻辑
# 当前端需要加载的资源特别大，会影响到用户体验的时候，一般会使用到懒加载模式
# 懒加载只会在图片需要使用的时候才会加载
# 因此，首页的html中已经指明了所有图片的url，但是加载是后台异步加载的，因此我们需要从首页的html中提取出图片的url


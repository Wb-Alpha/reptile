import requests
from urllib import request
from urllib import parse


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# url = "http://www.baidu.com"
#
# response = request.urlopen(url)
#
# print(response)
# # 读取响应体(此时读取到的是字节流)
# # print(response.read())
#
# # 指定编码集(通常在源码的head标签中有指定）
# text = response.read().decode("utf-8")
# # print(text)
# with open("baidu.html", "w", encoding='utf-8') as fp:
#     fp.write(text)
#
# # 获取状态码
# print(response.getcode())
# # 获取url
# print(response.geturl())
# # 获取响应头
# print(response.getheaders())

# 有时候url会有很多的参数值，如果希望获取某些指定结果，则需要添加一些参数
# 比如想要百度一下“苹果“，那么他的url如下，https://www.baidu.com/s?wd=%E8%8B%B9%E6%9E%9C
# # 如果想要搜索"苹果"，那应该使用quote函数将他转化为utf=8编码
# url = "http://www.baidu.com/s?wd=%E8%8B%B9%E6%9E%9C"
# url1 = "http://www.baidu.com/s?wd="+parse.quote("苹果")
# # print(url == url1)
# # response = request.urlopen(url)
# # text = response.read().decode("utf-8")
# # print(text)
# # 解码使用unquote函数
# # print(parse.unquote("E8%8B%B9%E6%9E%9C"))

# 如果参数太多，在拼接url的时候会非常麻烦，可以使用urlencode函数进行拼接
# params_dict = {
#     "user": "admin",
#     "password": "root"
# }
#
# params = parse.urlencode(params_dict)
# print(params)

# 下载图片
# img_url = "	https://img2.autotimes.com.cn/news/2021/06/0627_141125753686.jpg"
# response_img = request.urlopen(img_url)
# content = response_img.read()
# with open('bmw.jpg', 'wb') as fp:
#     fp.write(content)

# 我们也可以使用url
# img_url = "https://img.cheshi-img.com/center/680/99/21/f6/291ed522fffbeddb0620723e73.jpeg"
# request.urlretrieve(img_url, 'm3.jpeg')
#
# # 爬虫：伪装成浏览器发送请求
# # request.Request类可以用来封装一个请求对象，会携带除了url之外的一切服务器感兴趣的东西
# # 比如所cookie, ua等
# url = "http://www.baidu.com"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
# }
# req_obj = request.Request(url=url, headers=headers)
# response = request.urlopen(req_obj)
# print(response.read().encode("utf-8"))

# url分类
# 1. 直接获取地址栏中的url
# 2. 地址栏的url不是固定的，带有参数的需要手动配置
# 3. 有效地址不在地址栏中，在Network后台加载，使用F12查看
# 4. 第三种情况的变种

# URL分为get请求和post请求，返回值有xml（html）、json格式，解析方式不一样

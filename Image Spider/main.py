import requests
from bs4 import BeautifulSoup

url = 'http://tieba.baidu.com/p/2166231880'
header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,en-GB;q=0.5',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Host':'tieba.baidu.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
}
#img.BDE_Image src
s = requests.session()
req = s.get(url,headers = header)
soup = BeautifulSoup(req.text,'html5lib')
imgList = soup.find_all(attrs = {"class": "BDE_Image"})
index = 0
for node in imgList:
    src = node['src']
    req = s.get(src)
    if req.status_code == 200:
        open(r'E:/PythonCaseWork/Image Spider/images/image' + str(index) + r'.jpg','wb').write(req.content)
        index = index + 1
print('end!')

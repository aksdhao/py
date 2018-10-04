#获取网页源码
import requests  #取得requests库
url='http://www.mzitu.com'  #需要爬取的网址
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
html=requests.get(url,headers=header)
print(html.text)

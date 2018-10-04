import requests
url='https://www.618ii.com/index/home.html'
a=requests.get(url).text
print(a)
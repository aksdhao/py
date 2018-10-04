import requests,re
url='http://www.mm131.com/xinggan/'
a=requests.get(url).text
b=re.findall('http://www.mm131.com/xinggan/\d\d\d\d.html',a)
print(b)
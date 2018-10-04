import requests,re
url='http://www.mm131.com/qipao/'
html=requests.get(url).text
a=re.findall('http://www.mm131.com/qipao/\d{4,6}.html',html)
b=open('D:\py\c5.txt','w')

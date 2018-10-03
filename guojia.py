import requests,re
url='http://www.mm131.com/qipao/'
html=requests.get(url).text
a=re.findall('http://www.mm131.com/\w{5,7}/\d{4,6}.html',html)
print(a)
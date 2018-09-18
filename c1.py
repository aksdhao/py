import requests
import re
url = 'http://www.mm131.com/xinggan/2112.html'
html = requests.get(url).text
a = re.search(r'img src.* src="(.*?)" /',html,re.S)
print(a.group(1))
thtml = requests.get('http://'+ a)
tu = open(a,'wb')
tu.write(thtml.content)
tu.close()
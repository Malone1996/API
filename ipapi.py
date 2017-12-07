import urllib, urllib.request, sys
import ssl
#import json

host = 'https://api01.aliyun.venuscn.com'
path = '/ip'
method = 'GET'
appcode = '06d0e56ac82443009e6eeec4052ecdde'
querys = 'ip=120.78.174.186'
bodys = {}
url = host + path + '?' + querys

request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib.request.urlopen(request, context=ctx)
content = str(response.read(),'utf-8')
if (content):
	print(content)
    #print(json.loads(content))
f = open(r"C:\Users\mayao\Desktop\mobiles.txt",'wb')
f.write(content.encode())
f.close()


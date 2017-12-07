import urllib, urllib.request, sys#urllib2在python3版本中用urllib.request代替
import ssl

host = 'https://api01.aliyun.venuscn.com'
path = '/ip'
method = 'GET'
appcode = '06d0e56ac82443009e6eeec4052ecdde'#阿里云获取appcode
querys = 'ip=120.78.174.186'#查询指定IP地址
bodys = {}
url = host + path + '?' + querys

request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib.request.urlopen(request, context=ctx)
content = str(response.read(),'utf-8')#utf-8编码输出中文结果
if (content):
	print(content)
#在指定位置创建文件写入返回的数据	
f = open(r"C:\Users\mayao\Desktop\demo.txt",'wb')
f.write(content.encode())
f.close()


from urllib.request import urlopen
from urllib.request import Request
import simplejson as json  

'''
u = urlopen("https://www.google.com.hk/")
google = u.read()
print(google)
'''

headers = {
           'User-Agent' : 'python-keystoneclient',
           'X-Auth-Token' : 'SYSUADMIN'
           }
r = Request("http://192.168.0.195:35357/v2.0/tenants" , headers = headers)
print(r.get_method())
testu = urlopen(r)
result = testu.read()  #the result is class "bytes"
str = result.decode('utf-8')    # turn it to a str

target = json.loads(str)   #turn it into a dic of python

for key in target:
    print(key)


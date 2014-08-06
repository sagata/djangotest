import sys
import datetime
import requests
from urllib.request import urlopen


u = urlopen("https://www.google.com.hk/")
google = u.read()
print(google)

#r = requests.get('http://192.168.0.195:35357/v2.0/tenants', x-auth-token="SYSUADMIN")
'''
r = requests.get('https://api.github.com/user')
print(r.status_code)
print(r.content)
print("gehe")
print(r.headers)

now = datetime.datetime.now()
print(now)
    
    
    
    
print(sys.path)
'''
def testfun(arg, *arg2, **arg3):
    print("arg   "+arg)
    print(arg2)
    print("your sister")
    print(arg3)
    
list = ["xiaoyang","zhaoyunxun"]


dic = {       'Swaroop'   : 'swaroopch@byteofpython.info',
             'Larry'     : 'larry@wall.org',
             'Matsumoto' : 'matz@ruby-lang.org',
             'Spammer'   : 'spammer@hotmail.com'
     }



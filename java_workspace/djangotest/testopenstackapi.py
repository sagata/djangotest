import base64,urllib,httplib2,json,os


h3 = httplib2.Http(".cache")
h3.add_credentials('name', 'password')
resp3, content3 = h3.request("http://192.168.0.195:35357/v2.0/tenants",
    "GET", headers={'content-type':'application/json,' , 'X-Auth-Token ':'SYSUADMIN'  , 'User-Agent' : 'python-keystoneclient'} )
print (resp3)
print (content3)
'''
url1="192.168.0.195:35357"
params1 = '{"auth": {"tenantName": "tenant-name", "passwordCredentials":{"username": "admin", "password": "sysuadmin"}}}'
headers1 = {"Content-Type": 'application/json'}
conn1 = httplib2.Http()
response1,content = conn1.request('192.168.0.195:35357/v2.0/tokens')  
#response1,content = conn1.request("192.168.0.195:35357/v2.0/tokens","POST", headers)
#response1 = conn1.getresponse()
#data1 = response1.read()
#dd1 = json.loads(data1)

#print(dd1)
print(response1)

'''

'''
apitoken = dd1['access']['token']['id']
apitenant= dd1['access']['token']['tenant']['id']
apiurl = dd1['access']['serviceCatalog'][0]['endpoints'][0]['publicURL']
apiurlt = urlparse(dd1['access']['serviceCatalog'][0]['endpoints'][0]['publicURL'])

url2 = apiurlt[1]
params2 = urllib.urlencode({})
headers2 = { "X-Auth-Token":apitoken, "Content-type":"application/json" }
conn2 = httplib.HTTPConnection(url2)
conn2.request("GET", "%s/servers" % apiurlt[2], params2, headers2)
response2 = conn2.getresponse()
data2 = response2.read()
dd2 = json.loads(data2)
conn2.close()
for i in range(len(dd2['servers'])):
    print dd2['servers'][i]['name']
    '''
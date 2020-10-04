import json
import urllib.request, urllib.parse, urllib.error
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if len(address) < 1: address="http://py4e-data.dr-chuck.net/comments_42.xml"
print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)

c=0
s=0
for i in info['comments']:
    c=c+1
    # print(i['count'])
    s=s+i['count']

print('User count:',c)
print('Sum:',s)

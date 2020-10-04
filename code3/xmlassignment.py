import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if len(address) < 1: address="http://py4e-data.dr-chuck.net/comments_42.xml"
print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read()
print('Retrieved', len(data), 'characters')

y=data.decode()
tree = ET.fromstring(y)
lst = tree.findall('comments/comment')
print('Count:', len(lst))
s=0
for item in lst:
    s= s + int(item.find('count').text)
print("Sum:",s)

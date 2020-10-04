# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
c=0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL- ')
count=int(input('Enter count-'))
pos=int(input('Enter position-'))
i=0
print('Retrieving:',url)

while i<count:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    # print(type(soup))
        # Retrieve all of the anchor tags
    tags = soup('a')
    # print(tags)
    # print(type(tags))
    for tag in tags:
        c=c+1
        if c==pos:
            # print(tag)
            print('Retrieving:',tag.get('href', None))
            url =tag.get('href', None)
            i=i+1
            c=0
            break
y=re.findall('by_([^ ]+\.)',url)
print(y[0])

            # print('Retrieving:',tag.get('href', None))

import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL cerificate errors (for HTTPS sites)
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CRET_NONE

url = input('Enter -')
# for HTTPS
#html = urllib.request.urlopen(url, context=ctx).read()
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

for ingredients in soup:
    print(ingredients)

# Retrieve all of the anchor tags, tag is an object
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

import urllib.request
from bs4 import BeautifulSoup
import ssl

cummulative_value = 0

# Ignore SSL cerificate errors (for HTTPS sites)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fhand = urllib.request.urlopen(
    'https://py4e-data.dr-chuck.net/comments_1654173.html', context=ctx).read()
soup = BeautifulSoup(fhand, 'html.parser')

tags = soup('span')

for tag in tags:
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
    cummulative_value = cummulative_value + int(tag.contents[0])

print(cummulative_value)

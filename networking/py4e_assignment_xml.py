import urllib.request
# from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

cummulative_sum = 0

url = input('Enter html:')
html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')

# print(html.decode())

tree = ET.fromstring(html)
# print(tree)

# for branch in tree:
#     print(branch)

results = tree.findall('comments/comment')
for result in results:
    cummulative_sum += int(result.find('count').text)
    # print(result.find('count').text)

print(cummulative_sum)

# counts = tree.findall('.//count') --> skips findall comments/comment and subsequent find

# for count in counts:
# print(count.text)

import urllib.request
import json

cummulative_sum = 0

url = input('Enter url:')
data = urllib.request.urlopen(url).read()

info = json.loads(data)

users = info.get('comments')

for user in users:
    cummulative_sum += user['count']

print(cummulative_sum)

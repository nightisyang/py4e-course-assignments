from glob import glob
import urllib.request
from bs4 import BeautifulSoup

url = input('Enter the first url')
url_position = 18
url_counter = 0
repeat = 7
repeat_counter = 0


def loop(url_address):
    global url_counter
    global url

    http = urllib.request.urlopen(url_address)
    soup = BeautifulSoup(http, 'html.parser')

    tags = soup('a')

    for line in tags:
        url_counter += 1

        if url_counter == url_position:
            print('Retrieving:', line.get('href', None))
            url = line.get('href', None)
            #print('New url:', url)
            url_counter = 0
            break


while True:
    # print('checking...')
    # print(url)
    if repeat_counter < repeat:
        loop(url)
        repeat_counter += 1
        continue
    if repeat_counter == repeat:
        break

#print('Repeat counter:', repeat_counter)

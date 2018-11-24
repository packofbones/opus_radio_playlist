# -*- coding: utf-8 -*-
from lxml import html
import requests
import time
import datetime

def parse():
    url = 'https://www.lrt.lt/mediateka/tiesiogiai/lrt-opus'
    page = requests.get(url)
    tree = html.fromstring(page.content)
    path = '//*[@id="streamTitle"]'
    currently_playing = tree.xpath(path+'/text()')
    currently_playing = currently_playing[0]
    currently_playing = currently_playing.replace('Šiuo metu grojame: ', '')
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return time, currently_playing

currently_playing_old = ''
while True:
    current_time, currently_playing = parse()
    if currently_playing == currently_playing_old:
        time.sleep(15)
        continue
    else:
        open('out.txt', 'a').write(current_time+" "+currently_playing+'\n')
        print(current_time+currently_playing)
        currently_playing_old = currently_playing
        time.sleep(60)

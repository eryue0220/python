#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from urllib.request import urlopen

url = 'https://gdata.youtube.com/feeds/api.standardfeeds/top_rated?all=json'

response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
data = json.load(text)

for video in data['feed']['entry'][0:6]:
    print(video['title']['$t'])

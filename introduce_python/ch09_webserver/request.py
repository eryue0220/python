#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
url = 'http://www.iheartquotes.com/api/v1/random'
resp = requests.get(url)

print(resp.text);

#!/usr/bin/env python3
# -*- coding: utf-8 -*-ss

import requests

resp = requests.get('http://localhost:9090/echo/Motha')
if resp.status_code == 200 and resp.text == 'Say hi to Motha':
    print('It worked.')
else:
    print('Argh, got this:', resp.text)


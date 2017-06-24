#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import redis

conn = redis.Redis()
topics = ['maine coon', 'persian']
sub = conn.pubsub()

for msg in sub.listen():
    if msg['type'] == 'message':
        print(msg)
        cat = msg['channel']
        hat = msg['data']
        print('Subscribe: %s wears a %s' % (cat, hat))

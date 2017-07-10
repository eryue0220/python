#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        return bytes_or_str.decode('utf-8')
    
    return bytes_or_str

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        return bytes_or_str.encode('utf-8')
    
    return bytes_or_str

def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, unicode):
        return unicode_or_str.encode('utf-8')

    return unicode_or_str
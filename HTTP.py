#!/usr/bin/env python
# -*- coding: utf-8 -*-
#A simple HTTP client that uses API client library to request for data from github
import requests

r = requests.get('https://api.github.com', auth=('user', 'pass'))

print r.status_code
print r.headers['content-type']

# ------
# 200
# 'application/json'
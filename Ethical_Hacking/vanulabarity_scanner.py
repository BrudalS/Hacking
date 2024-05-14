#!/usr/bin/env python

import requests
from BeautifulSoup4 import BeautifulSoup

def request(url):
    try:
        return requests(url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "http://10.24.1.1:8090/httpclient.html"
response = request(target_url)
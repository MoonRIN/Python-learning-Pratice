'''这是一个正儿八经的爬虫
   希望这个爬虫能够给我带来一些帮助'''

from bs4 import BeautifulSoup
import requests
import re

def getHtmlText(url):
    try:
        r = requests.get(url, TimeoutError=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "abnormal occur"

def beautifulHtmlText(url):
    htmlText = getHtmlText(url)
    soup = BeautifulSoup(htmlText, 'html.parser')
    soup.prettify()

def 
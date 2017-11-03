from bs4 import BeautifulSoup
import requests
import bs4

def getHtmltext(url):
    try:
        r = requests.get(url, TimeoutError=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivLIst(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.elements.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])

def printUnivlist(ulist, num):
    print("{:^10}\t{:^6}\{:10}".format("ranking", "name", "score"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))
    
def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
    html = getHtmltext(url)
    fillUnivLIst(uinfo, html)
    printUnivlist(ulist, 137)
main()
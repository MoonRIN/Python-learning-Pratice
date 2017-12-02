import requests
import re 

def getHtmlText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding =r.apparent_encoding
        return r.text
    except:
        return ""

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\{:16}"
    print(tplt.format("No.","Price","Number"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods = 'Êé°ü'
    depth = 3
    start_url = 'https://s.taobao.com/search?=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHtmlText(url)
            parsePage(infoList, html)
        except:
            continue
        printGoodsList(infoList)

if __name__ == '__main__':
    main()
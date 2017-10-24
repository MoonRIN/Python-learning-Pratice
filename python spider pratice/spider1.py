import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status() #if status is not 200, then occur unusual 
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "abnomal occur"

if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))
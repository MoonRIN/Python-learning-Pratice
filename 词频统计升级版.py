import jieba
import turtle

yScale = 6
xScale = 30
def drawLine(t, x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)

def drawText(t, x, y, text):
    t.penup()
    t.goto(x, y)
    t.write(text)

def drawGraph(t):
    drawLine(t, 0, 0, 360, 0)
    drawLine(t, 0, 300, 0, 0)

    for x in range(count):
        x = x+1
        drawText(t, x*xScale-4, -20, (words[x-1]))
        drawText(t, x*xScale-4, items[x-1]*yScale+10, items[x-1])
    drawBar(t)

def drawRectangle(t, x, y):
    x = x*xScale
    y = y*yScale
    drawLine(t, x-5, 0, x-5, y)
    drawLine(t, x-5, y, x+5, y)
    drawLine(t, x+5, y, x+5, 0)
    drawLine(t, x+5, 0, x-5, 0)

def drawBar(t):
    for i in range(count):
        drawRectangle(t, i+1, items[i])


def getText():
    filename = input("pls in put what file you want to count:")
    txt = open(filename, "r").read()
    for ch in '~!@#$%^&*()_+`-=[]\{}|;:",./<>?''':
        txt.replace(ch, " ")
    return txt
text = getText()
words = text.split()
chineseWords = jieba.lcut(text, cut_all = False)
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
for chineseWords in words:
    counts[word] = counts.get(word, 0) + 1

items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10000):
    word, count = items[i]
    print("{0:<10}, {1:>5}".format(word, count))

import requests
import re
import time

def spider():
    head = '''<!doctype html>
        <html>
        <head>
            <meta charset="GBK">
        <title>yompc</title>
        <style>
        .tablewd{width:500px}
        </style>
        </head>

        <body align="center">
        	<table class="tablewd" border="1" cellpadding="5" align="center">
          <tbody>
            <tr>'''
    fo = open("index.html", "w+")
    fo.write(head)
    fo.close()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Referer': 'http://www.0818tuan.com/list-1-0.html'

    }
    url = "http://www.0818tuan.com/list-1-0.html"
    try:
     resp = requests.get(url, headers=headers)
    except OSError:
        spider()
    try:
     text = resp.content.decode('gbk')
    except OSError:
        spider()
    try:
     url = re.findall('\/xbhd\/(.*?).html', text, re.I | re.S | re.M)
    except OSError:
        spider()
    print(url[2:29])
    try:
     for urls in url[2:29]:
        urlsx = 'http://www.0818tuan.com/xbhd/'+urls+'.html'

        shibie(urlsx)
    except OSError:
        spider()
def shibie(urlsx):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Referer': 'http://www.0818tuan.com/list-1-0.html'
    }
    try:
     resp = requests.get(url=urlsx, headers=headers)
    except OSError:
        spider()
    try:
     textx = resp.content.decode('gbk')
    except OSError:
     spider()
    try:
     pet = '<div class="post-content">\r\n                <script src=/d/js/acmsd/thea4.js></script>\r\n(.*?)\r\n                <p align="center" class="pageLink"></p>'
     texts = re.findall(pet, textx, re.I | re.S | re.M)
     pet2 = '<h1 class="text-center">(.*?)</h1>'
     title = re.findall(pet2, textx, re.I | re.S | re.M)
     pet3 = '</small>(.*?)<a id="weixin"'
     times = re.findall(pet3, textx, re.I | re.S | re.M)
    except OSError:
        spider()
    try:
     body = ('<tr><th><a href="'+urlsx+'">'+title[0]+times[0]+'</a></th></tr><th scope="row">'+texts[0]+'</th>')
    except OSError:
        spider()
    addhtml(body)
def addhtml(body):
    xo = open("index.html", "a+")
    for i in body:
        xo.write(i)
    xo.close()
def end():
    head2 = '''</tr>
      </tbody>
    </table>



    </body>
    </html>'''
    xo = open("index.html", "a+")
    xo.write(head2)
    xo.close()
if __name__ == '__main__':
    while True:
     try:
      spider()
      time.sleep(60)
     except OSError:
         pass


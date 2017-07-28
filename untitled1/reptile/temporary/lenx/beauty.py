from bs4 import BeautifulSoup as bs
import urllib.request
import os
def url_open(url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    red = urllib.request.Request(url,headers=header)
    redponse = urllib.request.urlopen(url).read()
    html = bs(redponse,"html.parser")
    return html


def img_err(url):
    html = url_open(url).decode('utf-8')
    a = html.find('seo-page-num')
    return html[a[0]]


def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')

    while a != -1:
        b = html.find('.jpg',a,a+255)
        if b != -1:
            img_addrs.append(html[a:b])
        else:
            b = a+9

        a = html.find('img src=',b)
    return img_addrs


def imger(filename,img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename,'wb') as x:
            while x == True:
                img = url_open(each)
                x.write(img)

def Aruil(filename = 'lenx',page = '10'):
    os.mkdir(filename)
    os.chdir(filename)
    url = "http://www.nipic.com/zhuanti/1352196_%s.html"
    page_num = int(img_err(url))

    for i in range(page):
        page_num -=i
        page_url = (url % page_num)
        img_addrs = find_imgs(page_url)
        imger(filename,img_addrs)

if __name__ == '__main__':
    Aruil()




import urllib.request
from bs4 import BeautifulSoup as bs

def url_open(url):
    head = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
    lenx = urllib.request.Request(url,headers=head)
    html_open = urllib.request.urlopen(lenx).read()
    html = bs(html_open,"html.parser")
    return html

def fin_div(url):
    open_url = url_open(url)
    html = open_url.find('div',{'class_':'swipeboxEx'})
    for l in html:
        url_lend = l.find_all('a')

    return url_lend


def url_lenx():
    url = "http://699pic.com/sousuo-146819-0-1.html"
    down_url = url_open(url)
    html = fin_div(down_url)
    print(html)

if __name__ == '__main__':
    url_lenx()
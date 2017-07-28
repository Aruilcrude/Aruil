from bs4 import BeautifulSoup as bs
import urllib.request

def url_open(url):
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
    lenx = urllib.request.Request(url,headers=head)
    xue  = urllib.request.urlopen(lenx).read()
    html = bs(xue,'html.parser')

    return html

def url_img(url):
    html = url_open(url)
    xue = html.find_all('ul',{'class':'search-result-box clearfix'})
    for l in xue:
        fen = l.find_all('img')
        fenx = str(fen)
        fengxin = fenx.split()
        fenxx =fengxin[-1].split('"')

        return fenxx[1]
def url_lenx():
    for l in range(1,10):
        url = 'http://www.nipic.com/zhuanti/1352196_'+ str(l) +'.html'
        html = url_img(url)
        print(html)

if __name__ == '__main__':
    url_lenx()


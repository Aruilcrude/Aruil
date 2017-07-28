from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re
lenx = set()        #定义一个空集合
def xue(fen):       #函数
    global pages         #定义pages 是一个全局变量
    url = urlopen(fen)         #爬取输入进来的URL
    fenx = bs(url,"html.parser")      #对爬取的数据进行排版

                                 #循环提取网站里的链接
    for xin in fenx.find_all("a",href=re.compile('http.*')):
         #判断链接是否在xin的所有链接里
        if 'href' in xin.attrs:
            if xin.attrs['href'] not in pages:             #再次判断xin里的所有链接
                MIN = xin.attrs['href']                  #提取出xin里的全部链接
                print(MIN)                             #输出
                pages.add(MIN)                        #写入集合
                xue(MIN)
xue("")
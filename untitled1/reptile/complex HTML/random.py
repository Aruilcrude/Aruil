from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
import random
import datetime
random.seed(datetime.datetime.now())       #生成一个随机数
def FEN(xue):                              #定义函数
    url = urlopen("https://img.alicdn.com"+xue)    #抓取网页源码
    lenx = bs(url,"html.parser")                 #对源码进行排版
    return lenx.find("div",{"class":"skin-box-hd"}).find_all("img",src = re.compile("^(/bao/uploaded/)((?!:).)*$"))
                                                                                                                  #利用正则来匹配图片链接
links = FEN("/bao/uploaded/")            #输入的链接同有的目录
while len(links)> 0:                      #判断提取出来的链接数量
    fenx = links[random.randint(0,len(links)-1)].attrs["src"]        # 随机选取一个链接  然后选取所有的图片地址
    print(fenx)               #输出
    links = FEN(fenx)
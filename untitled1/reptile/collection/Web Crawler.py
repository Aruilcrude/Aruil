from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
import datetime
import random

pages = set()    #定义一个集合
random.seed(datetime.datetime.now())    #生成随机数

def lenx(bsobj,include):      #定义一个函数
    inter = []                 #空列表
    #提取输入的网站里的链接并加上链接共有的目录
    for link in bsobj.find_all("a",herf = re.compile("^(/htpp.*)"+include+"")):
        if link.attrs['href'] is not None:           #判断所有的地址不是空值
            if link.attrs['href'] not in inter:     #判断所有的链接不在列表里
                lenx.append(link.attrs['href'])      #不在列表里输入进列表
    return lenx        #返回值

def getlike(bsobj,exclude):          #定义函数
    externa = []                    #空列表
    for link in bsobj.find_all("a",
                               href = re.compile("^(http|www)((?!"+exclude+").)*$")):  #提取网站里的链接并加上第二个输入函数值
        if link.attrs['href'] not in externa:         #判断链接是否存在于列表里
            externa.append(link.attrs['href'])          #不存在就把链接写入到列表
    return externa                 #返回值

def Address(address):                       #定义函数
    addressparts = address.replace("http://","").split("/")      #利用正则提取HTTP开头的  并用/进行分割
    return addressparts          #返回值

def getlinks(page):                      #定义函数
    url = urlopen(page)                 #下载HTML源码
    xue = bs(url,"html.parser")          #解析HTML 源码
    feng = lenx(xue,Address(page)[0])         #用Address函数进行提取URL
    if len(feng)==0:                    #判断feng 的长度是否等于0
        leng = getlike(page)              #等于0就调用第二个函数
        return getlinks(leng[random.randint(0,len(leng)-1)])
                       #返回本函数的值  并根据第二个函数输出的链接进行随机抽取 ，抽取一条链接  总数就减一
    else:
        return feng[random.randint(0,len(feng)-1)]
        #返回feng的链接数

def lengxue(site):                  #定义函数
    feng = getlinks("http://oreilly.com")      #调用getlinks来处理网站
    print("how are you :"+feng)               #输出一个字符串并加上处理完成的链接
    lengxue(feng)
lengxue("http://oreilly.com")             #对lengxue函数进行赋值url
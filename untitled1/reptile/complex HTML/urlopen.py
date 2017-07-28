#coding=utf-8
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup as soup
fen = set()
xin = open("E:/grep/lenx.txt","w")
url =urlopen("https://list.tmall.com/search_product.htm?spm=875.7931836/B.subpannel2016028.9.Jj5v5j&q=%CE%C0%D2%C2&pos=9&cat=50025174&style=g&from=sn_1_rightnav&acm=201603151.1003.2.721325&sort=s&search_condition=7&scm=1003.2.201603151.OTHER_1492168466298_721325#J_crumbs")
lenx = soup(url,'html.parser')
fenx = lenx.find_all("div",{"href":re.compile('.+')})
print(fenx)

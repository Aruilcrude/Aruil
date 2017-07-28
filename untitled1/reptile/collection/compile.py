from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re

url = urlopen("http://www.chinacycc.com/forum-67-1.html")
lenx = bs(url,"html.parser")
xue = lenx.find_all("img",{"src":re.compile('http.*\.jpg')})
for fen in xue:
    print(fen['src'])
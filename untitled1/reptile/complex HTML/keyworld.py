#coding = utf-8
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
url = urlopen("http://www.chinacycc.com/forum.php?mod=forumdisplay&fid=56")
lenx = bs(url,"html.parser")
xue  = lenx.find_all(id="toptb")
print (xue[0].get_text())
#coding = utf-8
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re

url = urlopen("http://www.chinacycc.com/forum.php?mod=forumdisplay&fid=56")
lenx = bs(url,"html.parser")
fenx = lenx.find_all("a",{"href":re.compile('.+')})
for fen in fenx:
    print(fen.get_text())

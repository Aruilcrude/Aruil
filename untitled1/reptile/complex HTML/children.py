from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
url = urlopen("http://www.chinacycc.com/forum.php?mod=forumdisplay&fid=56")
lenx = bs(url,"html.parser")
for xue in lenx.find("div",{"src":"href"}).children:
    print(xue)
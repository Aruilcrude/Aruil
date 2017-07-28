from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
url = urlopen("http://www.chinacycc.com/forum-67-1.html")
lenx = bs(url,"html.parser")
for xue in lenx.find("div",{"id":"hd"}).find_all("a",href=re.compile("(^http).*")):
    if 'href' in xue.attrs:
        print(xue.attrs['href'])
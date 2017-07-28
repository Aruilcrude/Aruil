from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re
def url_lenx(url):
    html = urlopen(url)
    boig = bs(html,"lxml")
    return boig.find("ul",{"id":"pins"}).find_all('img')
link = url_lenx('http://www.mzitu.com/taiwan/')
lenx = str(link).split('"')
print(link)

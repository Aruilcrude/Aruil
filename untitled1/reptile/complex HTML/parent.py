from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
url = urlopen("https://list.tmall.com/search_product.htm?q=%CD%BC%C1%E9&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton")
lenx = bs(url,"html.parser")
print(lenx.find_all("div",{"src":"//img.alicdn.com/bao/uploaded/i3/TB1pverIpXXXXcEXXXXqu8pFpXX_120110.jpg_b.jpg"}).parent.p.get_text())
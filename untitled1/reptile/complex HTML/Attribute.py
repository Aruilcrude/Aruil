from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
lenx = set()        #定义一个集合
url = urlopen("http://www.chinacycc.com/portal.php")#打开一个网站
leng = bs(url,"html.parser")     #解析HTML
try:                                  #写下异常
    print(leng.h1.get_text())       #获取h1 里的所有文本内容
    print(leng.find(id = "adiy6"))   #找出所有的id = adiy6
    print(leng.find(id = "portal_block_1123")) #找出对应ID

except AttributeError:                  #触发异常
    print("页面的属性不存在! 不过需要修改一下")

for link in leng.find_all("a",href = re.compile(".+")):   #循环找出所有的符合的URL
    if 'href' in link.attrs:                              #判断href属性是否在link 的所有链接里
        if link.attrs['href'] not in lenx:                #再次判断link的所有链接没在lenx集合里
            feng = link.attrs['href']                    #实例化link 里的所有链接
            print("-------------\n"+feng)              #输出所有链接  用---------隔开
            lenx.add(feng)                     #写入lenx集合里
print(lenx)                                   #再输出集合


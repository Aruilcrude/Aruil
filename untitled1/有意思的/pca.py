from bs4 import BeautifulSoup
import string
import urllib.request
from time import sleep

b = ''
url = r'https://www.amazon.com/gp/search/other/ref=sr_sa_p_4?me=A1GWHXDV5OYG6D&rh=k:T-shirt&keywords=T-shirt&pickerToList=brandtextbin&indexField=%s&ie=UTF8&qid=1493996112'
for c in string.ascii_lowercase + '#':
    sleep(10)
    req = urllib.request.Request(url % c, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'})
    try:
        content = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(content, 'html.parser')

        uls = soup.find_all('ul', {'class': 's-see-all-indexbar-column'})
        for ul in uls:
            links = ul.find_all('a')
            print(len(links))
            for link in links:
                b = b + 'https://www.amazon.com' + link['href'] + '&lo=merchant-items' + '\n'
    except:
        print("I am is hack Aruil")

with open('E:/4.txt', 'w') as f:
    f.write(b)






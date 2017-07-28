import urllib.request as ur
xue = set()
lenx = open("E:/grep/xue/lenx.txt","w")
url = 'http://www.chinacycc.com/portal.php'
conn = ur.urlopen(url)
FENX = conn.read()
print(FENX)
feng = xue.add(FENX)
xin  = str(xue)
lenx.write(xin)
lenx.close()
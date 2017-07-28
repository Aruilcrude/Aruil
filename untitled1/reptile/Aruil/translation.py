from urllib.request import urlopen
import urllib.parse
import json
import time
while True:
    content = input("请输入需要翻译的内容(按'lenx'退出):")
    if content == 'lenx':
        break

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/"
    date = {
        'i': content,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':'1493344583519',
        'sign':'a08114a3ef2fa6798f1b7975925c4320',
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_CLICKBUTTON',
        'typoResult':'true'
    }

    date = urllib.parse.urlencode(date).encode('UTF-8')
    response = urlopen(url,date)
    html = response.read().decode('UTF-8')
    target = json.loads(html)
    print("翻译结果: %s" %(target['translateResult'][0][0]['tgt']))
    time.sleep(1)

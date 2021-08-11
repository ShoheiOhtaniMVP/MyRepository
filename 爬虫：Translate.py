import urllib.request
import urllib.parse
import json
import time
import installOpener

while True :
        content = input("请输入要翻译的内容(输入exit退出):")
        installOpener.installOpener()
        if content == "exit":
                break;
        url = "https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
        data = {'i': content,
                'from': 'AUTO',
                'to': 'AUTO',
                'smartresult': 'dict',
                'client': 'fanyideskweb',
                'sign': '32beaaeccb65f2b8405c11da0ed6f846',
                'lts': '1628351213531',
                'bv': 'eda468fc64295ecf2810ab8a672c2db1',
                'doctype': 'json',
                'version': '2.1',
                'keyfrom': 'fanyi.web',
                'action': 'FY_BY_CLICKBUTTION'}
        data = urllib.parse.urlencode(data).encode('utf-8')

        req = urllib.request.Request(url, data, head)
        response = urllib.request.urlopen(url,data)
        html = response.read().decode("utf-8")
        target = json.loads(html)

        def getTarget():
            return target['translateResult'][0][0]['tgt']

        print("翻译的结果为：" + getTarget())
import time
import urllib.request
import Req, installOpener
import json

def getUrl():
    access = input('请输入up主的UID：')
    url = 'https://api.bilibili.com/x/relation/stat?vmid=' + access + '&jsonp=jsonp'
    return url

if __name__ == '__main__':
    newurl = getUrl()
    req = Req.getReq(newurl)
    const = int(input('输入想要运行的秒数：'))
    filename = input('请输入你存储数据的文件名：')
    while const>=0:
        f = open(filename + '.txt','a')
        installOpener.installOpener()
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        follower = json.loads(html)
        target = follower['data']['follower']
        print('此up主的实时粉丝数为：%d' %(target))
        f.writelines(str(target) + '\n')
        time.sleep(1)
        const = const - 1
        f.close()

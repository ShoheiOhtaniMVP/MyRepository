import urllib.request
import random

iplist = ['117.94.222.152', '114.98.114.2', '118.117.188.191', '223.244.179.85', '106.45.104.24', '121.232.148.90', '175.7.199.185', '111.72.25.142', '118.117.189.122', '121.230.210.23', '182.84.144.8', '117.64.237.165', '47.98.179.39', '106.45.104.21', '121.226.21.143']

def installOpener():
    proxy_support = urllib.request.ProxyHandler({'http': random.choice(iplist)})
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36')]
    urllib.request.install_opener(opener)
import urllib.request
import os
import installOpener

global access, url, pages          #定义全局变量
access = ''                        #access是接收到的本子地址
newaccess = []                     #newaccess是修改过的本子地址，通过它才能找到图片地址
url = []                           #url是图片的最终地址
pages = 0                          #pages是本子的页数

def isExit1(str):                   #此函数判断输入的地址是否格式正确
    if str == 'exit':
        return 1
    else:
        return 0

def isExit2(str):
    if str[:5] != 'https':
        return 1
    else:
        return 0

def isExit3(str):
    try:
        if type(int(str)) != 'int':
            pass
    except ValueError:
        return 1
    else:
        return 0


def newFolder():                   #此函数数新建了一个文件夹用于储存本子
    folder = input('请新建一个文件夹：')
    if isExit1(folder) :
        print('程序退出！')
        return 1
    else:
        folder = 'E:\\图片资源\\本子\\' + folder
        os.mkdir(folder)
        os.chdir(folder)
        return 0

def getInformation():              #此函数用于获得access和pages
    global access, pages,boolean
    access = input('请输入本子的地址：')
    if isExit1(access):
        print('程序退出！')
        return 1
    elif isExit2(access):
        print('地址格式不正确！程序退出！')
        return 1
    else:
        pages = input('请输入本子的页数：')
        if isExit1(pages):
            print('程序退出！')
            return 1
        elif isExit3(pages):
            print('没有输入数字！程序结束！')
            return 1
        else:
            boolean = 1
            return 0


def getAccess():                   #此函数用于修改access，并将新的access存储在newaccess中
    global access, newaccess, pages
    for each in range(int(pages)):
        address = access + 'list/' + str(each+1) +'/'
        newaccess.append(address)

def findImages():                  #此函数用于利用newaccess找到真正的图片地址，并存储在url中
    global newaccess,url,pages
    for each in range(int(pages)):
        req = urllib.request.Request(newaccess[each])
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36')
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        a = html.find('https://i1')
        b = html.find('"', a)
        url.append(html[a:b])

def getImages():                   #此函数用于利用url找到图片并下载到指定的文件夹
    global url,pages
    for each in range(int(pages)):
        req = urllib.request.Request(url[each])
        req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36')
        response = urllib.request.urlopen(req)
        img = response.read()
        f = open('第' + str(each+1)+ '页.jpg', 'wb')
        f.write(img)
    f.close()
    print('下载成功')

if __name__ == '__main__' :         #最终执行的程序
    while True:
        print('任何时候输入exit都可以结束程序。')
        if newFolder():
            break
        if getInformation():
            break
        installOpener.installOpener()
        getAccess()
        findImages()
        getImages()
        j = input('是否退出？输入“是”退出，输入其他字符继续：')
        if j == '是' or j == 'exit':
            break
        else:
            continue
import os
import configparser
import urllib.request as req
import re
import time
import easygui
import sys
import os.path
import json
import stat
from you_get import common as you_get 
def geturl(url):
    webpage = req.urlopen(url)
    data = webpage.read()
    data = data.decode('utf-8')
    return data
shuju=easygui.enterbox('请输入一个av或bv号')
if shuju[0] == 'b' or shuju[0] == 'B':
    info = 1
elif shuju[0] == 'a' or shuju[0] == 'A':
    info = 0
else:
    easygui.msgbox("数据错误！！！")
    exit()
curpath=os.path.dirname(os.path.realpath(__file__))
conf=configparser.RawConfigParser()
conf.read("config.ini")
ver = conf.get("ver","version")
if info == 1:    
    api = conf.get("api","bvtoav").replace('%bv%',shuju).replace('%nobvbv%',shuju[2:]).replace('%ver',ver)
else:
    api = conf.get("api","avtobv").replace('%av%',shuju).replace('%noavaid%',shuju[2:]).replace('%ver%',ver)
updata = conf.get("updata","server").replace('%ver%',ver)
if geturl(updata)!='SUCCESS':
    easygui.msgbox(geturl(updata))
    exit()
f=open(shuju+'.json', 'w')
f.write(geturl(api))
f.close()
json=json.loads(geturl(api))
if json['code']!=0:
    easygui.msgbox('解析视频失败！')
    exit()
print('BV号：'+str(json['data']['bvid'])+'   AV号：AV'+str(json['data']['aid']))
if json['data']['copyright']==1:
    print('此作品为原创')
else:
    print('此作品为搬运')
print('视频封面外链：'+json['data']['pic'])
print('视频标题：'+json['data']['title'])
print('视频简介：'+json['data']['desc'])
print('视频作者：'+json['data']['owner']['name'])
print('作者头像：'+json['data']['owner']['face'])
print('视频mid：'+str(json['data']['owner']['mid']))
print('视频cid：'+str(json['data']['cid']))
print('视频类别：'+json['data']['tname'])
print('此视频现在有：')
print(str(json['data']['stat']['view'])+'次观看')
print(str(json['data']['stat']['danmaku'])+'条弹幕')
print(str(json['data']['stat']['reply'])+'条评论')
print(str(json['data']['stat']['favorite'])+'个收藏')
print(str(json['data']['stat']['coin'])+'个硬币')
print(str(json['data']['stat']['share'])+'次分享')
print(str(json['data']['stat']['like'])+'个点赞')
lll = int(input("\n输入1下载此视频，输入2退出："))
if lll==2:
    exit()
elif lll==1:
        directory = r'./'                         #设置下载目录
        url = 'https://www.bilibili.com/video/'+shuju      #需要下载的视频地址
        sys.argv = ['you-get','-o',directory,url]       #sys传递参数执行下载，就像在命令行一样
        you_get.main()
else:
    print("ERROR!!!")
    exit()
print('\n\n\nBILIBILI TOOL 2020 By YKM\n\n\n')

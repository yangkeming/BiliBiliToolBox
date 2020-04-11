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
def geturl(url):
    webpage = req.urlopen(url)
    data = webpage.read()
    data = data.decode('utf-8')
    return data
shuju = str(sys.argv[1])
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

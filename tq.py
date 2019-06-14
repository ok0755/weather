#coding=utf-8
#author:zhoub
import requests
from lxml import etree
import json
import os
from tabulate import tabulate

def WT(url):
    global arr
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
    req = requests.get(url,headers=header)
    html = req.json()
    req.close()
    detail = html['data']['forecast']
    arr.append([html['data']['city']])
    for d in detail:
        arr.append([d['date'],d['type'],d['low'][3:-1]+' ~ '+d['high'][3:-1],d['fengxiang'],d['fengli'][9:-3]])
    arr.append([''])
    return arr

if __name__=='__main__':
    arr = []
    tabulate_header = [u'日期',u'天气',u'气温',u'风向',u'风力']
    url1 = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101280605'  ## 宝安
    url2 = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101220304'  ## 南陵
    url3 = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101190801'  ## 徐州
    WT(url1)
    WT(url2)
    WT(url3)
    print(tabulate(arr,headers=tabulate_header,tablefmt='rst',stralign='center',missingval='  '))
    os.system('pause')
#coding=utf-8
#author:zhoub

from Tkinter import *
import requests
from lxml import etree
import os

def tq(url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
    response = requests.get(url,headers=header)
    response.encoding = 'utf-8'
    req = response.text
    response.close()
    selectors = etree.HTML(req)
    city = selectors.xpath('.//title/text()')[0][1:5]
    arr = []
    arr.append(city)
    ul = selectors.xpath('.//ul[@class="t clearfix"]/li')
    for d in ul:
        date = d.xpath('./h1/text()')[0]
        weather = d.xpath('./p[@class="wea"]/text()')[0]
        temperature = d.xpath('normalize-space(./p[@class="tem"])').replace('/','~')
        logo_day = d.xpath('.//big/@class')[0].replace('png40 ','')
        logo_night = d.xpath('.//big/@class')[1].replace('png40 ','')
        arr.append([date,logo_day,logo_night,weather,temperature])
    return arr

nlx = tq("http://www.weather.com.cn/weather/101220304.shtml")     ## 南陵天气
bao = tq("http://www.weather.com.cn/weather/101280605.shtml")     ## 宝安天气

root=Tk()
root.title(u'天气预报')
root.geometry('320x540+500+250')
##root.iconbitmap('d:\\weather72.ico')
root.resizable(width=False,height=False)
root.attributes("-alpha",0.9)

def UI(i,lists):
    global root
    for n in lists[1:]:
        Label(root,text=n[0]).grid(sticky=W,row=i+1,column=0)  ##日期
        """　插入天气图标 """
        gif = PhotoImage(file=r'd:\tq\%s.gif'%n[1])
        lable = Label(root,image=gif)
        lable.image=gif
        lable.grid(sticky=W,row=i+1,column=1)
        gif2 = PhotoImage(file=r'd:\tq\%s.gif'%n[2])
        lable2 = Label(root,image=gif2)
        lable2.image=gif2
        lable2.grid(sticky=W,row=i+1,column=2)
        Label(root,text=n[3]).grid(sticky=W,row=i+1,column=3)
        Label(root,text=n[4]).grid(sticky=W,row=i+1,column=4)
        i+=1
Label(root,text=nlx[0]).grid(sticky=W,row=0,column=0)
UI(0,nlx)
Label(root,text=bao[0]).grid(sticky=W,row=8,column=0)
UI(9,bao)
root.mainloop()
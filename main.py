#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time, datetime
from weibo_login import *
from sendweibo import *
from news import *
from bilibili import *
from tumblr import *
from twitterspider import *
from event import *

def updatetwitter(name, tag):
    global limit, pausetime
    try:        
        weibos=spider(name, limit)
        send(tag, weibos, pausetime, limit)

    except Exception as e:
        print(e)
        print(name, tag)
        time.sleep(pausetime)
        
def updatetumblr(name, tag):
    global limit, pausetime
    try:
        weibos=gettumblr(name, limit)
        send(tag, weibos, pausetime, limit)
                
    except Exception as e:
        print(e)
        print(name, tag)
        time.sleep(pausetime)        
        
def updatenews(name, tag):
    global limit, pausetime
    try:
        weibos=getnews(name, limit)
        send(tag, weibos, pausetime, limit)

    except Exception as e:
        print(e)
        print(name, tag)
        time.sleep(pausetime)   

def updatebilibili(name, tag):
    global limit, pausetime
    try:
        weibos=getbili(name, limit)
        send(tag, weibos, pausetime, limit)
                
    except Exception as e:
        print(e)
        print(name, tag)
        time.sleep(pausetime)         

def updateevent(name, tag):
    try:
        weibos=getevent(name)
        send(tag, weibos, pausetime, limit)
                
    except Exception as e:
        print(e)
        print(name, tag)
        time.sleep(pausetime)    
        

def start():
    global limit, pausetime
    limit=7
    pausetime=0.1

    #更新twitter

    name='kinmosa_anime'
    tag='#ＴＶアニメ「きんいろモザイク」#twitter:'
    updatetwitter(name, tag)

    name='suzakinishi'
    tag='#洲崎西#twitter:'
    updatetwitter(name, tag)

    name='suzakiaya7_6'
    tag='「洲崎綾の7.6」公式twitter:'
    updatetwitter(name, tag)

    name='suzaki_aya'
    tag='#洲崎綾#三十路記念twitter:'
    updatetwitter(name, tag)

    name='nishi_deliradi'
    tag='#西明日香のデリケートゾーン！#twitter:'
    updatetwitter(name, tag)

    name='nishiasuka_info'
    tag='#西明日香#公式ツイッター:'
    updatetwitter(name, tag)   
        
    name='akekodao'
    tag='#明坂聡美#twitter:'
    updatetwitter(name, tag)


    #更新 tumblr

    name='洲崎綾'
    tag='#洲崎綾##tumblr#'
    updatetumblr(name, tag)

    name='西明日香'
    tag='#西明日香##tumblr#'
    updatetumblr(name, tag)

    name='種田梨沙'
    tag='#種田梨沙##tumblr#'
    updatetumblr(name, tag)

    name='佐倉綾音'
    tag='#佐倉綾音##tumblr#'
    updatetumblr(name, tag)   


    #更新news

    name='洲崎綾'
    tag='#洲崎绫##News#'   
    updatenews(name, tag)

    name='西明日香'
    tag='#西明日香##News#'   
    updatenews(name, tag)

    name='種田梨沙'
    tag='#種田梨沙##News#'   
    updatenews(name, tag)

    name='佐倉綾音'
    tag='#佐倉綾音##News#'   
    updatenews(name, tag)


    #更新bilibili

    name='洲崎绫'
    tag='#洲崎绫##bilibili#'        
    updatebilibili(name, tag)

    name='西明日香'
    tag='#西明日香##bilibili#'        
    updatebilibili(name, tag)

    name='種田梨沙'
    tag='#種田梨沙##bilibili#'        
    updatebilibili(name, tag)

    name='佐倉綾音'
    tag='#佐倉綾音##bilibili#'        
    updatebilibili(name, tag)   

    #更新event

    name='洲崎綾/3902'
    tag='#洲崎绫##Event countdown#'    
    updateevent(name, tag)

    name='西明日香/2470'
    tag='#西明日香##Event countdown#'    
    updateevent(name, tag)

    name='種田梨沙/3528'
    tag='#種田梨沙##Event countdown#'    
    updateevent(name, tag)

    name='佐倉綾音/2650'
    tag='#佐倉綾音##Event countdown#'    
    updateevent(name, tag)

if __name__ == '__main__':
    start()

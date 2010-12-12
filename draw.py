#!/usr/bin/env python
# encoding: utf-8
"""
draw.py

"""
import os
import sys
import glob
import Image
import ImageDraw
import ImageFont
import ImageFilter

from hashlib import md5
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import HttpResponse

#necessary to force chinese encoding(utf8)
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding) 

def findPath(path):
    '''path is a relative;
    return absolute path based on the project folder'''

    return os.path.join(os.path.dirname(__file__), path) 

def delete_pic(remain=100):
    '''delete old pics so as to reduce the disk usage'''

    p=findPath("media/result/*.png")

    files=glob.glob(p)
    s={}
    for f in files:
        statinfo=os.stat(f)
        s[f]=statinfo.st_mtime        

    c= s.items()
    c.sort(key=lambda x:x[1]) 

    if len(c)<=remain:
        pass
    else:
        for (x,y) in c[0:len(c)-remain]:            
            os.unlink(x)

def fontFile(font):
    return findPath("font/%s" % font) 

def fontPosition(pFont):
    '''specify the position and size for each font'''
    if pFont.find("wqy")!=-1: #for wenquanyi
        textPosition=(20, 15)
        fontSize=150 
    elif pFont.find("xujinglei")!=-1: #for xujinglei
        textPosition=(10, 10)
        fontSize=170 
    elif  pFont.find("YaHei") !=-1: 
        textPosition=(25, 0)
        fontSize=140
    elif pFont.find("fzybksjt") !=-1: #fang zheng ying kai jian
        textPosition=(15, 15)
        fontSize=160 
    elif pFont.find("fzqtj") !=-1: #fang zheng ying kai jian
        textPosition=(15, 15)
        fontSize=160 
    elif pFont.find("shoujin") !=-1: #fang zheng ying kai jian
        textPosition=(18, 18)
        fontSize=155 
    elif pFont.find("msjhbd") !=-1 :
        textPosition=(18, -8)
        fontSize=155 
    elif pFont.find("liuti") !=-1 :
        textPosition=(15, 15)
        fontSize=165
    elif pFont.find("fangzhengsuxinshiliukaijianti") !=-1 :
        textPosition=(15, 15)
        fontSize=165 
    return (textPosition, fontSize) 


def my_draw(request,bg, text, font, textColor, shadowColor, border, shadow, highlight):
    """draw avatar. Core part of the program."""

    delete_pic()

    pure=md5(text+bg+font+textColor+shadowColor+str(border)+str(shadow)+str(highlight)).hexdigest()+".png" 
    filename=findPath('media/result/')+pure 
    pFont=fontFile(font)

    (textPosition, fontSize)=fontPosition(pFont)

    #generate new pic only when not existing 
    if not os.path.exists(filename):
        # when debugging, set if to 1, so as to gen pic each time;
        # when done, set if to not os.path.exists(filename), and only gen new pics.
        
        image_a=Image.open(findPath("colors/%s" % bg))
        image_b=Image.open(findPath("colors/%s" % bg))
        font=ImageFont.truetype(pFont, fontSize)
        width=180
        height=180
        img_draw=ImageDraw.Draw(image_b)
        shadow=int(shadow)
        if shadow ==0:    #no shadow at all
            img_draw.text(textPosition,text,font=font, fill=textColor) 
            image_b.save(filename)
        else  :
            if shadow==2: #shadow offset
                side=15
            else:         #shadow but no offset
                side=10 

            box=(10,10,width+10, height+10)
            position=(0+side,0+side, width+side, height+side)

            img_draw.text(textPosition,text,font=font,fill=shadowColor) 
            imgfilted=image_b.filter(ImageFilter.BLUR) 
            region=imgfilted.crop(box)
            img_draw=ImageDraw.Draw(image_a) 
            image_a.paste(region,position)
            img_draw.text(textPosition,text,font=font, fill=textColor) 
            image_a.save(filename)

  
    url="""./site_media/result/%s""" % pure
    html="""<a href="/result?url=%s"><img src="%s"></a>""" % (url, url)
    return HttpResponse(html)


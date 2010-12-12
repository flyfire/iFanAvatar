#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#author:         rex
#blog:           http://iregex.org
#filename        index.py
#created:        2010-12-06 15:38
import os
import Image

import ImageDraw
import ImageFont
import ImageFilter
from django.http import HttpResponse
from draw import findPath
from hashlib import md5

def draw_hat(bg, hat, angle, offsetLeft, offsetTop, hatWidth, hatHeight):
    
    filename=md5("".join([str(x) for x in [bg, hat, angle, offsetLeft, offsetTop, hatWidth, hatHeight]])).hexdigest()+".png"
    filename=findPath('media/result/')+filename 
    bg=bg[-49:] #/site_media/result/bc98ff0348403f8098a3f7207c29f94f.png
    
    bg=findPath(bg)
    bg=Image.open(bg)
    
    hat=hat[hat.index("media"):hat.index("png")+3]
    hat=findPath(hat)
    hat=Image.open(hat)
    
    #resize the hat
    hat=hat.resize((hatWidth, hatHeight), Image.ANTIALIAS)
    hat=hat.rotate(angle, Image.BILINEAR, expand=1)
    box=(0, 0, hat.size[0], hat.size[1])
    pisition=(offsetLeft, offsetTop, hat.size[0]+offsetLeft, hat.size[1]+offsetTop)
    bg.paste(hat,pisition, hat)
    
    #save as file
    bg.save(filename, "PNG")
    filename=filename[-49:]
       
    url="""./site_%s""" % filename
    html="""<a href="/result?url=%s"><img src="%s"></a>""" % (url, url)
    return HttpResponse(html)

#!/usr/bin/env python
# encoding: utf-8

import os
import random

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
from django.shortcuts import render_to_response
from fontdict import fontdict
from draw import my_draw 
from hat import draw_hat
from misc import getVersionInfor


def fontcss():
    '''generate css for fonts; '''
    format='''
/****           %s           ****/ 
@font-face {
  font-family: "%s";
  src: url(/site_media/font/%s);
}'''
    css=''
    for font in fontdict.keys():
        css += format % (fontdict[font], font, font)
    return css
#    response = HttpResponse(mimetype='text/plain; charset=utf-8')
#    response.write(css)
#    return response 

def home(request):
    '''index view'''
    
    version,build = getVersionInfor()
    t = get_template('index.html')
    
    html = t.render(Context({'fontdict':fontdict,
#        'fontcss': fontcss(),
        "version":  version,
        "build":    build}))
    return HttpResponse(html)

def generate(request):

    bg = request.GET.get('bg', '')  #can be changed to POST
    if not bg or bg=='undefined':#undefined
        bg='logo192.png'
    text=request.GET.get('text', '')
    font=request.GET.get('font', '')
    textColor=request.GET.get('textColor', '')
    shadowColor=request.GET.get('shadowColor', '')

    #boolean args
    border=eval(request.GET.get('border', '')) 
    shadow=eval(request.GET.get('shadow', '')) 
    highlight=eval(request.GET.get('highlight', '')) 
    
    return my_draw(request,
            bg=bg,
            text=text,
            font=font,
            textColor=textColor,
            shadowColor=shadowColor,
            border=border,
            shadow=shadow,
            highlight=highlight)
    
    
def generate_random(request):
    bgPath = os.getcwd() + "/media/colors/"
    fontPath = os.getcwd() + "/media/font"

    def randomColorUnit():
        return str(hex(random.randrange(0x00, 0xFF))[2:]).zfill(2)

    bg = random.choice(os.listdir(bgPath))
    text = request.GET.get('text', '')
    font = random.choice(os.listdir(fontPath))
    textColor = "#" + randomColorUnit() + randomColorUnit() + randomColorUnit()
    shadowColor = "#" + randomColorUnit() + randomColorUnit() + randomColorUnit()
    border = random.randint(0, 1)
    shadow = random.randint(0, 2)
    highlight = random.randint(0, 1)

    return my_draw(request, bg, text, font, textColor, shadowColor, border, shadow, highlight)

def hat(request):
    
    bg = request.GET.get('bg', '')  #can be changed to POST
    hat=request.GET.get('hat', '')
    angle=int(float(request.GET.get('angle', '')))
    offsetTop=int(float(request.GET.get('offsetTop', '')))
    offsetLeft=int(float(request.GET.get('offsetLeft', '')))
    hatHeight=int(float(request.GET.get('hatHeight', '')))
    hatWidth=int(float(request.GET.get('hatWidth', '')))
    
    return draw_hat(bg, hat, angle, offsetLeft, offsetTop, hatWidth, hatHeight) 

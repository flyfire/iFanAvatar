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
    hat=request.GET.get('hat', '')
    angle=int(float(request.GET.get('angle', '')))
    offsetTop=int(float(request.GET.get('offsetTop', '')))
    offsetLeft=int(float(request.GET.get('offsetLeft', '')))
    hatHeight=int(float(request.GET.get('hatHeight', '')))
    hatWidth=int(float(request.GET.get('hatWidth', '')))
    
    return draw_hat(bg, hat, angle, offsetLeft, offsetTop, hatWidth, hatHeight) 
        
   
    

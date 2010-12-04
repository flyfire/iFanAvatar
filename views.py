#!/usr/bin/env python
# encoding: utf-8

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
from django.shortcuts import render_to_response
from fontdict import fontdict
from draw import my_draw
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
    

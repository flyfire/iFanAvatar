#!/usr/bin/env python
# encoding: utf-8
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
from django.shortcuts import render_to_response
from fonts import fonts
from draw import my_draw

def home(request):
    '''
        html = t.render(Context({'current_date': now}))
        return HttpResponse(html)
    '''
    t = get_template('index.html')
    html = t.render(Context({'fonts':fonts}))
    return HttpResponse(html)

def generate(request):

    bg = request.GET.get('bg', '')  #can be changed to POST
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
    

#!/usr/bin/env python
# encoding: utf-8
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response

from draw import my_draw
def home(request):
    return render_to_response('index.html')

def generate(request):
    bg = request.GET.get('bg', '')  #can be changed to POST
    char=request.GET.get('char', '')
    font=request.GET.get('font', '')
    print 'we got font', font
    return my_draw(request,char,bg,font)
    

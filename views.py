#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
import Image
import ImageDraw
import ImageFont
import ImageFilter 
import sys
import md5
import os
import glob
from django.template.loader import get_template
from django.shortcuts import render_to_response
from rex.tips.models import Tips


default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


def delete_pic(remain=36):
    p="/home/zhasm/www/rex/media/*.png"
    files=glob.glob(p)
    s={}
    for f in files:
        statinfo=os.stat(f)
        s[f]=statinfo.st_mtime        

    c= s.items()
    c.sort(key=lambda x:x[1]) 
    #[(0, 9), (1,8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1), (9, 0)] 
    #print len(c)
    #print c
    if len(c)<=remain:
        pass
    else:
        for (x,y) in c[0:len(c)-remain]:            
            os.unlink(x)


def my_draw(request,mychar,bg):
    """
    
    """
    
    
    delete_pic()    
    text=mychar[0:1]
    pure=md5.new(text+bg).hexdigest()+".png" 
    filename="/home/zhasm/www/rex/media/"+pure
    
    #generate new pic only when not existing
    if not os.path.exists(filename):
        image_a=Image.open("/home/zhasm/www/rex/colors/bg.png")
        image_b=Image.open("/home/zhasm/www/rex/colors/%s"%bg)
        font=ImageFont.truetype("/home/zhasm/www/rex/iYaHei.ttf",150) 
        font2=ImageFont.truetype("/home/zhasm/www/rex/iYaHei.ttf",154) 

        img_draw=ImageDraw.Draw(image_b)
        img_draw.text((20,-15),text,font=font,fill="#808080")
        imgfilted=image_b.filter(ImageFilter.BLUR)

        img_draw=ImageDraw.Draw(image_a)

        box=(0,0,190,190)
        position=(5,5,195,195)
        region=imgfilted.crop(box)
        image_a.paste(region,position)
        img_draw.text((25,-10),text,font=font,fill="#ffffff") 
        
        image_a.save(filename)

    #display the picture;
    #img tag is enough, for this is displayed in pic_output div.
    html="""<img src="./site_media/%s">"""%pure
    return HttpResponse(html)


def index(request):
    
    #html=""""""
    #files=glob("./media/*.png")
    
    return render_to_response('index.html', {'tips':Tips.objects.all()})
    #t = get_template('')
    #html = t.render(Context({'current_date': now}))
    #return HttpResponse(t)

    #return HttpResponse(html)

def generate(request):
    
    bg = request.POST.get('bg', '')
    dtext=request.POST.get('dtext', '')
    if not bg or not dtext:    
        return HttpResponse("输入一个汉字！")
    else:
        return my_draw(request,dtext,bg)

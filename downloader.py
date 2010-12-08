#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#author:         rex
#blog:           http://iregex.org
#filename        dowloader.py
#created:        2010-12-08 10:29
from django.http import HttpResponse
from draw import findPath
def downloader(request):
    url = request.GET.get('url', '')  #can be changed to POST
    #

    #get the absolute filepath:
    url=url[-49:] 
    if len(url)!=49:
        return HttpResponse("""<script>alert("下载文件出错！\\n 请重新点击生成按钮。");</script>""");
    fn=findPath(url)

    #get content 
    try:
        f=open(fn, "rb")
        content=f.read()
        f.close()
    except:
        return HttpResponse("""<script>alert("读取图片文件出错！");</script>""");

    #return the filecontent
    response = HttpResponse(content, mimetype="image/png")
    response['Content-Disposition'] = 'attachment; filename=%s' % url[-36:] 
    return response



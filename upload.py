from django.http import HttpResponse
from draw import findPath

def upload(request):

    if request.method == 'POST': 
        fn=request.FILES['file'].name
        filehandle=open(findPath("media/result/"+fn), "wb")
        filehandle.write(request.FILES['file'].read())
        filehandle.close()
        fn="/site_media/result/"+fn
        return HttpResponse("""{"fn":"%s"}""" % fn, mimetype="text/javascript")
    else: 
        return HttpResponse("")

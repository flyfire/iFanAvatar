# encoding: utf-8
from django.conf.urls.defaults import *
from views import home, generate, generate_random, hat
from upload import upload
import os.path
from downloader import downloader

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
STATIC_DOC_ROOT = os.path.join(os.path.dirname(__file__), 'media').replace('\\','/')


urlpatterns = patterns('',
    # Example:
    # (r'^iFanAvatar/', include('iFanAvatar.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^/?$', home),
    (r'^gen$',generate),
    (r'^random$', generate_random),
    (r'^result$', downloader),
    (r'^hat$', hat),
    (r'^upload$', upload),
    (r'^site_media/(?P<path>.*/?)$', 'django.views.static.serve',
            {'document_root': STATIC_DOC_ROOT}),
)

from django.conf.urls.defaults import *
from views import index,generate
from django.contrib import admin


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
STATIC_DOC_ROOT = '/home/zhasm/www/rex/media/'
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    # (r'^rex/', include('rex.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    (r'^generate.*?$',generate),
    (r'^$',index),
    (r'^site_media/(?P<path>.*/?)$', 'django.views.static.serve',
            {'document_root': STATIC_DOC_ROOT}), 
    (r'^admin/(.*)', admin.site.root),
)

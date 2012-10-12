from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from rec.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'init/$',create_all ),
                      url(r'^users/(?P<uid>\d+)/',user_detail),
                       url(r'^create/',create_rank_view),
##                       url(r'^films/(?P<id>\d+)/',function),
                      ## url(r'^recomendation/', include('recomendation.foo.urls')),

    #Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

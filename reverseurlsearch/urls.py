# from django.conf.urls import patterns, include, url
#from django.conf.urls import *
from django.conf.urls.defaults import *
from views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^$', 'reverseurlsearch.views.home'),
    (r'^processUrl/', 'reverseurlsearch.views.processUrl'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

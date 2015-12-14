from django.conf.urls import patterns,include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
        
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('pulsarvpn.urls')),
    # url(r'^likes/', include('likes.urls')),
    # (r'^', include('ratings.urls')),
    
)

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'productManage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^bo/', include('product_bo.urls')),
    url(r'^admin/', include(admin.site.urls)),
]


if settings.DEBUG:  
   urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }))
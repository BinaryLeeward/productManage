from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'photo', views.photo, name='photo'),
    url(r'add', views.add, name='add'),
    url(r'listProduct', views.listProduct, name='listProduct')
]
from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), #如果有人访问 'http://127.0.0.1:8000' 地址，那么 views.post_list 是这个请求该去到的地方
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]

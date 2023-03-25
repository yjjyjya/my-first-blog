from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), #如果有人访问 'http://127.0.0.1:8000' 地址，那么 views.post_list 是这个请求该去到的地方
]

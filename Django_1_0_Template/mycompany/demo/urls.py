from demo.views import detail
from django.urls import path, include, re_path as url
from django.contrib import admin

urlpatterns = [
    # url(r'^demo/$', detail, name='detail'),
     url(r'^$', detail, name='detail'),
]

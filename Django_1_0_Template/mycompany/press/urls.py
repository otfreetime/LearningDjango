from press.models import PressRelease
from .views import detail, functional_detail_view, functional_list_view, press_list
from django.urls import path, include, re_path as url
from django.contrib import admin
from django.views.generic import RedirectView,ListView

press_list_dict = {
    'queryset': PressRelease.objects.all(),
}


urlpatterns = [
    # url(r'^demo/$', detail, name='detail'),
    # url(r'^detail/(?P<pk>\d+)/$', detail,name='detail'),
    # url(r'list/$',press_list,name='press-list'),
    url(r'$', RedirectView.as_view(url='/press/list/')),
    url(r'list/$', functional_list_view),
    url(r'^detail/(?P<pk>\d+)/$', functional_detail_view,name='functional-detail-view'),
]

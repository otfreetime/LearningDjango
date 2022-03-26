# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import  path
from django.views.generic.base import View
from .views import PostView
from . import views

urlpatterns = [

    # The home page
    path('1/', PostView.as_view(), name="cgs-lookup"),
    path('', views.index, name='index'),


]

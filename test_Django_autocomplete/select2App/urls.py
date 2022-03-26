# urls.py
from django.urls import  path

from . import views

urlpatterns = [
    path("create/", views.createView, name="create-view")
]
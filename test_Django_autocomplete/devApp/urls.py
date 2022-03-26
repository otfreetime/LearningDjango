
from django.urls import  path
from django.views.generic.base import View
from .views import createView , generateView
from . import views

urlpatterns = [
       path('', createView.as_view(), name="create-codes"),
       path('generate/', views.generateView, name="generate-codes")
]

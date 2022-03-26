"""
test_Django_autocomplete URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path, include
from  App.views import *


from dal import autocomplete
from django.urls import re_path as url
from .models import  *






#from .views import CountryAutocomplete

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('', home),
    path('home/', home),
    path('search/', search_address),
    path('list', search),
    path('address/new/', address_form),
    url(r'^address-autocomp/$', AddressAutocomp.as_view(), name='address-autocomp'),
 
    #url(
    #    'test-autocomplete/',
    #    autocomplete.Select2QuerySetView.as_view(model=FakeAddress),
    #    name='select2_fk',
    #),
    #url(
    #    r'^country-autocomplete/$',
    #    CountryAutocomplete.as_view(),
    #    name='country-autocomplete',
    #),
]

#urlpatterns.extend(TestForm.as_urls())

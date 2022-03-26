from django.contrib import admin
from django.urls import path,include, re_path as url
from . import views
from .views import *
import djhacker 


urlpatterns = [
	path('admin/', admin.site.urls),
	path('',views.home,name='home'),
	#url(r'^language-autocomplete/$',languageAutocomplete.as_view(),name='language-autocomplete'),,
	url(
        'test-autocomplete/$',
        autocomplete.Select2QuerySetView.as_view(
            queryset= Language.objects.all(),
        ),
        name='language-autocomplete'),

]



# # don't forget to pip install djhacker
#import djhacker 
#from django import forms
#djhacker.formfield(
#    Language.name,
#    forms.ModelChoiceField,
#    widget=autocomplete.ModelSelect2(url='language-autocomplete')
#)
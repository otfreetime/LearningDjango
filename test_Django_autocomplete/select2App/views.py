
# views.py
#from django.http import HttpResponse
#from django.views import generic
from django.shortcuts import render
from .forms import createForm
#from .models import  models



def createView(response):
    form = createForm()
    return render(response, "select2App/createPage.html",{'form': form})
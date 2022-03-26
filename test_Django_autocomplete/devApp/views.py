#from django.forms import models
#from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import  createForm , generateForm
from .models import  CodesModel , GenerateModel

class createView(CreateView):
    model=CodesModel
    form_class=createForm
    template_name = 'devApp/createPage.html'
   

def generateView(response):
    if response.method== "POST":
        form = generateForm(response.POST)
        if form.is_valid():
            form.save()
    else:  
        form = generateForm()

    return render(response, "devApp/generatePage.html",{'form': form})
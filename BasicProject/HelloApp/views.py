
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()
    return render(
        request,
        "HelloApp/index.html",  
        {
            'title':"Hello Django",
            'message':"Hello Django!",
            'content': "on " + now.strftime("%A, %d %B, %Y at %X"),
        }
    )   
      
def about(request):
    return render(
        request,
        "HelloApp/about.html",
        {
            'title' : "About HelloApp",
            'content' : "Example app page for Django."
        }
    )